"""
protocol_service.py  — UPDATED (2-call architecture + registry integration)

Changes from previous version:
  - After successful JSON parse, registers protocol + test cases in SQLite
  - This feeds impact_analysis_service with real protocol and TC data
  - Zero extra API calls

Total Gemini API calls: 2 per protocol generation (unchanged).
"""

import re
import json
from services.scenario_service import generate_scenarios, build_traceability_summary
from services.gemini_service import ask_gemini


# ============================================================
# SCREEN ID STRIPPER
# ============================================================

def _strip_screen_ids(text):
    """Remove any SCR-XXX identifiers that Gemini leaks despite rules."""
    return re.sub(r'\s*\(SCR-\d+\)', '', text)


# ============================================================
# JSON CLEANER
# ============================================================

def _clean_json(raw):
    raw = raw.strip()
    raw = re.sub(r'^```json\s*', '', raw)
    raw = re.sub(r'^```\s*', '', raw)
    raw = re.sub(r'```\s*$', '', raw)
    return raw.strip()


# ============================================================
# MAIN ENTRY POINT — 2 API calls total
# ============================================================

def generate_protocol(user_input):
    """
    Generate a complete validation protocol.
    Returns structured markdown text for display and Excel export.

    API calls:
        Call 1 — generate_scenarios()
        Call 2 — Gemini JSON protocol generation
        All other processing is pure Python.
    """

    # ── Call 1: Generate scenarios ────────────────────────
    scenario_output = generate_scenarios(user_input)

    # ── Build traceability context (DB only, no API call) ─
    traceability = build_traceability_summary(user_input)

    screens_list = "\n".join(traceability["screens"])    or "Not identified"
    params_list  = "\n".join(traceability["parameters"]) or "Not identified"
    risks_list   = "\n".join(traceability["risks"])      or "Not identified"
    req_list     = "\n".join(traceability["requirements"]) or "Not identified"

    # ── Call 2: Generate full protocol as JSON ─────────────
    prompt = f"""
You are a Principal Medical Device Verification Engineer.
Generate a complete formal validation protocol for the BD HemoSphere ALTA platform.

====================================================
INPUTS
====================================================

Feature: {user_input}

RELATED REQUIREMENTS (resolved from database — use these exactly):
{req_list}

RELATED SCREENS (use NAMES only — strip any SCR-XXX IDs):
{screens_list}

RELATED PARAMETERS:
{params_list}

RELATED RISKS:
{risks_list}

SCENARIO PACKAGE (source of truth for all test cases):
{scenario_output}

====================================================
OUTPUT INSTRUCTIONS
====================================================

Respond with ONLY a single valid JSON object.
No preamble. No explanation. No markdown fences.
No text before or after the JSON.

The JSON must follow this EXACT schema:

{{
  "protocol_info": {{
    "protocol_id": "ALTA-PROTO-XXXXXX",
    "protocol_name": "string",
    "feature": "string",
    "objective": "string",
    "related_requirements": ["REQ-001", "REQ-002"],
    "related_risks": ["RSK-001"],
    "related_screens": ["Screen Name Only — no SCR-XXX"],
    "related_parameters": ["PARAM1", "PARAM2"],
    "preconditions": ["string", "string"],
    "test_environment": {{
      "ALTA Monitor": "string",
      "CTA Simulator": "string",
      "Acumen IQ Sensor": "string",
      "Software Version": "TBD — specify at execution",
      "Test Operator": "Qualified QA Engineer"
    }}
  }},

  "test_cases": [
    {{
      "execution_order": 1,
      "tc_id": "TC-PS-001",
      "title": "Descriptive title — never write Test Case for TC-XXX",
      "priority": "Critical|High|Medium|Low",
      "scenario_type": "Positive|Negative|Boundary|Alarm|Workflow|Error Handling|Regression",
      "related_requirements": ["REQ-001"],
      "related_risks": ["RSK-001"],
      "steps": [
        {{
          "step_id": "1.0",
          "step_type": "Test Case",
          "text": "Title of this test case",
          "expected_result": "",
          "srs_id": ""
        }},
        {{
          "step_id": "1.1",
          "step_type": "Precondition",
          "text": "Power on the ALTA Monitor",
          "expected_result": "ALTA Monitor boots and displays startup screen",
          "srs_id": ""
        }},
        {{
          "step_id": "1.5",
          "step_type": "Instruction",
          "text": "Launch CTA Simulator application",
          "expected_result": "CTA Simulator main window opens",
          "srs_id": ""
        }},
        {{
          "step_id": "1.12",
          "step_type": "Verification",
          "text": "Verify HPI value is within expected range",
          "expected_result": "HPI displays 75 ± 2 as per ANA-001",
          "srs_id": "ANA-001"
        }},
        {{
          "step_id": "1.15",
          "step_type": "Cleanup",
          "text": "Stop CTA Simulator waveform output",
          "expected_result": "Simulator status shows Stopped",
          "srs_id": ""
        }}
      ]
    }}
  ],

  "traceability": [
    {{
      "requirement_id": "REQ-001",
      "mapped_test_cases": ["TC-PS-001", "TC-NS-002"]
    }}
  ],

  "risk_traceability": [
    {{
      "risk_id": "RSK-001",
      "mapped_test_cases": ["TC-PS-001"]
    }}
  ],

  "coverage_summary": {{
    "total_test_cases": 27,
    "requirements_covered": 5,
    "risks_covered": 2,
    "screens_referenced": 3,
    "parameters_referenced": 4,
    "scenario_type_breakdown": {{
      "Positive": 5,
      "Negative": 5,
      "Boundary": 5,
      "Alarm": 3,
      "Workflow": 3,
      "Error Handling": 3,
      "Regression": 3
    }}
  }}
}}

====================================================
CRITICAL RULES — READ EVERY ONE
====================================================

SCREEN NAMES:
- NEVER write SCR-001, SCR-013, SCR-023 or any SCR-XXX anywhere.
- Use only human-readable screen names.
- If you do not know the exact screen name, write "Monitoring Screen".

STEP TYPES — only these five values allowed:
  Test Case | Precondition | Instruction | Verification | Cleanup

SRS ID:
- Populate ONLY on Verification steps.
- Use requirement IDs only (e.g. ANA-001). Never risk IDs or screen IDs.
- All other step types: srs_id must be empty string "".

TEST CASE TITLES:
- Every tc_id must have a real, descriptive title.
- NEVER write "Test Case for TC-AS-019" or anything like it.

INSTRUCTION GRANULARITY:
- One physical action per Instruction step.
- MINIMUM 8 Instruction steps before any Verification step.
- Follow this execution sequence:
    1. Preconditions (2-4 steps): power on, connect hardware
    2. Instructions — simulator setup (3-5 steps): launch, load profile, set parameters
    3. Instructions — navigation (2-3 steps): navigate to each screen
    4. Instructions — execution (3-5 steps): perform the action, observe display
    5. Verification (1-3 steps): verify one specific measurable behavior per step
    6. Cleanup (2-3 steps): restore system to baseline

EXPECTED RESULTS on Verification steps must be SPECIFIC and MEASURABLE.
  GOOD: "HPI displays 78 ± 2 as per ANA-001"
  BAD:  "System behaves correctly"

JSON VALIDITY:
- All strings must be properly escaped.
- No trailing commas.
- No comments inside JSON.
- The entire response must be parseable by Python json.loads().
"""

    raw = ask_gemini(prompt)
    return _build_protocol_from_json(raw, user_input, traceability)


