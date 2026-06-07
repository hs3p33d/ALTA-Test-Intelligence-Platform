import streamlit as st
import sqlite3
import pandas as pd

from services.rag_service import ask_alta

DB_NAME = "alta_poc.db"


# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    try:

        with open("styles.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except:

        pass


# ==========================================
# DATABASE FUNCTIONS
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

    df = pd.read_sql_query(
        query,
        conn
    )

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
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ALTA AI Assistant",
    page_icon="🩺",
    layout="wide"
)

load_css()

st.title("🩺 ALTA Test Intelligence Assistant")


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Requirements Repository",
        "AI Q&A"
    ]
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "Dashboard":

    st.header("ALTA Test Intelligence Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">85</div>
            <div class="metric-title">Requirements</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">15</div>
            <div class="metric-title">Risks</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">25</div>
            <div class="metric-title">Screens</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">20</div>
            <div class="metric-title">Parameters</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.success("🟢 Gemini API Connected")

    st.success("🟢 ALTA Knowledge Base Loaded")

    st.info("""
### Current Capabilities

✅ Requirement Search

✅ Risk Search

✅ Screen Search

✅ Parameter Search

✅ Traceability Search

✅ AI Question Answering
""")

    st.subheader("POC Roadmap")

    st.write("""
Current Phase:
- Dashboard
- Requirements Repository
- AI Q&A

Upcoming:
- Scenario Generator
- Protocol Generator
- Impact Analysis
""")

# ==========================================
# REQUIREMENTS REPOSITORY
# ==========================================

elif page == "Requirements Repository":

    st.header("Requirements Repository")

    df = load_requirements()

    search = st.text_input(
        "Search Requirement"
    )

    if search:

        filtered = df[
            df["id"].str.contains(search, case=False)
            |
            df["title"].str.contains(search, case=False)
            |
            df["feature"].str.contains(search, case=False)
        ]

    else:

        filtered = df

    st.write(
        f"Total Results: {len(filtered)}"
    )

    st.dataframe(
        filtered,
        use_container_width=True
    )

    if len(filtered) > 0:

        selected = st.selectbox(
            "Select Requirement",
            filtered["id"]
        )

        if selected:

            row = get_requirement(selected)

            st.subheader(row[1])

            st.write("### Category")
            st.write(row[2])

            st.write("### Priority")
            st.write(row[3])

            st.write("### Feature")
            st.write(row[4])

            st.write("### Screens")
            st.write(row[5])

            st.write("### Parameters")
            st.write(row[6])

            st.write("### Risks")
            st.write(row[7])

            st.write("### Dependencies")
            st.write(row[8])

            st.write("### Requirement")
            st.write(row[9])

            st.write("### Verification Method")
            st.write(row[10])

            st.write("### Acceptance Criteria")
            st.write(row[11])

            st.write("### Impact Keywords")
            st.write(row[12])


# ==========================================
# AI Q&A
# ==========================================

elif page == "AI Q&A":

    st.header("ALTA AI Assistant")

    st.subheader("Quick Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("What is HPI?"):
            st.session_state["question"] = "What is HPI?"

        if st.button("Tell me about CAI"):
            st.session_state["question"] = "Tell me about CAI"

        if st.button("What is RSK-015?"):
            st.session_state["question"] = "What is RSK-015?"

    with col2:

        if st.button("Which screens use Smart Wedge?"):
            st.session_state["question"] = "Which screens use Smart Wedge?"

        if st.button("What risks are associated with HPI?"):
            st.session_state["question"] = "What risks are associated with HPI?"

        if st.button("What parameters are related to CAI?"):
            st.session_state["question"] = "What parameters are related to CAI?"

    st.divider()

    question = st.text_area(
        "Ask ALTA AI",
        value=st.session_state.get(
            "question",
            ""
        ),
        height=120,
        placeholder="Ask anything about ALTA..."
    )

    col1, col2 = st.columns(2)

    with col1:

        ask_clicked = st.button(
            "Ask AI"
        )

    with col2:

        clear_clicked = st.button(
            "Clear"
        )

    if clear_clicked:

        st.session_state["question"] = ""

        st.rerun()

    if ask_clicked:

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Analyzing Requirements, Risks, Screens and Parameters..."
            ):

                try:

                    answer = ask_alta(
                        question
                    )

                    st.success(
                        "Answer Generated"
                    )

                    st.markdown(
                        f"""
<div class="answer-box">
{answer}
</div>
""",
                        unsafe_allow_html=True
                    )

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )