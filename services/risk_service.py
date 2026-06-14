from pathlib import Path
import re

RISK_FILE = Path("master_data/risks.md")


# ==========================================
# SEARCH RISKS
# ==========================================

def search_risks(keyword):

    content = RISK_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Risk ID:",
        content
    )

    results = []

    for block in blocks:

        if not block.strip():
            continue

        block = "Risk ID:" + block

        if keyword.lower() in block.lower():

            results.append(block)

    return results


# ==========================================
# GET RISK BY ID
# ==========================================

def get_risk_by_id(risk_id):

    content = RISK_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Risk ID:",
        content
    )

    for block in blocks:

        if not block.strip():
            continue

        full_block = "Risk ID:" + block

        if f"Risk ID: {risk_id}" not in full_block:
            continue

        title_match = re.search(
    r"Risk Name:\s*\n(.+)",
    full_block
)

        return {
    "id": risk_id,
    "title": (
        title_match.group(1).strip()
        if title_match
        else risk_id
    )
}

    return None


# ==========================================
# BUILD CONTEXT
# ==========================================

def build_risk_context(keyword):

    matches = search_risks(keyword)

    if not matches:
        return ""

    context = ""

    for risk in matches[:10]:

        context += f"""

================================
RISK
================================

{risk}

"""

    return context


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print(
        get_risk_by_id(
            "RSK-005"
        )
    )