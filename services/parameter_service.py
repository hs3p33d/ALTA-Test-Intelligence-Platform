from pathlib import Path
import re

PARAMETER_FILE = Path("master_data/parameters.md")


def search_parameters(keyword):

    content = PARAMETER_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Parameter ID:",
        content
    )

    results = []

    for block in blocks:

        if not block.strip():
            continue

        block = "Parameter ID:" + block

        if keyword.lower() in block.lower():

            results.append(block)

    return results


def build_parameter_context(keyword):

    matches = search_parameters(keyword)

    if not matches:
        return ""

    context = ""

    for parameter in matches[:10]:

        context += f"""

================================
PARAMETER
================================

{parameter}

"""

    return context


if __name__ == "__main__":

    context = build_parameter_context("HPI")

    print(context)