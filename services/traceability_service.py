import sqlite3
import re

DB_NAME = "alta_poc.db"


def get_screen_ids_for_feature(feature):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    rows = cursor.execute(
        """
        SELECT screens
        FROM requirements
        WHERE
            title LIKE ?
            OR feature LIKE ?
            OR requirement LIKE ?
        """,
        (
            f"%{feature}%",
            f"%{feature}%",
            f"%{feature}%"
        )
    ).fetchall()

    conn.close()

    screen_ids = set()

    for row in rows:

        if not row[0]:
            continue

        matches = re.findall(
            r"SCR-\d+",
            row[0]
        )

        screen_ids.update(matches)

    return sorted(screen_ids)


def build_traceability_context(feature):

    screens = get_screen_ids_for_feature(
        feature
    )

    if not screens:
        return ""

    context = "RELATED SCREEN IDS\n\n"

    for screen in screens:

        context += f"{screen}\n"

    return context


if __name__ == "__main__":

    print(
        build_traceability_context(
            "Smart Wedge"
        )
    )