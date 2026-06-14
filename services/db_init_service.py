"""
db_init_service.py

Creates all new SQLite tables required by the intelligence registry services.
Safe to call on every app startup — uses CREATE TABLE IF NOT EXISTS throughout.

Call init_db() once from app.py at startup.

Tables created:
    generated_protocols         — index of every protocol generated
    protocol_requirement_map    — protocol ↔ requirement traceability
    protocol_risk_map           — protocol ↔ risk traceability
    protocol_screen_map         — protocol ↔ screen traceability
    generated_scenarios         — index of every scenario generated
    scenario_requirement_map    — scenario ↔ requirement traceability
    generated_test_cases        — index of every test case generated
    tc_requirement_map          — test case ↔ requirement traceability
    tc_risk_map                 — test case ↔ risk traceability
"""

import sqlite3
from pathlib import Path

DB = "alta_poc.db"

SCHEMA = """

-- =====================================================
-- PROTOCOL REGISTRY
-- =====================================================

CREATE TABLE IF NOT EXISTS generated_protocols (
    protocol_id             TEXT PRIMARY KEY,
    protocol_name           TEXT NOT NULL DEFAULT '',
    feature                 TEXT NOT NULL DEFAULT '',
    objective               TEXT DEFAULT '',
    related_requirements    TEXT DEFAULT '',
    related_risks           TEXT DEFAULT '',
    related_screens         TEXT DEFAULT '',
    related_parameters      TEXT DEFAULT '',
    tc_count                INTEGER DEFAULT 0,
    source_input            TEXT DEFAULT '',
    created_at              TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS protocol_requirement_map (
    protocol_id     TEXT NOT NULL,
    requirement_id  TEXT NOT NULL,
    PRIMARY KEY (protocol_id, requirement_id)
);

CREATE TABLE IF NOT EXISTS protocol_risk_map (
    protocol_id TEXT NOT NULL,
    risk_id     TEXT NOT NULL,
    PRIMARY KEY (protocol_id, risk_id)
);

CREATE TABLE IF NOT EXISTS protocol_screen_map (
    protocol_id TEXT NOT NULL,
    screen_id   TEXT NOT NULL,
    PRIMARY KEY (protocol_id, screen_id)
);

-- =====================================================
-- SCENARIO REGISTRY
-- =====================================================

CREATE TABLE IF NOT EXISTS generated_scenarios (
    scenario_id             TEXT PRIMARY KEY,
    protocol_id             TEXT DEFAULT '',
    feature                 TEXT DEFAULT '',
    scenario_type           TEXT DEFAULT '',
    priority                TEXT DEFAULT '',
    scenario_text           TEXT DEFAULT '',
    related_requirements    TEXT DEFAULT '',
    related_risks           TEXT DEFAULT '',
    created_at              TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS scenario_requirement_map (
    scenario_id     TEXT NOT NULL,
    requirement_id  TEXT NOT NULL,
    PRIMARY KEY (scenario_id, requirement_id)
);

-- =====================================================
-- TEST CASE REGISTRY
-- =====================================================

CREATE TABLE IF NOT EXISTS generated_test_cases (
    tc_id                   TEXT PRIMARY KEY,
    protocol_id             TEXT DEFAULT '',
    feature                 TEXT DEFAULT '',
    title                   TEXT DEFAULT '',
    priority                TEXT DEFAULT '',
    scenario_type           TEXT DEFAULT '',
    related_requirements    TEXT DEFAULT '',
    related_risks           TEXT DEFAULT '',
    step_count              INTEGER DEFAULT 0,
    verification_count      INTEGER DEFAULT 0,
    created_at              TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS tc_requirement_map (
    tc_id           TEXT NOT NULL,
    requirement_id  TEXT NOT NULL,
    PRIMARY KEY (tc_id, requirement_id)
);

CREATE TABLE IF NOT EXISTS tc_risk_map (
    tc_id   TEXT NOT NULL,
    risk_id TEXT NOT NULL,
    PRIMARY KEY (tc_id, risk_id)
);

"""


def init_db():
    """
    Create all registry tables if they don't already exist.
    Safe to call on every startup.
    """
    conn = sqlite3.connect(DB)
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database initialised successfully.")
    conn = sqlite3.connect(DB)
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ).fetchall()
    conn.close()
    print("All tables:")
    for t in tables:
        print(f"  {t[0]}")