# ============================================================
# JSON → STRUCTURED MARKDOWN CONVERTER
# ============================================================

def _build_protocol_from_json(raw_json, user_input, traceability):
    """
    Parse JSON from Gemini, register in SQLite, convert to structured markdown.
    """
    data = None

    try:
        data = json.loads(_clean_json(raw_json))
    except json.JSONDecodeError:
        try:
            match = re.search(r'\{.*\}', raw_json, re.DOTALL)
            if match:
                data = json.loads(match.group())
        except Exception:
            pass

    if not data:
        return _fallback(user_input, raw_json, "JSON parse failed")

    # ── Register in SQLite (no API calls) ─────────────────
    try:
        from services.protocol_registry_service import register_protocol
        from services.tc_registry_service import register_test_cases
        register_protocol(data)
        register_test_cases(data)
    except Exception:
        pass  # Never let registry failure break the user's protocol

    # ── Build markdown output ─────────────────────────────
    lines = []

    info = data.get("protocol_info", {})

    lines.append("## PROTOCOL INFORMATION")
    lines.append("")
    lines.append(f"Protocol ID: {info.get('protocol_id', 'ALTA-PROTO-001')}")
    lines.append(f"Protocol Name: {info.get('protocol_name', user_input + ' Validation Protocol')}")
    lines.append(f"Feature: {info.get('feature', user_input)}")
    lines.append(f"Objective: {info.get('objective', '')}")
    lines.append(f"Related Requirements: {', '.join(info.get('related_requirements', []))}")
    lines.append(f"Related Risks: {', '.join(info.get('related_risks', []))}")

    screens = [_strip_screen_ids(s) for s in info.get('related_screens', [])]
    lines.append(f"Related Screens: {', '.join(screens)}")
    lines.append(f"Related Parameters: {', '.join(info.get('related_parameters', []))}")
    lines.append("")

    lines.append("## PRECONDITIONS")
    lines.append("")
    for item in info.get("preconditions", []):
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## TEST ENVIRONMENT")
    lines.append("")
    for key, val in info.get("test_environment", {}).items():
        lines.append(f"- {key}: {val}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Test Case Summary
    lines.append("## TEST CASE SUMMARY")
    lines.append("")
    lines.append("| Execution Order | Test Case ID | Title | Priority | Scenario Type | Related Requirements |")
    lines.append("|---|---|---|---|---|---|")

    test_cases = data.get("test_cases", [])
    for tc in test_cases:
        reqs  = ", ".join(tc.get("related_requirements", [])) or "-"
        title = tc.get("title", "").replace("|", "-")
        lines.append(
            f"| {tc.get('execution_order', '')} "
            f"| {tc.get('tc_id', '')} "
            f"| {title} "
            f"| {tc.get('priority', '')} "
            f"| {tc.get('scenario_type', '')} "
            f"| {reqs} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Test Steps
    lines.append("## TEST STEPS")
    lines.append("")
    lines.append("| Test Case ID | Step ID | Step Type | Text | Expected Result | SRS ID | Status | Comment |")
    lines.append("|---|---|---|---|---|---|---|---|")

    for tc in test_cases:
        tc_id = tc.get("tc_id", "")
        for step in tc.get("steps", []):
            text     = _strip_screen_ids(step.get("text", "")).replace("|", "-")
            expected = _strip_screen_ids(step.get("expected_result", "")).replace("|", "-")
            srs      = step.get("srs_id", "")
            if step.get("step_type", "") != "Verification":
                srs = ""
            lines.append(
                f"| {tc_id} "
                f"| {step.get('step_id', '')} "
                f"| {step.get('step_type', '')} "
                f"| {text} "
                f"| {expected} "
                f"| {srs} "
                f"|  |  |"
            )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Traceability
    lines.append("## REQUIREMENT TRACEABILITY")
    lines.append("")
    lines.append("| Requirement ID | Mapped Test Cases |")
    lines.append("|---|---|")
    for item in data.get("traceability", []):
        tc_ids = ", ".join(item.get("mapped_test_cases", []))
        lines.append(f"| {item.get('requirement_id', '')} | {tc_ids} |")

    lines.append("")
    lines.append("## RISK TRACEABILITY")
    lines.append("")
    lines.append("| Risk ID | Mapped Test Cases |")
    lines.append("|---|---|")
    for item in data.get("risk_traceability", []):
        tc_ids = ", ".join(item.get("mapped_test_cases", []))
        lines.append(f"| {item.get('risk_id', '')} | {tc_ids} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Coverage
    lines.append("## COVERAGE SUMMARY")
    lines.append("")
    cov = data.get("coverage_summary", {})
    lines.append(f"Total Test Cases: {cov.get('total_test_cases', len(test_cases))}")
    lines.append(f"Requirements Covered: {cov.get('requirements_covered', '')}")
    lines.append(f"Risks Covered: {cov.get('risks_covered', '')}")
    lines.append(f"Screens Referenced: {cov.get('screens_referenced', '')}")
    lines.append(f"Parameters Referenced: {cov.get('parameters_referenced', '')}")
    lines.append("")
    lines.append("Scenario Type Breakdown:")
    for stype, count in cov.get("scenario_type_breakdown", {}).items():
        lines.append(f"  {stype}: {count} test case(s)")

    return "\n".join(lines)


# ============================================================
# FALLBACK
# ============================================================

def _fallback(user_input, raw, error_msg):
    return (
        f"## PROTOCOL INFORMATION\n\n"
        f"Protocol ID: ALTA-PROTO-FALLBACK\n"
        f"Protocol Name: {user_input} Validation Protocol\n"
        f"Feature: {user_input}\n"
        f"Objective: Protocol generation encountered a JSON parse error.\n"
        f"Related Requirements: \nRelated Risks: \nRelated Screens: \nRelated Parameters: \n\n"
        f"## PRECONDITIONS\n\n- Review raw output below and regenerate.\n\n"
        f"## TEST ENVIRONMENT\n\n- JSON Parse Error: {error_msg}\n\n"
        f"---\n\n"
        f"## TEST CASE SUMMARY\n\n"
        f"| Execution Order | Test Case ID | Title | Priority | Scenario Type | Related Requirements |\n"
        f"|---|---|---|---|---|---|\n\n---\n\n"
        f"## TEST STEPS\n\n"
        f"| Test Case ID | Step ID | Step Type | Text | Expected Result | SRS ID | Status | Comment |\n"
        f"|---|---|---|---|---|---|---|---|\n\n---\n\n"
        f"## REQUIREMENT TRACEABILITY\n\n| Requirement ID | Mapped Test Cases |\n|---|---|\n\n"
        f"## RISK TRACEABILITY\n\n| Risk ID | Mapped Test Cases |\n|---|---|\n\n---\n\n"
        f"## COVERAGE SUMMARY\n\nTotal Test Cases: 0\n\n---\n\nRAW AI OUTPUT:\n\n{raw}"
    )