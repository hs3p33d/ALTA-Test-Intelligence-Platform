"""
enrichment_service.py  — FIXED for actual master_data field names

Tested against:
    master_data/screens.md  — uses "Screen Name:", "Purpose:", "Category:", "Related Parameters:"
    master_data/risks.md    — uses "Risk Name:", "Description:", "Severity:", "Mitigation Areas:"
    master_data/parameters.md — uses "Parameter Name:", "Full Name:", "Unit:", "Clinical Purpose:"

Field name fixes from original:
    screens.md:  "Description:" → "Purpose:"
    risks.md:    "Risk Title:"  → "Risk Name:"
                 "Mitigation:"  → "Mitigation Areas:" (first bullet only)
"""

import re
from pathlib import Path
from functools import lru_cache

BASE = Path(__file__).resolve().parent.parent / "master_data"


# ============================================================
# SCREEN ENRICHMENT
# ============================================================

@lru_cache(maxsize=1)
def _load_screens():
    """
    Parse screens.md into a dict keyed by Screen ID.

    Actual fields in screens.md:
        Screen ID:         SCR-001
        Screen Name:       Main Monitoring Screen      (may be on next line)
        Category:          Monitoring
        Purpose:           Primary real-time patient monitoring...
        Related Parameters:• MAP \n• CO \n...
    """
    screens = {}
    try:
        text = (BASE / "screens.md").read_text(encoding="utf-8")
        blocks = re.split(r"(?=Screen ID:)", text, flags=re.IGNORECASE)

        for block in blocks:
            id_m   = re.search(r"Screen ID:\s*(\S+)",    block, re.IGNORECASE)
            name_m = re.search(r"Screen Name:\s*\n?(.+)", block, re.IGNORECASE)
            cat_m  = re.search(r"Category:\s*\n?(.+)",   block, re.IGNORECASE)
            purp_m = re.search(r"Purpose:\s*\n?(.+)",    block, re.IGNORECASE)

            # Related Parameters — collect bullet list items
            params = []
            param_section = re.search(
                r"Related Parameters:(.*?)(?=\nNavigation Sources:|\nRelated Features:|\nImpact Keywords:|$)",
                block, re.DOTALL | re.IGNORECASE
            )
            if param_section:
                for line in param_section.group(1).splitlines():
                    p = line.replace("•", "").strip()
                    if p:
                        params.append(p)

            if id_m and name_m:
                sid = id_m.group(1).strip()
                screens[sid] = {
                    "id":          sid,
                    "name":        name_m.group(1).strip(),
                    "category":    cat_m.group(1).strip()  if cat_m  else "",
                    "description": purp_m.group(1).strip() if purp_m else "",  # Purpose as description
                    "parameters":  params,
                }
    except FileNotFoundError:
        pass
    except Exception:
        pass
    return screens


def get_screen(screen_id: str) -> dict:
    screens = _load_screens()
    return screens.get(screen_id.strip(), {
        "id":          screen_id,
        "name":        screen_id,
        "category":    "",
        "description": "",
        "parameters":  [],
    })


def enrich_screen_ids(raw: str) -> list:
    """Extract all SCR-XXX IDs from any string and return enriched dicts."""
    ids = re.findall(r"SCR-\d+", str(raw))
    seen = set()
    result = []
    for sid in ids:
        if sid not in seen:
            seen.add(sid)
            result.append(get_screen(sid))
    return result


def format_screens_for_prompt(raw: str) -> str:
    """
    Formatted screen block for Gemini prompt injection.

    Example output:
        SCR-001 — Main Monitoring Screen  [Category: Monitoring]
          Purpose: Primary real-time patient monitoring display.
          Parameters: MAP, CO, CI, HPI, GHI
        SCR-007 — HPI Secondary Screen  [Category: Clinical Tools]
          Purpose: Deep dive analytical environment for HPI behaviors.
    """
    enriched = enrich_screen_ids(raw)
    if not enriched:
        cleaned = raw.strip()
        return cleaned if cleaned else "None identified."

    lines = []
    for s in enriched:
        header = f"{s['id']} — {s['name']}"
        if s["category"]:
            header += f"  [Category: {s['category']}]"
        lines.append(header)
        if s["description"]:
            lines.append(f"  Purpose: {s['description']}")
        if s["parameters"]:
            lines.append(f"  Parameters: {', '.join(s['parameters'])}")
    return "\n".join(lines)


def screen_names_only(raw: str) -> list:
    """Returns list of screen NAMES for use in protocol prompts."""
    enriched = enrich_screen_ids(raw)
    if not enriched:
        return [s.strip() for s in re.split(r"[,\n]", raw) if s.strip()]
    return [s["name"] for s in enriched]


# ============================================================
# RISK ENRICHMENT
# ============================================================

@lru_cache(maxsize=1)
def _load_risks():
    """
    Parse risks.md into a dict keyed by Risk ID.

    Actual fields in risks.md:
        Risk ID:           RSK-001
        Risk Name:         Patient Misidentification...   (NOT "Risk Title:")
        Category:          Clinical Workflow
        Severity:          Critical
        Description:       Patient physiological tracking streams...
        Potential Impact:  Incorrect clinical treatment...
        Mitigation Areas:  • Patient Demographics Verification   (NOT "Mitigation:")
    """
    risks = {}
    try:
        text = (BASE / "risks.md").read_text(encoding="utf-8")
        blocks = re.split(r"(?=Risk ID:)", text, flags=re.IGNORECASE)

        for block in blocks:
            id_m     = re.search(r"Risk ID:\s*(\S+)",       block, re.IGNORECASE)
            name_m   = re.search(r"Risk Name:\s*\n?(.+)",   block, re.IGNORECASE)  # FIXED: was "Risk Title:"
            cat_m    = re.search(r"Category:\s*\n?(.+)",    block, re.IGNORECASE)
            sev_m    = re.search(r"Severity:\s*\n?(.+)",    block, re.IGNORECASE)
            desc_m   = re.search(r"Description:\s*\n?(.+)", block, re.IGNORECASE)
            impact_m = re.search(r"Potential Impact:\s*\n?(.+)", block, re.IGNORECASE)

            # Mitigation Areas — collect bullet list items  (FIXED: was "Mitigation:")
            mitigations = []
            mit_section = re.search(
                r"Mitigation Areas:(.*?)(?=\nImpact Keywords:|\nRelated Features:|$)",
                block, re.DOTALL | re.IGNORECASE
            )
            if mit_section:
                for line in mit_section.group(1).splitlines():
                    m = line.replace("•", "").strip()
                    if m:
                        mitigations.append(m)

            if id_m:
                rid = id_m.group(1).strip()
                risks[rid] = {
                    "id":          rid,
                    "title":       name_m.group(1).strip()   if name_m   else rid,
                    "category":    cat_m.group(1).strip()    if cat_m    else "",
                    "severity":    sev_m.group(1).strip()    if sev_m    else "Unknown",
                    "description": desc_m.group(1).strip()   if desc_m   else "",
                    "impact":      impact_m.group(1).strip() if impact_m else "",
                    "mitigation":  "; ".join(mitigations),
                }
    except FileNotFoundError:
        pass
    except Exception:
        pass
    return risks


def get_risk(risk_id: str) -> dict:
    risks = _load_risks()
    return risks.get(risk_id.strip(), {
        "id":          risk_id,
        "title":       risk_id,
        "category":    "",
        "severity":    "Unknown",
        "description": "",
        "impact":      "",
        "mitigation":  "",
    })


def enrich_risk_ids(raw: str) -> list:
    """Extract all RSK-XXX IDs from any string and return enriched dicts."""
    ids = re.findall(r"RSK-\d+", str(raw))
    seen = set()
    result = []
    for rid in ids:
        if rid not in seen:
            seen.add(rid)
            result.append(get_risk(rid))
    return result


def format_risks_for_prompt(raw: str) -> str:
    """
    Formatted risk block for Gemini prompt injection.

    Example output:
        RSK-003 — HPI Algorithmic False Negative Error  [Severity: Critical | Category: Analytics Risks]
          Description: The HPI algorithm may fail to identify waveform anomalies...
          Potential Impact: Delayed clinical response to occult systemic hypoperfusion.
          Mitigations: Independent Primary Metric Cross-Checking (MAP); Multi-Parametric Safety Bound Interlocking
    """
    enriched = enrich_risk_ids(raw)
    if not enriched:
        cleaned = raw.strip()
        return cleaned if cleaned else "None identified."

    lines = []
    for r in enriched:
        header = f"{r['id']} — {r['title']}"
        header += f"  [Severity: {r['severity']}"
        if r["category"]:
            header += f" | Category: {r['category']}"
        header += "]"
        lines.append(header)
        if r["description"]:
            lines.append(f"  Description: {r['description']}")
        if r["impact"]:
            lines.append(f"  Potential Impact: {r['impact']}")
        if r["mitigation"]:
            lines.append(f"  Mitigations: {r['mitigation']}")
    return "\n".join(lines)


def get_risk_severity(risk_id: str) -> str:
    """Returns severity string for a single risk ID. Used by scoring engine."""
    return get_risk(risk_id).get("severity", "Unknown")


# ============================================================
# PARAMETER ENRICHMENT (bonus — from parameters.md)
# ============================================================

@lru_cache(maxsize=1)
def _load_parameters():
    """
    Parse parameters.md into a dict keyed by Parameter Name (e.g. "MAP").

    Actual fields:
        Parameter ID:      PAR-001
        Parameter Name:    MAP
        Full Name:         Mean Arterial Pressure
        Category:          Hemodynamic - Pressure
        Unit:              mmHg
        Clinical Purpose:  Represents the average perfusion pressure...
    """
    params = {}
    try:
        text = (BASE / "parameters.md").read_text(encoding="utf-8")
        blocks = re.split(r"(?=Parameter ID:)", text, flags=re.IGNORECASE)

        for block in blocks:
            id_m      = re.search(r"Parameter ID:\s*(\S+)",        block, re.IGNORECASE)
            name_m    = re.search(r"Parameter Name:\s*\n?(.+)",    block, re.IGNORECASE)
            full_m    = re.search(r"Full Name:\s*\n?(.+)",         block, re.IGNORECASE)
            cat_m     = re.search(r"Category:\s*\n?(.+)",          block, re.IGNORECASE)
            unit_m    = re.search(r"Unit:\s*\n?(.+)",              block, re.IGNORECASE)
            purpose_m = re.search(r"Clinical Purpose:\s*\n?(.+)",  block, re.IGNORECASE)

            if id_m and name_m:
                pname = name_m.group(1).strip()
                params[pname] = {
                    "id":       id_m.group(1).strip(),
                    "name":     pname,
                    "fullname": full_m.group(1).strip()    if full_m    else pname,
                    "category": cat_m.group(1).strip()     if cat_m     else "",
                    "unit":     unit_m.group(1).strip()    if unit_m    else "",
                    "purpose":  purpose_m.group(1).strip() if purpose_m else "",
                }
    except FileNotFoundError:
        pass
    except Exception:
        pass
    return params


def get_parameter(param_name: str) -> dict:
    params = _load_parameters()
    return params.get(param_name.strip(), {
        "id":       "",
        "name":     param_name,
        "fullname": param_name,
        "category": "",
        "unit":     "",
        "purpose":  "",
    })