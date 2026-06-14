"""
impact_score_service.py

Deterministic Impact Scoring Engine.

Calculates an integer score 0-100 based on change characteristics
detected from the user input and the affected requirement/risk/screen data.

Score is calculated BEFORE the Gemini call.
Gemini receives the pre-calculated score and is instructed to explain it,
not invent its own.

Score Bands:
     0 – 30  =  LOW
    31 – 70  =  MEDIUM
    71 – 100 =  HIGH

No API calls. Pure Python.
"""

import re


# ============================================================
# SCORING WEIGHTS
# Adjust these numbers to tune sensitivity.
# ============================================================

WEIGHTS = {
    # Change type signals (detected from user_input text)
    "direct_requirement_change":  30,   # User input contains a requirement ID (e.g. ANA-001)
    "alarm_change":               25,   # Input mentions alarm, threshold, trigger, alert
    "analytics_change":           20,   # Input mentions algorithm, calculation, prediction, FFT
    "configuration_change":       10,   # Input mentions setting, configure, adjust, modify
    "parameter_value_change":      8,   # Input contains "from X to Y" numeric pattern

    # Data breadth signals (detected from affected data counts)
    "risk_count_high":            20,   # More than 3 risks affected
    "risk_count_medium":          10,   # 2-3 risks affected
    "screen_count_high":          10,   # More than 3 screens affected
    "screen_count_medium":         5,   # 2-3 screens affected
    "requirement_count_high":     15,   # More than 5 requirements affected
    "requirement_count_medium":    8,   # 3-5 requirements affected

    # Risk severity signals (from enrichment_service)
    "high_severity_risk_present": 15,   # Any affected risk has severity HIGH or CRITICAL
    "medium_severity_risk":        5,   # Any affected risk has severity MEDIUM
}

# Keyword lists for change type detection
ALARM_KEYWORDS = [
    "alarm", "alert", "threshold", "trigger", "notification",
    "silence", "acknowledge", "alarm priority", "audible", "visual alarm",
    "alarm limit", "alarm delay", "alarm condition"
]

ANALYTICS_KEYWORDS = [
    "algorithm", "calculation", "formula", "predict", "index",
    "fft", "waveform analysis", "model", "coefficient", "compute",
    "analytics", "trend calculation", "hpi", "cai", "wedge index"
]

CONFIGURATION_KEYWORDS = [
    "configur", "setting", "default", "adjust", "modify",
    "chang", "updat", "limit", "range", "parameter value"
]


# ============================================================
# SCORING ENGINE
# ============================================================

