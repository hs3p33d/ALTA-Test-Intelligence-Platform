"""
tc_registry_service.py

Stores every generated test case in SQLite and provides query functions
used by impact_analysis_service to identify which test cases need
re-execution after a change.

Enables the full traceability chain:
    Requirement → Scenario → Protocol → Test Case

Called by:
    protocol_service.py         — register_test_cases() after JSON parsing
    impact_analysis_service.py  — format_tc_impact_for_prompt()
"""

import sqlite3

DB = "alta_poc.db"

# Priority display order
PRIORITY_ORDER = ["Critical", "High", "Medium", "Low"]


# ============================================================
# REGISTER
# ============================================================

def register_test_cases(protocol_data: dict):
    """
    Store all test cases from a generated protocol in the registry.

    Args:
        protocol_data: The parsed JSON dict from protocol_service.
                       Must contain "protocol_info" and "test_cases".

    Safe to call even if tables don't exist — fails silently.
    """
    try:
        info        = protocol_data.get("protocol_info", {})
        protocol_id = info.get("protocol_id", "").strip()
        feature     = info.get("feature", "").strip()

        conn = sqlite3.connect(DB)
        c    = conn.cursor()

        for tc in protocol_data.get("test_cases", []):
            tc_id = tc.get("tc_id", "").strip()
            if not tc_id:
                continue

            steps          = tc.get("steps", [])
            verifications  = [s for s in steps if s.get("step_type") == "Verification"]

            c.execute("""
                INSERT OR REPLACE INTO generated_test_cases
                (tc_id, protocol_id, feature, title, priority,
                 scenario_type, related_requirements, related_risks,
                 step_count, verification_count)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                tc_id,
                protocol_id,
                feature,
                tc.get("title", ""),
                tc.get("priority", ""),
                tc.get("scenario_type", ""),
                ", ".join(tc.get("related_requirements", [])),
                ", ".join(tc.get("related_risks", [])),
                len(steps),
                len(verifications),
            ))

            for req_id in tc.get("related_requirements", []):
                req_id = req_id.strip()
                if req_id:
                    c.execute(
                        "INSERT OR IGNORE INTO tc_requirement_map VALUES (?, ?)",
                        (tc_id, req_id)
                    )

            for risk_id in tc.get("related_risks", []):
                risk_id = risk_id.strip()
                if risk_id:
                    c.execute(
                        "INSERT OR IGNORE INTO tc_risk_map VALUES (?, ?)",
                        (tc_id, risk_id)
                    )

        conn.commit()
        conn.close()

    except Exception:
        pass  # Never let registry failure break protocol generation


# ============================================================
# QUERY
# ============================================================

def find_test_cases_by_requirement(req_id: str) -> list:
    """Returns all test cases that cover a given requirement ID."""
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT t.tc_id, t.feature, t.title, t.priority,
                   t.scenario_type, t.protocol_id, t.verification_count
            FROM generated_test_cases t
            JOIN tc_requirement_map m ON t.tc_id = m.tc_id
            WHERE m.requirement_id = ?
            ORDER BY
                CASE t.priority
                    WHEN 'Critical' THEN 1
                    WHEN 'High'     THEN 2
                    WHEN 'Medium'   THEN 3
                    WHEN 'Low'      THEN 4
                    ELSE 5
                END
        """, (req_id,)).fetchall()
        conn.close()
        return [
            {
                "tc_id":              r[0],
                "feature":            r[1],
                "title":              r[2],
                "priority":           r[3],
                "type":               r[4],
                "protocol_id":        r[5],
                "verification_count": r[6],
            }
            for r in rows
        ]
    except Exception:
        return []


def find_test_cases_by_feature(keyword: str) -> list:
    """Returns all test cases generated for a feature keyword."""
    try:
        conn = sqlite3.connect(DB)
        rows = conn.execute("""
            SELECT tc_id, feature, title, priority, scenario_type,
                   protocol_id, verification_count
            FROM generated_test_cases
            WHERE LOWER(feature) LIKE ?
            ORDER BY
                CASE priority
                    WHEN 'Critical' THEN 1
                    WHEN 'High'     THEN 2
                    WHEN 'Medium'   THEN 3
                    WHEN 'Low'      THEN 4
                    ELSE 5
                END
        """, (f"%{keyword.lower()}%",)).fetchall()
        conn.close()
        return [
            {
                "tc_id":              r[0],
                "feature":            r[1],
                "title":              r[2],
                "priority":           r[3],
                "type":               r[4],
                "protocol_id":        r[5],
                "verification_count": r[6],
            }
            for r in rows
        ]
    except Exception:
        return []


def format_tc_impact_for_prompt(keyword: str, req_ids: list) -> str:
    """
    Build the test case impact section for the Gemini prompt.
    Groups test cases by priority (Critical → High → Medium → Low).

    Args:
        keyword:  Detected feature keyword
        req_ids:  List of affected requirement IDs

    Returns:
        Formatted string for prompt injection.
    """
    found = {}

    for req_id in req_ids:
        for tc in find_test_cases_by_requirement(req_id):
            found[tc["tc_id"]] = tc

    for tc in find_test_cases_by_feature(keyword):
        found[tc["tc_id"]] = tc

    if not found:
        return (
            "No test cases have been generated for this feature yet. "
            "Recommend generating a protocol via the Protocol Generator "
            "before performing impact analysis for full test case traceability."
        )

    # Group by priority
    by_priority = {p: [] for p in PRIORITY_ORDER}
    for tc in found.values():
        p = tc.get("priority", "Medium")
        bucket = by_priority.get(p, by_priority["Medium"])
        bucket.append(tc)

    total = len(found)
    lines = [f"Existing test cases requiring re-evaluation ({total} total):"]

    for priority in PRIORITY_ORDER:
        tcs = by_priority.get(priority, [])
        if tcs:
            lines.append(f"\n  {priority} Priority Re-Execution:")
            for tc in tcs:
                title_preview = (tc["title"] or "")[:80]
                proto_ref = f"  [Protocol: {tc['protocol_id']}]" if tc["protocol_id"] else ""
                lines.append(
                    f"    {tc['tc_id']} — {title_preview}{proto_ref}"
                )

    return "\n".join(lines)