import json

from services.search_service import build_context
from services.risk_service import build_risk_context
from services.screen_service import build_screen_context
from services.parameter_service import build_parameter_context
from services.traceability_service import build_traceability_context
from services.gemini_service import ask_gemini


# ==========================================
# QUESTION ANALYZER
# ==========================================

def analyze_question(question):

    prompt = f"""
You are an ALTA AI Assistant.

Analyze the user's question.

Return ONLY valid JSON.

Example:

{{
    "intent": "qa",
    "entity": "HPI"
}}

Allowed intents:

qa
risk_lookup
screen_lookup
parameter_lookup
scenario_generation
protocol_generation
impact_analysis

Question:

{question}
"""

    response = ask_gemini(prompt)

    try:

        start = response.find("{")
        end = response.rfind("}") + 1

        json_text = response[start:end]

        return json.loads(json_text)

    except Exception:

        return {
            "intent": "qa",
            "entity": question
        }


# ==========================================
# CONTEXT BUILDER
# ==========================================

def build_context_for_intent(intent, entity):

    entity = entity.strip()

    requirement_context = build_context(
        entity,
        limit=10
    )

    risk_context = build_risk_context(
        entity
    )

    parameter_context = build_parameter_context(
        entity
    )

    screen_context = f"""
SCREEN DEFINITIONS

{build_screen_context(entity)}

TRACEABILITY RESULTS

{build_traceability_context(entity)}
"""

    return f"""

========================
REQUIREMENTS
========================

{requirement_context}

========================
RISKS
========================

{risk_context}

========================
SCREENS
========================

{screen_context}

========================
PARAMETERS
========================

{parameter_context}

"""


# ==========================================
# PROMPT RULES
# ==========================================

def get_rules(intent):

    if intent == "screen_lookup":

        return """
RULES

1. Use ONLY supplied ALTA knowledge.
2. Always show Screen ID and Screen Name.
3. Use Traceability Results when available.
4. Do not invent screens.
5. If screen exists in traceability but not in screen definitions, clearly mention that.
6. Keep answer concise.

OUTPUT FORMAT

Related Screens

SCR-###
Screen Name

SCR-###
Screen Name
"""

    if intent == "risk_lookup":

        return """
RULES

1. Use ONLY supplied ALTA knowledge.
2. Always show Risk ID and Risk Name.
3. Show Severity.
4. Show Description.
5. Keep answer concise.

OUTPUT FORMAT

Related Risks

RSK-###
Risk Name

Severity:
...

Description:
...
"""

    if intent == "parameter_lookup":

        return """
RULES

1. Use ONLY supplied ALTA knowledge.
2. Always show Parameter ID and Parameter Name.
3. Show Unit if available.
4. Keep answer concise.

OUTPUT FORMAT

Related Parameters

PAR-###
Parameter Name
"""

    return """
RULES

1. Use ONLY supplied ALTA knowledge.
2. Do NOT use general medical knowledge.
3. Always show ID and Name together.
4. Never show IDs alone.
5. Organize answer into sections.

OUTPUT FORMAT

Overview

Related Requirements

Related Risks

Related Screens

Related Parameters

Testing Considerations
"""


# ==========================================
# MAIN ENGINE
# ==========================================

def ask_alta(question):

    analysis = analyze_question(
        question
    )

    print("\n====================")
    print("QUESTION ANALYSIS")
    print("====================")
    print(analysis)

    intent = analysis.get(
        "intent",
        "qa"
    )

    entity = analysis.get(
        "entity",
        question
    )

    context = build_context_for_intent(
        intent,
        entity
    )

    if not context.strip():

        return "No matching ALTA knowledge found."

    rules = get_rules(
        intent
    )

    prompt = f"""
You are an ALTA Test Intelligence Assistant.

{rules}

ALTA KNOWLEDGE

{context}

QUESTION

{question}

ANSWER
"""

    return ask_gemini(
        prompt
    )


# ==========================================
# LOCAL TEST
# ==========================================

if __name__ == "__main__":

    answer = ask_alta(
        "Which screens use Smart Wedge?"
    )

    print("\n====================")
    print("FINAL ANSWER")
    print("====================")
    print(answer)