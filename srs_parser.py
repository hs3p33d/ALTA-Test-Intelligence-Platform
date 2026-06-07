import sqlite3
import re
from pathlib import Path

# ==========================================
# DATABASE SETUP
# ==========================================

DB_NAME = "alta_poc.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS requirements (
    id TEXT PRIMARY KEY,
    title TEXT,
    category TEXT,
    priority TEXT,
    feature TEXT,
    screens TEXT,
    parameters TEXT,
    risks TEXT,
    dependencies TEXT,
    requirement TEXT,
    verification_method TEXT,
    acceptance_criteria TEXT,
    impact_keywords TEXT
)
""")

conn.commit()


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def extract_field(block, field_name):

    fields = [
        "Title",
        "Category",
        "Priority",
        "Feature",
        "Screens",
        "Parameters",
        "Related Risks",
        "Dependencies",
        "Requirement",
        "Verification Method",
        "Acceptance Criteria",
        "Impact Keywords"
    ]

    start_marker = f"{field_name}:"

    start = block.find(start_marker)

    if start == -1:
        return ""

    start += len(start_marker)

    end = len(block)

    for field in fields:

        if field == field_name:
            continue

        pos = block.find(f"\n{field}:", start)

        if pos != -1 and pos < end:
            end = pos

    return block[start:end].strip()


def parse_requirement(block):

    req_match = re.search(
        r"Requirement ID:\s*([A-Z]+-\d+)",
        block
    )

    if not req_match:
        return None

    req_id = req_match.group(1)

    return {
        "id": req_id,
        "title": extract_field(block, "Title"),
        "category": extract_field(block, "Category"),
        "priority": extract_field(block, "Priority"),
        "feature": extract_field(block, "Feature"),
        "screens": extract_field(block, "Screens"),
        "parameters": extract_field(block, "Parameters"),
        "risks": extract_field(block, "Related Risks"),
        "dependencies": extract_field(block, "Dependencies"),
        "requirement": extract_field(block, "Requirement"),
        "verification_method": extract_field(block, "Verification Method"),
        "acceptance_criteria": extract_field(block, "Acceptance Criteria"),
        "impact_keywords": extract_field(block, "Impact Keywords")
    }


def save_requirement(req):

    cursor.execute("""
    INSERT OR REPLACE INTO requirements
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        req["id"],
        req["title"],
        req["category"],
        req["priority"],
        req["feature"],
        req["screens"],
        req["parameters"],
        req["risks"],
        req["dependencies"],
        req["requirement"],
        req["verification_method"],
        req["acceptance_criteria"],
        req["impact_keywords"]
    ))


# ==========================================
# READ ALL REQUIREMENT FILES
# ==========================================

DATA_FOLDER = Path("data")

for file in DATA_FOLDER.glob("*.md"):

    print(f"Processing {file.name}")

    content = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    blocks = re.split(
        r"Requirement ID:",
        content
    )

    for block in blocks:

        if not block.strip():
            continue

        block = "Requirement ID:" + block

        req = parse_requirement(block)

        if req:
            save_requirement(req)

conn.commit()

total = cursor.execute(
    "SELECT COUNT(*) FROM requirements"
).fetchone()[0]

print(f"\nTotal Requirements Imported = {total}")

conn.close()