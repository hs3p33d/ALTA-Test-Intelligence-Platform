"""
scenario_service.py  — UPDATED

Changes from original:
  - After generating scenarios, parses and registers them in SQLite
  - This feeds impact_analysis_service with real scenario data
  - Zero extra API calls — registration is pure Python

API calls: still 1 (unchanged).
"""

from services.search_service import build_context
from services.search_service import search_requirements
from services.gemini_service import ask_gemini
from services.screen_service import get_screen_by_id
from services.risk_service import get_risk_by_id

import re


# ==========================================
# INPUT DETECTION
# ==========================================

def detect_input_type(user_input):

    user_input = user_input.strip()

    if re.match(r"^[A-Z]+-\d+$", user_input):
        return "requirement"

    if len(user_input.split()) <= 3:
        return "feature"

    return "change"


# ==========================================
# TRACEABILITY SUMMARY
# ==========================================

def build_traceability_summary(user_input):

    rows = search_requirements(
        user_input,
        limit=5
    )

    requirements = []
    screens = set()
    parameters = set()
    risks = set()

    for row in rows:

        requirements.append(
            f"{row[0]} - {row[1]}"
        )

        # Screens
        if len(row) > 5 and row[5]:
            for screen_id in row[5].split(","):
                screen_id = screen_id.strip()
                if not screen_id:
                    continue
                screen = get_screen_by_id(screen_id)
                if screen:
                    screens.add(f"{screen['id']} - {screen['name']}")
                else:
                    screens.add(screen_id)

        # Parameters
        if len(row) > 6 and row[6]:
            parameters.update(
                [x.strip() for x in row[6].split(",") if x.strip()]
            )

        # Risks
        if len(row) > 7 and row[7]:
            for risk_id in row[7].split(","):
                risk_id = risk_id.strip()
                if not risk_id:
                    continue
                risk = get_risk_by_id(risk_id)
                if risk:
                    risks.add(f"{risk['id']} - {risk['title']}")
                else:
                    risks.add(risk_id)

    return {
        "requirements": sorted(requirements),
        "screens":      sorted(list(screens)),
        "parameters":   sorted(list(parameters)),
        "risks":        sorted(list(risks))
    }


# ==========================================
# CONTEXT BUILDER
# ==========================================

def build_scenario_context(user_input):

    input_type = detect_input_type(user_input)
    context    = build_context(user_input, limit=5)
    traceability = build_traceability_summary(user_input)

    return (input_type, context, traceability)


# ==========================================
# SCENARIO PARSER
# Extracts structured dicts from Gemini markdown output.
# Used both locally (for registration) and by protocol_service.
# ==========================================

SCENARIO_TYPE_MAP = {
    "Positive Scenarios":       "Positive",
    "Negative Scenarios":       "Negative",
    "Boundary Scenarios":       "Boundary",
    "Error Handling Scenarios": "Error Handling",
    "Alarm Scenarios":          "Alarm",
    "Workflow Scenarios":       "Workflow",
    "Regression Scenarios":     "Regression",
}


def parse_scenarios(scenario_text):
    """
    Parse the markdown output from generate_scenarios() into a list of dicts.

    Each dict:
        {
            "id":           "PS-001",
            "type":         "Positive",
            "priority":     "High",
            "scenario":     "Verify that...",
            "requirements": ["ANA-001"],
            "risks":        ["RSK-003"],
        }
    """
    scenarios    = []
    current_type = None

    lines = scenario_text.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Detect section header
        for section_name, stype in SCENARIO_TYPE_MAP.items():
            if re.match(rf"^#+\s*{re.escape(section_name)}", line, re.IGNORECASE):
                current_type = stype
                break

        # Detect scenario ID line  e.g. "PS-001" or "**PS-001**"
        id_match = re.match(r"^\*{0,2}([A-Z]{2}-\d{3})\*{0,2}$", line)
        if id_match and current_type:
            scenario_id = id_match.group(1)
            block = {
                "id":           scenario_id,
                "type":         current_type,
                "priority":     "High",
                "scenario":     "",
                "requirements": [],
                "risks":        [],
            }

            i += 1
            while i < len(lines):
                l = lines[i].strip()

                # Stop at next scenario ID or section
                if re.match(r"^\*{0,2}[A-Z]{2}-\d{3}\*{0,2}$", l):
                    break
                if re.match(r"^#+\s", l):
                    break

                # Priority
                if re.match(r"^priority\s*:", l, re.IGNORECASE):
                    val = re.sub(r"^priority\s*:\s*", "", l, flags=re.IGNORECASE).strip()
                    if val:
                        block["priority"] = val
                    elif i + 1 < len(lines):
                        i += 1
                        block["priority"] = lines[i].strip()

                # Scenario text
                elif re.match(r"^scenario\s*:", l, re.IGNORECASE):
                    val = re.sub(r"^scenario\s*:\s*", "", l, flags=re.IGNORECASE).strip()
                    parts = [val] if val else []
                    i += 1
                    while i < len(lines):
                        nl = lines[i].strip()
                        if re.match(r"^(priority|scenario|related requirements|related risks)\s*:", nl, re.IGNORECASE):
                            break
                        if re.match(r"^\*{0,2}[A-Z]{2}-\d{3}\*{0,2}$", nl):
                            break
                        if re.match(r"^#+\s", nl):
                            break
                        if nl:
                            parts.append(nl)
                        i += 1
                    block["scenario"] = " ".join(parts)
                    continue

                # Related Requirements
                elif re.match(r"^related requirements\s*:", l, re.IGNORECASE):
                    val = re.sub(r"^related requirements\s*:\s*", "", l, flags=re.IGNORECASE).strip()
                    reqs = [r.strip() for r in re.split(r"[,\s]+", val) if re.match(r"[A-Z]+-\d+", r.strip())]
                    i += 1
                    while i < len(lines):
                        nl = lines[i].strip()
                        if re.match(r"^(priority|scenario|related requirements|related risks)\s*:", nl, re.IGNORECASE):
                            break
                        if re.match(r"^\*{0,2}[A-Z]{2}-\d{3}\*{0,2}$", nl):
                            break
                        if re.match(r"^#+\s", nl):
                            break
                        more = [r.strip(" -•*") for r in re.split(r"[,\s]+", nl)
                                if re.match(r"[A-Z]+-\d+", r.strip(" -•*"))]
                        reqs.extend(more)
                        i += 1
                    block["requirements"] = list(dict.fromkeys(reqs))
                    continue

                # Related Risks
                elif re.match(r"^related risks\s*:", l, re.IGNORECASE):
                    val = re.sub(r"^related risks\s*:\s*", "", l, flags=re.IGNORECASE).strip()
                    risks = [r.strip() for r in re.split(r"[,\s]+", val) if re.match(r"[A-Z]+-\d+", r.strip())]
                    i += 1
                    while i < len(lines):
                        nl = lines[i].strip()
                        if re.match(r"^(priority|scenario|related requirements|related risks)\s*:", nl, re.IGNORECASE):
                            break
                        if re.match(r"^\*{0,2}[A-Z]{2}-\d{3}\*{0,2}$", nl):
                            break
                        if re.match(r"^#+\s", nl):
                            break
                        more = [r.strip(" -•*") for r in re.split(r"[,\s]+", nl)
                                if re.match(r"[A-Z]+-\d+", r.strip(" -•*"))]
                        risks.extend(more)
                        i += 1
                    block["risks"] = list(dict.fromkeys(risks))
                    continue

                i += 1

            scenarios.append(block)
            continue

        i += 1

    return scenarios


