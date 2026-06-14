"""
protocol_registry_service.py

Stores every generated protocol in SQLite and provides query functions
used by impact_analysis_service to find real protocol names.

Eliminates hallucinated protocol IDs (ALG-VER-PROT-008 etc.)
by giving Gemini only protocols that actually exist.

Called by:
    protocol_service.py  — register_protocol() after successful generation
    impact_analysis_service.py — format_protocol_impact_for_prompt()
"""

import sqlite3

DB = "alta_poc.db"


# ============================================================
# REGISTER
# ============================================================

def register_protocol(protocol_data: dict):
    """
    Store a generated protocol in the registry.

    Args:
        protocol_data: The parsed JSON dict from protocol_service.generate_protocol()
                       Must contain "protocol_info" and "test_cases" keys.

    Safe to call even if tables don't exist yet — fails silently.
    """
    try:
        info = protocol_data.get("protocol_info", {})
        pid  = info.get("protocol_id", "").strip()
        if not pid:
            return

        conn = sqlite3.connect(DB)
        c    = conn.cursor()

        c.execute("""
            INSERT OR REPLACE INTO generated_protocols
            (protocol_id, protocol_name, feature, objective,
             related_requirements, related_risks, related_screens,
             related_parameters, tc_count, source_input)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            pid,
            info.get("protocol_name", ""),
            info.get("feature", ""),
            info.get("objective", ""),
            ", ".join(info.get("related_requirements", [])),
            ", ".join(info.get("related_risks", [])),
            ", ".join(info.get("related_screens", [])),
            ", ".join(info.get("related_parameters", [])),
            len(protocol_data.get("test_cases", [])),
            info.get("feature", ""),
        ))

        # Requirement map
        for req_id in info.get("related_requirements", []):
            req_id = req_id.strip()
            if req_id:
                c.execute(
                    "INSERT OR IGNORE INTO protocol_requirement_map VALUES (?, ?)",
                    (pid, req_id)
                )

        # Risk map
        for risk_id in info.get("related_risks", []):
            risk_id = risk_id.strip()
            if risk_id:
                c.execute(
                    "INSERT OR IGNORE INTO protocol_risk_map VALUES (?, ?)",
                    (pid, risk_id)
                )

        # Screen map (store names, not IDs)
        for screen in info.get("related_screens", []):
            screen = screen.strip()
            if screen:
                c.execute(
                    "INSERT OR IGNORE INTO protocol_screen_map VALUES (?, ?)",
                    (pid, screen)
                )

        conn.commit()
        conn.close()

    except Exception:
        pass  # Never let registry failure break protocol generation


# ============================================================
# QUERY
# ============================================================

def find_protocols_by_requirement(req_id: str) -> list:
    """
    Returns all protocols that cover a given requirement ID.
    Returns [] if table doesn't exist or no results.
    """
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT p.protocol_id, p.protocol_name, p.feature, p.tc_count
            FROM generated_protocols p
            JOIN protocol_requirement_map m ON p.protocol_id = m.protocol_id
            WHERE m.requirement_id = ?
            ORDER BY p.created_at DESC
        """, (req_id,)).fetchall()
        conn.close()
        return [
            {"id": r[0], "name": r[1], "feature": r[2], "tc_count": r[3]}
            for r in rows
        ]
    except Exception:
        return []


def find_protocols_by_feature(keyword: str) -> list:
    """
    Returns protocols whose feature or name contains the keyword.
    Case-insensitive.
    """
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT protocol_id, protocol_name, feature, tc_count
            FROM generated_protocols
            WHERE LOWER(feature) LIKE ?
               OR LOWER(protocol_name) LIKE ?
               OR LOWER(source_input) LIKE ?
            ORDER BY created_at DESC
        """, (
            f"%{keyword.lower()}%",
            f"%{keyword.lower()}%",
            f"%{keyword.lower()}%",
        )).fetchall()
        conn.close()
        return [
            {"id": r[0], "name": r[1], "feature": r[2], "tc_count": r[3]}
            for r in rows
        ]
    except Exception:
        return []


def format_protocol_impact_for_prompt(keyword: str, req_ids: list) -> str:
    """
    Build a protocol impact context block for the Gemini prompt.
    Returns only protocols that actually exist in the registry.
    If registry is empty, returns an instruction NOT to invent protocol names.

    Args:
        keyword:  The detected feature keyword (e.g. "HPI", "Smart Wedge")
        req_ids:  List of affected requirement IDs

    Returns:
        A formatted string ready to paste into a prompt section.
    """
    found = {}

    # Search by requirement
    for req_id in req_ids:
        for p in find_protocols_by_requirement(req_id):
            found[p["id"]] = p

    # Search by feature keyword
    for p in find_protocols_by_feature(keyword):
        found[p["id"]] = p

    if not found:
        return (
            "No protocols have been generated for this feature yet in the ALTA platform.\n"
            "DO NOT invent protocol IDs or names such as ALG-VER-PROT-008.\n"
            "Instead, describe the TYPES of protocols that would be needed:\n"
            "  - Example: A boundary validation protocol for HPI thresholds\n"
            "  - Example: An alarm validation protocol for HPI alarm triggers\n"
            "Use the format: 'Protocol Required: [description]' — never invent an ID."
        )

    lines = ["Existing generated protocols covering this feature (use these names only):"]
    for p in found.values():
        lines.append(
            f"  {p['id']} — {p['name']}"
            f"  (Feature: {p['feature']}, Test Cases: {p['tc_count']})"
        )

    return "\n".join(lines)