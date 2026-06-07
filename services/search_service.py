import sqlite3

DB_NAME = "alta_poc.db"


def search_requirements(keyword, limit=10):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    rows = cursor.execute(
        """
        SELECT
            id,
            title,
            category,
            feature,
            screens,
            parameters,
            risks,
            dependencies,
            requirement
        FROM requirements
        WHERE
            id LIKE ?
            OR title LIKE ?
            OR feature LIKE ?
            OR requirement LIKE ?
            OR impact_keywords LIKE ?
        LIMIT ?
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            limit
        )
    ).fetchall()

    conn.close()

    return rows


def build_context(keyword, limit=5):

    results = search_requirements(
        keyword,
        limit
    )

    if not results:
        return "No relevant requirements found."

    context = ""

    for row in results:

        context += f"""

Requirement ID:
{row[0]}

Title:
{row[1]}

Category:
{row[2]}

Feature:
{row[3]}

Screens:
{row[4]}

Parameters:
{row[5]}

Risks:
{row[6]}

Dependencies:
{row[7]}

Requirement:
{row[8]}

=================================================

"""

    return context


if __name__ == "__main__":

    print("\nSearching for HPI...\n")

    results = search_requirements("HPI")

    for row in results:

        print(
            row[0],
            "|",
            row[1]
        )

    print("\n\nCONTEXT SAMPLE\n")

    print(
        build_context("HPI")
    )