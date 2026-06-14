from pathlib import Path
import re

SCREEN_FILE = Path("master_data/screens.md")


# ==========================================
# SEARCH SCREENS
# ==========================================

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


# ==========================================
# GET SCREEN BY ID
# ==========================================

def get_screen_by_id(screen_id):

    content = SCREEN_FILE.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Screen ID:",
        content
    )

    for block in blocks:

        if not block.strip():
            continue

        full_block = "Screen ID:" + block

        if f"Screen ID: {screen_id}" not in full_block:
            continue

        name_match = re.search(
    r"Screen Name:\s*\n(.+)",
    full_block
)

        return {
            "id": screen_id,
            "name": (
                name_match.group(1).strip()
                if name_match
                else "Unknown Screen"
            )
        }

    return None


# ==========================================
# BUILD CONTEXT
# ==========================================

def build_screen_context(keyword):

    matches = search_screens(keyword)

    print(
        "\nSCREEN MATCHES FOUND:",
        len(matches)
    )

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


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print(
        get_screen_by_id(
            "SCR-023"
        )
    )