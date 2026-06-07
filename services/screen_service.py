from pathlib import Path
import re

SCREEN_FILE = Path("master_data/screens.md")


def search_screens(keyword):

    content = SCREEN_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Screen ID:",
        content
    )

    results = []

    for block in blocks:

        if not block.strip():
            continue

        block = "Screen ID:" + block

        if keyword.lower() in block.lower():

            results.append(block)

    return results


def build_screen_context(keyword):

    matches = search_screens(keyword)

    print("\nSCREEN MATCHES FOUND:", len(matches))

    if not matches:
        return ""

    context = ""

    for screen in matches:

        context += f"""

================================
SCREEN
================================

{screen}

"""

    return context


if __name__ == "__main__":

    context = build_screen_context(
        "Smart Wedge"
    )

    print(context)