def calculate_impact_score(
    user_input: str,
    affected_requirements: list,
    affected_risks: list,
    affected_screens: list,
    affected_parameters: list,
    risk_severities: list = None,
) -> dict:
    """
    Calculate a deterministic impact score.

    Args:
        user_input:              The raw change description from the user.
        affected_requirements:   List of requirement ID strings.
        affected_risks:          List of risk ID strings.
        affected_screens:        List of screen ID strings (raw, may include SCR-XXX).
        affected_parameters:     List of parameter strings.
        risk_severities:         Optional list of severity strings for affected risks.
                                 If provided, used for HIGH/MEDIUM severity bonus.

    Returns:
        {
            "score":       72,
            "level":       "HIGH",
            "factors":     ["direct_requirement_change", "alarm_change", ...],
            "breakdown":   {"direct_requirement_change": 30, "alarm_change": 25},
            "explanation": "Score: 72/100 → HIGH\n  ..."
        }
    """
    score = 0
    factors = []
    breakdown = {}

    text = user_input.lower()

    # ── Change type signals ───────────────────────────────

    # Direct requirement ID in input
    if re.search(r"[A-Z]{2,6}-\d+", user_input):
        _add(score, factors, breakdown, "direct_requirement_change", WEIGHTS)
        score += WEIGHTS["direct_requirement_change"]

    # Alarm change
    if any(kw in text for kw in ALARM_KEYWORDS):
        factors.append("alarm_change")
        breakdown["alarm_change"] = WEIGHTS["alarm_change"]
        score += WEIGHTS["alarm_change"]

    # Analytics / algorithm change
    if any(kw in text for kw in ANALYTICS_KEYWORDS):
        factors.append("analytics_change")
        breakdown["analytics_change"] = WEIGHTS["analytics_change"]
        score += WEIGHTS["analytics_change"]

    # Configuration change
    if any(kw in text for kw in CONFIGURATION_KEYWORDS):
        factors.append("configuration_change")
        breakdown["configuration_change"] = WEIGHTS["configuration_change"]
        score += WEIGHTS["configuration_change"]

    # Numeric value change pattern  e.g. "from 85 to 90"
    if re.search(r"from\s+\d+[\.\d]*\s+to\s+\d+[\.\d]*", text):
        factors.append("parameter_value_change")
        breakdown["parameter_value_change"] = WEIGHTS["parameter_value_change"]
        score += WEIGHTS["parameter_value_change"]

    # ── Data breadth signals ──────────────────────────────

    req_count = len(affected_requirements)
    if req_count > 5:
        factors.append("requirement_count_high")
        breakdown["requirement_count_high"] = WEIGHTS["requirement_count_high"]
        score += WEIGHTS["requirement_count_high"]
    elif req_count >= 3:
        factors.append("requirement_count_medium")
        breakdown["requirement_count_medium"] = WEIGHTS["requirement_count_medium"]
        score += WEIGHTS["requirement_count_medium"]

    risk_count = len(affected_risks)
    if risk_count > 3:
        factors.append("risk_count_high")
        breakdown["risk_count_high"] = WEIGHTS["risk_count_high"]
        score += WEIGHTS["risk_count_high"]
    elif risk_count >= 2:
        factors.append("risk_count_medium")
        breakdown["risk_count_medium"] = WEIGHTS["risk_count_medium"]
        score += WEIGHTS["risk_count_medium"]

    screen_count = len(affected_screens)
    if screen_count > 3:
        factors.append("screen_count_high")
        breakdown["screen_count_high"] = WEIGHTS["screen_count_high"]
        score += WEIGHTS["screen_count_high"]
    elif screen_count >= 2:
        factors.append("screen_count_medium")
        breakdown["screen_count_medium"] = WEIGHTS["screen_count_medium"]
        score += WEIGHTS["screen_count_medium"]

    # ── Risk severity signals ─────────────────────────────

    if risk_severities:
        severities_upper = [s.upper() for s in risk_severities]
        if any(s in ("HIGH", "CRITICAL") for s in severities_upper):
            factors.append("high_severity_risk_present")
            breakdown["high_severity_risk_present"] = WEIGHTS["high_severity_risk_present"]
            score += WEIGHTS["high_severity_risk_present"]
        elif any(s == "MEDIUM" for s in severities_upper):
            factors.append("medium_severity_risk")
            breakdown["medium_severity_risk"] = WEIGHTS["medium_severity_risk"]
            score += WEIGHTS["medium_severity_risk"]

    # ── Cap and band ──────────────────────────────────────

    score = min(score, 100)

    if score <= 30:
        level = "LOW"
    elif score <= 70:
        level = "MEDIUM"
    else:
        level = "HIGH"

    # ── Human-readable explanation ────────────────────────

    breakdown_lines = [
        f"    {_label(k)}: +{v} points"
        for k, v in breakdown.items()
    ]
    explanation = (
        f"Impact Score: {score}/100 → {level}\n"
        f"  Contributing Factors:\n"
        + "\n".join(breakdown_lines)
        + f"\n  Affected: {req_count} requirements, {risk_count} risks, {screen_count} screens"
    )

    return {
        "score":       score,
        "level":       level,
        "factors":     factors,
        "breakdown":   breakdown,
        "explanation": explanation,
    }


def format_score_for_prompt(score_result: dict) -> str:
    """
    Returns the score block for injection into the Gemini prompt.
    Instructs Gemini to use this level, not invent its own.
    """
    return (
        f"PRE-CALCULATED IMPACT SCORE: {score_result['score']}/100\n"
        f"IMPACT LEVEL: {score_result['level']}\n\n"
        f"{score_result['explanation']}\n\n"
        f"INSTRUCTION: You MUST use the above IMPACT LEVEL ({score_result['level']}) "
        f"in your Final QA Assessment section. "
        f"Do not recalculate or override it. "
        f"Your role is to justify this level using the requirement, risk and screen context provided."
    )


# ── Internal helpers ──────────────────────────────────────

def _add(score, factors, breakdown, key, weights):
    """Helper — not actually used in the main flow above but kept for extensions."""
    factors.append(key)
    breakdown[key] = weights[key]


def _label(key: str) -> str:
    """Convert snake_case factor key to readable label."""
    return key.replace("_", " ").title()