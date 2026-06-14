"""
impact_analysis_service.py  — UPDATED

Changes from original:
  1. Screen IDs resolved to real names via enrichment_service
  2. Risk IDs resolved to real descriptions/severity via enrichment_service
  3. Impact level calculated deterministically via impact_score_service (not by LLM)
  4. Protocol context from protocol_registry_service (real protocols, no hallucination)
  5. Scenario context from scenario_registry_service (real scenarios, no hallucination)
  6. Test case context from tc_registry_service (real test cases, no hallucination)

API calls: still 1 (unchanged). All new context is built deterministically.
"""

from services.search_service import search_requirements
from services.gemini_service import ask_gemini
from services.enrichment_service import (
    format_screens_for_prompt,
    format_risks_for_prompt,
    get_risk_severity,
)
from services.impact_score_service import (
    calculate_impact_score,
    format_score_for_prompt,
)
from services.protocol_registry_service import format_protocol_impact_for_prompt
from services.scenario_registry_service import format_scenario_impact_for_prompt
from services.tc_registry_service import format_tc_impact_for_prompt


def generate_impact_analysis(user_input):

    # =====================================
    # FEATURE EXTRACTION
    # =====================================

    keyword = user_input

    known_features = [
        "HPI",
        "CAI",
        "Smart Wedge",
        "PPV",
        "SVV",
        "MAP",
        "CO",
        "CI",
        "PAOP",
        "GHI"
    ]

    for feature in known_features:
        if feature.lower() in user_input.lower():
            keyword = feature
            break

    # =====================================
    # REQUIREMENT SEARCH
    # =====================================

    requirements = search_requirements(keyword)

    requirement_context   = ""
    affected_requirements = []
    affected_screens_raw  = set()
    affected_parameters   = set()
    affected_risks_raw    = set()
    affected_components   = set()

    for req in requirements[:25]:

        req_id      = req[0]
        title       = req[1]
        category    = req[2]
        feature     = req[3]
        screens     = req[4]
        parameters  = req[5]
        risks       = req[6]
        components  = req[7]
        description = req[8]

        affected_requirements.append(req_id)

        requirement_context += f"""
Requirement ID:
{req_id}

Title:
{title}

Category:
{category}

Feature:
{feature}

Description:
{description}

====================================================
"""
        for line in str(screens).split("\n"):
            line = line.replace("•", "").strip()
            if line:
                affected_screens_raw.add(line)

        for line in str(parameters).split("\n"):
            line = line.replace("•", "").strip()
            if line:
                affected_parameters.add(line)

        for line in str(risks).split("\n"):
            line = line.replace("•", "").strip()
            if line:
                affected_risks_raw.add(line)

        for line in str(components).split("\n"):
            line = line.replace("•", "").strip()
            if line:
                affected_components.add(line)

    # =====================================
    # ENRICH SCREENS AND RISKS
    # =====================================

    # Build enriched screen block (SCR-XXX → real names + descriptions)
    screens_context = format_screens_for_prompt(
        "\n".join(sorted(affected_screens_raw))
    )

    # Build enriched risk block (RSK-XXX → real title + severity + mitigation)
    risks_context = format_risks_for_prompt(
        "\n".join(sorted(affected_risks_raw))
    )

    # Plain text contexts (unchanged)
    requirements_context = "\n".join(sorted(set(affected_requirements)))
    parameters_context   = "\n".join(sorted(affected_parameters))
    components_context   = "\n".join(sorted(affected_components))

    # =====================================
    # DETERMINISTIC IMPACT SCORE
    # =====================================

    # Collect risk severities for the scoring engine
    risk_severities = [
        get_risk_severity(rid)
        for rid in affected_risks_raw
        if rid.startswith("RSK-")
    ]

    impact_score = calculate_impact_score(
        user_input            = user_input,
        affected_requirements = list(set(affected_requirements)),
        affected_risks        = [r for r in affected_risks_raw if r.startswith("RSK-")],
        affected_screens      = [s for s in affected_screens_raw if s.startswith("SCR-")],
        affected_parameters   = list(affected_parameters),
        risk_severities       = risk_severities,
    )

    score_context = format_score_for_prompt(impact_score)

    # =====================================
    # REGISTRY CONTEXTS (no API calls)
    # =====================================

    protocol_context = format_protocol_impact_for_prompt(
        keyword  = keyword,
        req_ids  = list(set(affected_requirements)),
    )

    scenario_context = format_scenario_impact_for_prompt(
        keyword  = keyword,
        req_ids  = list(set(affected_requirements)),
    )

    tc_context = format_tc_impact_for_prompt(
        keyword  = keyword,
        req_ids  = list(set(affected_requirements)),
    )

    # =====================================
    # GEMINI PROMPT
    # =====================================

    prompt = f"""
You are a Principal Medical Device Verification Lead working on the BD HemoSphere ALTA platform.

You are performing a formal Change Impact Analysis.

Your responsibility is to determine:

- Requirement Impact
- Screen Impact
- Parameter Impact
- Risk Impact
- Verification Impact
- Protocol Impact
- Regression Impact
- Validation Impact
- Traceability Impact

You are NOT writing a management summary.
You are performing a regulated medical device impact assessment.

====================================================
CHANGE REQUEST
====================================================

{user_input}

====================================================
DETECTED FEATURE
====================================================

{keyword}

====================================================
IMPACT SCORE (PRE-CALCULATED — DO NOT CHANGE)
====================================================

{score_context}

====================================================
AFFECTED REQUIREMENTS
====================================================

{requirements_context}

====================================================
REQUIREMENT DETAILS
====================================================

{requirement_context}

====================================================
AFFECTED SCREENS (with metadata — use names shown, not IDs)
====================================================

{screens_context}

====================================================
AFFECTED PARAMETERS
====================================================

{parameters_context}

====================================================
AFFECTED RISKS (with metadata — use descriptions shown, do not modify them)
====================================================

{risks_context}

====================================================
AFFECTED COMPONENTS
====================================================

{components_context}

====================================================
KNOWN PROTOCOLS (use ONLY these — do not invent protocol IDs)
====================================================

{protocol_context}

====================================================
AFFECTED SCENARIOS (from scenario registry)
====================================================

{scenario_context}

====================================================
AFFECTED TEST CASES (from test case registry)
====================================================

{tc_context}

====================================================
OUTPUT FORMAT
====================================================

# Change Classification

Classify the change as one or more of:

- Requirement Change
- Configuration Change
- Alarm Change
- Parameter Change
- Workflow Change
- UI Change
- Analytics Change
- Algorithm Change
- Integration Change

Explain rationale.

====================================================

# Requirement Impact Assessment

For each impacted requirement provide:

Requirement ID
Title
Impact Level (HIGH / MEDIUM / LOW)
Direct / Indirect
Reason

====================================================

# Screen Impact Assessment

For each impacted screen provide the SCREEN NAME (not SCR-XXX ID):

Screen Name
Impact Level
Required Validation

====================================================

# Parameter Impact Assessment

For each parameter provide:

Parameter
Impact Level
Validation Required

====================================================

# Risk Impact Assessment

For each risk use ONLY the description provided in the AFFECTED RISKS section above.
Do NOT invent risk descriptions.

Risk ID
Risk Title (from provided metadata)
Severity (from provided metadata)
Risk Exposure Change
Mitigation Verification Required

====================================================

# Verification Impact Assessment

Identify affected verification activities.

Examples:
- Boundary Validation
- Alarm Validation
- Workflow Validation
- Analytics Validation
- Logging Validation
- Trend Validation
- Persistence Validation
- Configuration Validation

Explain why each activity is required.

====================================================

# Traceability Impact Assessment

Identify:
Affected Requirements
Affected Risks
Affected Screens (use names)
Affected Parameters
Affected Components

Explain traceability relationships.

====================================================

# Protocol Impact Assessment

Use ONLY the protocols listed in the KNOWN PROTOCOLS section above.
If no protocols exist yet, describe what TYPE of protocol is needed — do NOT invent protocol IDs.

Determine whether protocols require:
- No Change
- Minor Update
- Major Revision
- New Protocol Required

Provide rationale.

====================================================

# Regression Impact Assessment

If affected test cases are listed in the AFFECTED TEST CASES section above,
reference them by their real TC IDs.

Determine:
- Targeted Regression
- Feature Regression
- Subsystem Regression
- Full Regression

Provide rationale.

Identify:
High Priority Regression Areas (reference real TC IDs if available)
Medium Priority Regression Areas
Low Priority Regression Areas

====================================================

# Recommended Test Types

Include:
- Positive Testing
- Negative Testing
- Boundary Testing
- Workflow Testing
- Alarm Testing
- Error Handling Testing
- Regression Testing

For each provide:
Reason
Coverage Goal

====================================================

# Recommended Validation Activities

Generate detailed validation recommendations using ALTA terminology.

Examples:
- Verify threshold persistence across reboot
- Verify audit log generation
- Verify trend calculations
- Verify parameter refresh intervals
- Verify alarm state transitions

====================================================

# Recommended New Test Scenarios

If affected scenarios are listed in the AFFECTED SCENARIOS section above,
reference them by ID and note whether they need to be re-generated or updated.

Generate 5-10 high-value NEW scenarios where gaps exist.

For each new scenario:
Scenario
Objective
Priority

====================================================

# Final QA Assessment

The impact level has been pre-calculated as: {impact_score['level']}
Score: {impact_score['score']}/100

Your task:
1. Confirm this level is appropriate given the requirement and risk context.
2. Explain the key drivers behind this score.
3. State the recommended QA approach for {impact_score['level']} impact changes.

DO NOT assign a different impact level. Use: {impact_score['level']}

====================================================
RULES
====================================================

1. Use supplied requirements only.
2. Use supplied screen NAMES (not IDs).
3. Use supplied risk descriptions — do not modify or invent them.
4. Use supplied parameters and components.
5. Do not invent requirement IDs, risk IDs, or protocol IDs.
6. Reference real test case IDs and scenario IDs where provided.
7. Focus on verification impact, validation activities, and traceability.
8. Use ALTA terminology throughout.
9. Be structured. Use bullet points where appropriate.
10. Think like a Principal Medical Device Verification Lead.
11. Output must be suitable for future Polarion-based impact assessments.
"""

    return ask_gemini(prompt)