# ==========================================
# GENERATE SCENARIOS
# ==========================================

def generate_scenarios(user_input):

    (input_type, context, traceability) = build_scenario_context(user_input)

    prompt = f"""
You are a Senior Medical Device QA Engineer
working on BD HemoSphere ALTA.

Generate realistic and practical test scenarios.

================================================

INPUT TYPE

{input_type}

================================================

USER INPUT

{user_input}

================================================

ALTA CONTEXT

{context}

================================================

RELATED REQUIREMENTS

{chr(10).join(traceability["requirements"])}

================================================

RELATED SCREENS

{chr(10).join(traceability["screens"])}

================================================

RELATED PARAMETERS

{chr(10).join(traceability["parameters"])}

================================================

RELATED RISKS

{chr(10).join(traceability["risks"])}

================================================

RULES

1. Generate realistic QA scenarios.

2. Avoid duplicates.

3. Keep scenarios concise.

4. Use ALTA terminology.

5. Generate:

5 Positive

5 Negative

5 Boundary

3 Error Handling

3 Alarm

3 Workflow

3 Regression

6. Every scenario must include:

Scenario ID

Priority

Scenario

Related Requirements

Related Risks

7. Priorities must be:

Critical
High
Medium
Low

8. Assign realistic priorities.

9. Use markdown.

================================================

OUTPUT FORMAT

# Feature Summary

Short business summary.

# Recommended Testing Techniques
Provide maximum 5 testing techniques.
Only the most relevant techniques.
- Technique

# Related Requirements

List all.

# Related Screens

List all.

# Related Parameters

List all.

# Related Risks

List all.

# Positive Scenarios

PS-001

Priority:
High

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Negative Scenarios

NS-001

Priority:
High

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Boundary Scenarios

BS-001

Priority:
Medium

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Error Handling Scenarios

ES-001

Priority:
High

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Alarm Scenarios

AS-001

Priority:
Critical

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Workflow Scenarios

WS-001

Priority:
Medium

Scenario:
...

Related Requirements:
...

Related Risks:
...

# Regression Scenarios

RS-001

Priority:
High

Scenario:
...

Related Requirements:
...

Related Risks:
...

Generate only final output.
No explanations.
"""

    result = ask_gemini(prompt)

    # ── Register scenarios in SQLite (no API call) ────────
    try:
        parsed = parse_scenarios(result)
        if parsed:
            from services.scenario_registry_service import register_scenarios
            register_scenarios(parsed, user_input)
    except Exception:
        pass  # Never block scenario generation

    return result


# ==========================================
# RESOLVE HELPERS
# ==========================================

def resolve_screen(screen_id):
    try:
        screen = get_screen_by_id(screen_id)
        if screen:
            return f"{screen_id} - {screen['name']}"
    except Exception:
        pass
    return screen_id


def resolve_risk(risk_id):
    try:
        risk = get_risk_by_id(risk_id)
        if risk:
            return f"{risk_id} - {risk['title']}"
    except Exception:
        pass
    return risk_id


# ==========================================
# LOCAL TEST
# ==========================================

if __name__ == "__main__":
    result = generate_scenarios("HPI")
    print(result)