"""
scenario_registry_service.py

Stores every generated scenario in SQLite and provides query functions
used by impact_analysis_service to identify which scenarios are affected
by a change — without any Gemini call.

Called by:
    scenario_service.py         — register_scenarios() after generation
    impact_analysis_service.py  — format_scenario_impact_for_prompt()
"""

import re
import sqlite3

DB = "alta_poc.db"


# ============================================================
# REGISTER
# ============================================================

def register_scenarios(scenarios: list, feature: str, protocol_id: str = ""):
    """
    Store a list of parsed scenario dicts in the registry.

    Args:
        scenarios:    List of dicts from protocol_service.parse_scenarios()
                      Each dict must have: id, type, priority, scenario, requirements, risks
        feature:      The feature keyword this scenario was generated for (e.g. "HPI")
        protocol_id:  Optional — parent protocol ID if generated as part of a protocol run.

    Safe to call even if tables don't exist — fails silently.
    """
    try:
        conn = sqlite3.connect(DB)
        c    = conn.cursor()

        for s in scenarios:
            # Build a stable unique ID: FEATURE-TYPE-ID  e.g. HPI-PS-001
            raw_id  = s.get("id", "")
            sid     = f"{feature.upper().replace(' ', '_')}-{raw_id}"

            c.execute("""
                INSERT OR REPLACE INTO generated_scenarios
                (scenario_id, protocol_id, feature, scenario_type,
                 priority, scenario_text, related_requirements, related_risks)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                sid,
                protocol_id,
                feature,
                s.get("type", ""),
                s.get("priority", ""),
                s.get("scenario", ""),
                ", ".join(s.get("requirements", [])),
                ", ".join(s.get("risks", [])),
            ))

            for req_id in s.get("requirements", []):
                req_id = req_id.strip()
                if req_id:
                    c.execute(
                        "INSERT OR IGNORE INTO scenario_requirement_map VALUES (?, ?)",
                        (sid, req_id)
                    )

        conn.commit()
        conn.close()

    except Exception:
        pass  # Never block scenario generation


# ============================================================
# QUERY
# ============================================================

def find_scenarios_by_requirement(req_id: str) -> list:
    """Returns all scenarios that reference a given requirement ID."""
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT s.scenario_id, s.feature, s.scenario_type,
                   s.priority, s.scenario_text
            FROM generated_scenarios s
            JOIN scenario_requirement_map m ON s.scenario_id = m.scenario_id
            WHERE m.requirement_id = ?
            ORDER BY s.scenario_type, s.priority
        """, (req_id,)).fetchall()
        conn.close()
        return [
            {
                "id":       r[0],
                "feature":  r[1],
                "type":     r[2],
                "priority": r[3],
                "text":     r[4],
            }
            for r in rows
        ]
    except Exception:
        return []


def find_scenarios_by_feature(keyword: str) -> list:
    """Returns all scenarios generated for a given feature keyword."""
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT scenario_id, feature, scenario_type, priority, scenario_text
            FROM generated_scenarios
            WHERE LOWER(feature) LIKE ?
            ORDER BY scenario_type, priority
        """, (f"%{keyword.lower()}%",)).fetchall()
        conn.close()
        return [
            {
                "id":       r[0],
                "feature":  r[1],
                "type":     r[2],
                "priority": r[3],
                "text":     r[4],
            }
            for r in rows
        ]
    except Exception:
        return []


def format_scenario_impact_for_prompt(keyword: str, req_ids: list) -> str:
    """
    Build the scenario impact section for injection into the Gemini prompt.
    Groups scenarios by type for readability.

    Args:
        keyword:  Detected feature keyword
        req_ids:  List of affected requirement IDs

    Returns:
        Formatted string for prompt injection.
    """
    found = {}

    for req_id in req_ids:
        for s in find_scenarios_by_requirement(req_id):
            found[s["id"]] = s

    for s in find_scenarios_by_feature(keyword):
        found[s["id"]] = s

    if not found:
        return (
            "No scenarios have been generated for this feature yet. "
            "Recommend generating scenarios via the Scenario Generator "
            "before performing impact analysis for maximum traceability."
        )

    # Group by scenario type
    grouped = {}
    for s in found.values():
        stype = s.get("type", "Other")
        grouped.setdefault(stype, []).append(s)

    lines = [f"Existing scenarios affected by this change ({len(found)} total):"]
    type_order = [
        "Positive", "Negative", "Boundary",
        "Alarm", "Workflow", "Error Handling", "Regression"
    ]
    for stype in type_order:
        scenarios = grouped.get(stype, [])
        if scenarios:
            lines.append(f"\n  {stype} Scenarios:")
            for s in scenarios:
                text_preview = (s["text"] or "")[:90]
                lines.append(
                    f"    {s['id']} [{s['priority']}]: {text_preview}"
                )

    return "\n".join(lines)