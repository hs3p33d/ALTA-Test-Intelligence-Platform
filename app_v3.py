import re
from pathlib import Path

import pandas as pd
import sqlite3
import streamlit as st

from services.rag_service import ask_alta

DB_NAME = "alta_poc.db"
BASE_DIR = Path(__file__).resolve().parent


# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="ALTA Test Intelligence Platform",
    page_icon="🩺",
    layout="wide"
)


# ==========================================
# CSS
# ==========================================

def load_css():
    try:
        css_path = BASE_DIR / "styles.css"
        if css_path.exists():
            with open(css_path, "r", encoding="utf-8") as f:
                st.markdown(
                    f"<style>{f.read()}</style>",
                    unsafe_allow_html=True
                )
    except Exception:
        pass


load_css()


# ==========================================
# HELPERS
# ==========================================

def count_occurrences(file_path: str, marker: str) -> int:
    try:
        path = BASE_DIR / file_path
        if not path.exists():
            return 0
        text = path.read_text(encoding="utf-8", errors="ignore")
        return len(re.findall(re.escape(marker), text, flags=re.MULTILINE))
    except Exception:
        return 0


def normalize_text(value):
    if value is None:
        return ""
    return str(value).strip()


# ==========================================
# DATABASE
# ==========================================

@st.cache_data
def load_requirements():
    conn = sqlite3.connect(DB_NAME)

    query = """
    SELECT
        id,
        title,
        category,
        feature,
        priority
    FROM requirements
    ORDER BY id
    """

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_requirement(req_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    row = cursor.execute(
        """
        SELECT *
        FROM requirements
        WHERE id = ?
        """,
        (req_id,)
    ).fetchone()

    conn.close()
    return row


# ==========================================
# SESSION STATE
# ==========================================

if "selected_req" not in st.session_state:
    st.session_state.selected_req = None

if "qa_query" not in st.session_state:
    st.session_state.qa_query = ""

if "qa_result" not in st.session_state:
    st.session_state.qa_result = ""

if "qa_last_submitted" not in st.session_state:
    st.session_state.qa_last_submitted = ""


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown(
    """
<div style="padding: 0.25rem 0 1rem 0;">
    <div style="font-size: 1.4rem; font-weight: 800; color: #ffffff;">🩺 ALTA AI</div>
    <div style="font-size: 0.85rem; color: #9fb3c8;">Clinical Test Intelligence Platform</div>
</div>
""",
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔎 AI Q&A",
        "📋 Requirement Repository",
        "🧪 Test Scenario Generator",
        "📝 Protocol Generator",
        "📊 Impact Analysis"
    ],
    label_visibility="collapsed"
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    requirements_count = load_requirements().shape[0]
    risks_count = count_occurrences("master_data/risks.md", "Risk ID:")
    screens_count = count_occurrences("master_data/screens.md", "Screen ID:")
    parameters_count = count_occurrences("master_data/parameters.md", "Parameter ID:")

    st.title("ALTA Test Intelligence Platform")

    st.markdown(
        """
<div class="answer-box" style="margin-top: 10px; margin-bottom: 20px;">
    <div style="font-size: 1.6rem; font-weight: 800; margin-bottom: 8px; color: #ffffff;">
        🩺 HemoSphere ALTA AI Platform
    </div>
    <div style="font-size: 1rem; color: #9fb3c8; line-height: 1.6;">
        AI-powered requirement intelligence, risk analysis, scenario generation and impact assessment for ALTA testing.
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
<div class="metric-card">
    <div class="metric-value">{requirements_count}</div>
    <div class="metric-title">Requirements</div>
</div>
""",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
<div class="metric-card">
    <div class="metric-value">{risks_count}</div>
    <div class="metric-title">Risks</div>
</div>
""",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
<div class="metric-card">
    <div class="metric-value">{screens_count}</div>
    <div class="metric-title">Screens</div>
</div>
""",
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
<div class="metric-card">
    <div class="metric-value">{parameters_count}</div>
    <div class="metric-title">Parameters</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.divider()

    s1, s2 = st.columns(2)

    with s1:
        st.info("🟢 Gemini API Status: Connected")

    with s2:
        st.info("🟢 ALTA Knowledge Base Status: Loaded")

    st.subheader("Current Capabilities")

    cap1, cap2, cap3 = st.columns(3)

    with cap1:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-title" style="margin-bottom: 8px;">Knowledge</div>
    <div style="color: #ffffff; line-height: 1.8;">
        ✅ Requirement Search<br>
        ✅ Risk Search<br>
        ✅ Screen Search
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    with cap2:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-title" style="margin-bottom: 8px;">Traceability</div>
    <div style="color: #ffffff; line-height: 1.8;">
        ✅ Parameter Search<br>
        ✅ Traceability Search<br>
        ✅ Relationship Mapping
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    with cap3:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-title" style="margin-bottom: 8px;">AI</div>
    <div style="color: #ffffff; line-height: 1.8;">
        ✅ ALTA Knowledge Search<br>
        ✅ Intent Detection<br>
        ✅ Contextual Answers
    </div>
</div>
""",
            unsafe_allow_html=True
        )

    st.subheader("Roadmap")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-value" style="font-size: 20px;">Ready</div>
    <div class="metric-title">Requirement Repository</div>
</div>
""",
            unsafe_allow_html=True
        )

    with r2:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-value" style="font-size: 20px;">Ready</div>
    <div class="metric-title">AI Q&A</div>
</div>
""",
            unsafe_allow_html=True
        )

    with r3:
        st.markdown(
            """
<div class="metric-card">
    <div class="metric-value" style="font-size: 20px;">Next</div>
    <div class="metric-title">Scenario / Protocol / Impact</div>
</div>
""",
            unsafe_allow_html=True
        )


# ==========================================
# AI Q&A
# ==========================================

elif page == "🔎 AI Q&A":

    st.title("🔍 ALTA Knowledge Search")
    st.caption("Search across Requirements, Risks, Screens, Parameters and Traceability relationships.")

    st.subheader("Suggested Searches")

    q1, q2, q3 = st.columns(3)

    with q1:
        if st.button("What is HPI?", use_container_width=True):
            st.session_state.qa_query = "What is HPI?"
            st.rerun()

        if st.button("Tell me about CAI", use_container_width=True):
            st.session_state.qa_query = "Tell me about CAI"
            st.rerun()

    with q2:
        if st.button("What is RSK-015?", use_container_width=True):
            st.session_state.qa_query = "What is RSK-015?"
            st.rerun()

        if st.button("What risks are associated with HPI?", use_container_width=True):
            st.session_state.qa_query = "What risks are associated with HPI?"
            st.rerun()

    with q3:
        if st.button("Which screens use Smart Wedge?", use_container_width=True):
            st.session_state.qa_query = "Which screens use Smart Wedge?"
            st.rerun()

        if st.button("What parameters are related to CAI?", use_container_width=True):
            st.session_state.qa_query = "What parameters are related to CAI?"
            st.rerun()

    st.divider()

    st.markdown("### Search ALTA Knowledge Base")

    question = st.text_input(
        "Ask ALTA AI",
        value=st.session_state.qa_query,
        placeholder="Type a question like: What is HPI?"
    )

    b1, b2, b3 = st.columns([2, 1, 1])

    with b1:
        search_clicked = st.button("🔍 Search", use_container_width=True)

    with b2:
        clear_clicked = st.button("Clear", use_container_width=True)

    with b3:
        st.caption("Use the buttons above for quick queries.")

    if clear_clicked:
        st.session_state.qa_query = ""
        st.session_state.qa_result = ""
        st.session_state.qa_last_submitted = ""
        st.rerun()

    if search_clicked:
        if not normalize_text(question):
            st.warning("Please enter a question.")
        else:
            st.session_state.qa_query = question
            st.session_state.qa_last_submitted = question
            with st.spinner("Analyzing ALTA Knowledge..."):
                st.session_state.qa_result = ask_alta(question)

    if st.session_state.qa_result:
        st.markdown("### Search Result")
        st.markdown(
            f"""
<div class="answer-box">
{st.session_state.qa_result}
</div>
""",
            unsafe_allow_html=True
        )
    else:
        st.info("Search ALTA knowledge to see requirements, risks, screens and parameters.")


# ==========================================
# REQUIREMENT REPOSITORY
# ==========================================

elif page == "📋 Requirement Repository":

    st.title("Requirements Repository")
    st.caption("Search by requirement ID, title or feature. Select one result to see its full details.")

    df = load_requirements()

    search = st.text_input(
        "Search Requirement ID, Title or Feature",
        placeholder="Example: HPI, Smart Wedge, CAI, ALM-001"
    )

    if normalize_text(search):
        filtered = df[
            df["id"].str.contains(search, case=False, na=False)
            | df["title"].str.contains(search, case=False, na=False)
            | df["feature"].str.contains(search, case=False, na=False)
        ].copy()
    else:
        filtered = df.iloc[0:0].copy()

    result_count = len(filtered)

    st.caption(f"{result_count} results found")

    if not normalize_text(search):
        st.info("Start typing in the search box to filter requirements. This keeps the page clean and avoids loading all items at once.")

    elif result_count == 0:
        st.warning("No matching requirements found.")

    else:
        left, right = st.columns([1, 2])

        # build labels for the radio selector
        req_ids = filtered["id"].tolist()
        req_titles = dict(zip(filtered["id"], filtered["title"]))

        if st.session_state.selected_req not in req_ids:
            st.session_state.selected_req = req_ids[0]

        with left:
            st.subheader("Matching Requirements")

            selected_req = st.radio(
                "Requirements",
                req_ids,
                index=req_ids.index(st.session_state.selected_req),
                format_func=lambda rid: f"{rid} • {req_titles.get(rid, '')[:42]}",
                label_visibility="collapsed"
            )
            st.session_state.selected_req = selected_req

        with right:
            row = get_requirement(st.session_state.selected_req)

            if row:
                st.subheader("Requirement Details")

                st.markdown(
                    f"""
<div class="answer-box">
    <div style="font-size: 14px; color: #00D4FF; font-weight: 700; margin-bottom: 10px;">
        {normalize_text(row[0])}
    </div>
    <div style="font-size: 30px; font-weight: 800; line-height: 1.25;">
        {normalize_text(row[1])}
    </div>
</div>
""",
                    unsafe_allow_html=True
                )

                c1, c2 = st.columns(2)

                with c1:
                    st.markdown(f"**Category:** {normalize_text(row[2])}")
                    st.markdown(f"**Feature:** {normalize_text(row[4])}")

                with c2:
                    st.markdown(f"**Priority:** {normalize_text(row[3])}")

                st.markdown("### Screens")
                st.info(normalize_text(row[5]))

                st.markdown("### Parameters")
                st.info(normalize_text(row[6]))

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### Risks")
                    st.warning(normalize_text(row[7]))

                with col2:
                    st.markdown("### Dependencies")
                    st.info(normalize_text(row[8]))

                st.markdown("### Requirement")
                st.write(normalize_text(row[9]))

                if len(row) > 10 and normalize_text(row[10]):
                    st.markdown("### Verification Method")
                    st.write(normalize_text(row[10]))

                if len(row) > 11 and normalize_text(row[11]):
                    st.markdown("### Acceptance Criteria")
                    st.write(normalize_text(row[11]))

                if len(row) > 12 and normalize_text(row[12]):
                    st.markdown("### Impact Keywords")
                    st.write(normalize_text(row[12]))


# ==========================================
# TEST SCENARIO GENERATOR
# ==========================================

elif page == "🧪 Test Scenario Generator":

    st.title("Test Scenario Generator")
    st.caption("Generate structured test scenarios from ALTA requirements.")

    c1, c2 = st.columns([2, 1])

    with c1:
        feature = st.text_input(
            "Feature / Requirement",
            placeholder="Example: HPI, Smart Wedge, CAI, ANA-001"
        )

    with c2:
        priority = st.selectbox(
            "Scenario Depth",
            ["Standard", "Detailed", "Regression Focus"]
        )

    st.markdown(
        """
<div class="metric-card">
    <div class="metric-title">Expected Output</div>
    <div style="margin-top: 10px; color: #ffffff; line-height: 1.8;">
        Positive scenarios • Negative scenarios • Boundary scenarios • Error scenarios • Regression scenarios
    </div>
</div>
""",
        unsafe_allow_html=True
    )

    if st.button("Generate Scenarios", use_container_width=True):
        st.info("Scenario generation will be connected in the next phase.")


# ==========================================
# PROTOCOL GENERATOR
# ==========================================

elif page == "📝 Protocol Generator":

    st.title("Protocol Generator")
    st.caption("Draft protocol steps in a structured format from an ALTA requirement or feature.")

    c1, c2 = st.columns([2, 2])

    with c1:
        feature = st.text_input(
            "Feature / Requirement",
            placeholder="Example: HPI Alarm Threshold Validation"
        )

    with c2:
        scenario = st.text_input(
            "Scenario",
            placeholder="Example: Trigger alarm above threshold"
        )

    if st.button("Generate Protocol", use_container_width=True):
        st.info("Protocol generation will be connected in the next phase.")

    st.markdown(
        """
<div class="answer-box">
    <div style="font-weight: 800; margin-bottom: 10px;">Protocol Output Preview</div>
    <div style="line-height: 1.8;">
        Step 1 • Preconditions<br>
        Step 2 • Test Actions<br>
        Step 3 • Expected Result<br>
        Step 4 • Pass / Fail Criteria
    </div>
</div>
""",
        unsafe_allow_html=True
    )


# ==========================================
# IMPACT ANALYSIS
# ==========================================

elif page == "📊 Impact Analysis":

    st.title("Impact Analysis")
    st.caption("Identify what should be retested when a feature, parameter or screen changes.")

    changed_feature = st.text_input(
        "Changed Feature / Parameter / Screen",
        placeholder="Example: CAI, HPI, Smart Wedge, SCR-013"
    )

    if st.button("Analyze Impact", use_container_width=True):
        st.info("Impact analysis will be connected in the next phase.")

    st.markdown(
        """
<div class="answer-box">
    <div style="font-weight: 800; margin-bottom: 10px;">Expected Impact Output</div>
    <div style="line-height: 1.8;">
        Affected Requirements<br>
        Affected Screens<br>
        Affected Risks<br>
        Affected Parameters<br>
        Recommended Retest Areas
    </div>
</div>
""",
        unsafe_allow_html=True
    )