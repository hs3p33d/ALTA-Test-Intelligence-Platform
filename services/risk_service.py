from pathlib import Path
import re

RISK_FILE = Path("master_data/risks.md")


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


if __name__ == "__main__":

    context = build_risk_context("HPI")

    print(context)