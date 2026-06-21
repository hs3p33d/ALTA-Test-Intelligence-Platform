"""
ALTA AI — Test Intelligence Platform
Complete rebuild fixing all reported issues:
- Quick template buttons: rendered as HTML links, no Streamlit button conflicts
- Live search: st.session_state driven, no value= conflict
- Medical art: fixed 120x80px on all inner pages, animated CSS on dashboard
- Dashboard: single animated ECG waveform, clean layout
"""

import re
from pathlib import Path
import pandas as pd
import sqlite3
import streamlit as st

from services.rag_service import ask_alta
from services.scenario_service import generate_scenarios
from services.protocol_service import generate_protocol
from services.protocol_excel_builder import protocol_to_excel
from services.impact_analysis_service import generate_impact_analysis

try:
    from services.db_init_service import init_db
    init_db()
except Exception:
    pass

DB_NAME  = "alta_poc.db"
BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title            = "ALTA AI",
    page_icon             = "🩺",
    layout                = "wide",
    initial_sidebar_state = "collapsed",
)


# ── CSS ───────────────────────────────────────────────────

# IMPORTANT:
# Theme must exist BEFORE load_css() is called

if "theme" not in st.session_state:
    st.session_state.theme = "dark"


def load_css():

    theme = st.session_state.get(
        "theme",
        "dark"
    )

    css_file = (
        "styles.css"
        if theme == "dark"
        else "styles_light.css"
    )

    css_path = BASE_DIR / css_file

    if css_path.exists():

        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )


load_css()

# ── Helpers ───────────────────────────────────────────────
def nz(v) -> str:
    return "" if v is None else str(v).strip()

def count_md(fp, marker):
    try:
        p = BASE_DIR / fp
        return len(re.findall(re.escape(marker),
               p.read_text(encoding="utf-8", errors="ignore"))) if p.exists() else 0
    except Exception:
        return 0

def rule():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

def lbl(t):
    st.markdown(f'<p class="field-label">{t}</p>', unsafe_allow_html=True)

def toggle_theme():

    st.session_state.theme = (
        "light"
        if st.session_state.theme == "dark"
        else "dark"
    )


# ── Database ──────────────────────────────────────────────
@st.cache_data
def load_requirements():
    conn = sqlite3.connect(DB_NAME)
    df   = pd.read_sql_query(
        "SELECT id,title,category,feature,priority FROM requirements ORDER BY id", conn)
    conn.close()
    return df

def get_req(req_id):
    conn = sqlite3.connect(DB_NAME)
    row  = conn.cursor().execute(
        "SELECT * FROM requirements WHERE id=?", (req_id,)).fetchone()
    conn.close()
    return row

# ── Session state ─────────────────────────────────────────
_defaults = {
    "page":       "dashboard",
    "sel_req":    None,
    "qa_input":   "", "qa_result": "", "qa_last": "",
    "sc_input":   "", "sc_result": "",
    "pr_input":   "", "pr_result": "",
    "ia_input":   "", "ia_result": "",
    "req_search": "",
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────────────────
# WIDGET-SAFE TEXT INPUT PATTERN
#
# THE REAL BUG:
# Streamlit forbids writing to st.session_state[key] for ANY widget
# that has already been instantiated with that key — not just within
# the same run, but on every subsequent run for the lifetime of that
# widget on the page. This raises StreamlitAPIException unconditionally.
#
# THE CORRECT FIX (Streamlit's own recommended pattern):
# Use TWO separate keys:
#   - a "true" state key (e.g. "qa_input") that the rest of the app
#     reads from and that pills/Clear buttons are allowed to write to
#     freely, since no widget is ever bound to it directly.
#   - a "widget" key (e.g. "qa_input_w") that the actual st.text_input
#     owns. Right BEFORE creating the widget each run, we copy the
#     true value into the widget key — but ONLY if the widget key
#     doesn't exist yet (first run) or a pill/Clear just requested an
#     update via a one-shot "_sync" flag. After the widget renders,
#     we copy its current value back into the true key so the rest of
#     the app always sees what the user typed, live, every keystroke.
# ─────────────────────────────────────────────────────────

def synced_text_input(label, true_key, **kwargs):
    """
    Drop-in replacement for st.text_input that allows external code
    (suggestion pills, Clear buttons) to update the value via
    st.session_state[true_key] = "...", st.rerun() — without ever
    hitting Streamlit's "cannot modify after instantiation" error.

    Returns the current live value (same as st.text_input would).
    """
    widget_key = f"{true_key}__w"

    # Seed the widget key from the true key ONLY when the widget key
    # doesn't exist yet (first render) or a pill/Clear button staged
    # a new value via the "<true_key>__pending" flag.
    pending_flag = f"{true_key}__pending"
    if widget_key not in st.session_state or st.session_state.get(pending_flag, False):
        st.session_state[widget_key] = st.session_state.get(true_key, "")
        st.session_state[pending_flag] = False

    value = st.text_input(label, key=widget_key, **kwargs)

    # Mirror the live widget value back into the true key every run
    # so the rest of the app (Generate buttons, etc.) always sees the
    # current text immediately — true live sync, no Enter needed.
    st.session_state[true_key] = value
    return value


def stage_value(true_key: str, value: str):
    """
    Called by suggestion pills / Clear buttons. Safely schedules a
    new value for a synced_text_input WITHOUT touching the widget's
    own key directly (which would raise StreamlitAPIException).
    Call st.rerun() immediately after this.
    """
    st.session_state[true_key] = value
    st.session_state[f"{true_key}__pending"] = True


# ─────────────────────────────────────────────────────────
# SUGGESTION PILLS  — small inline buttons.
# Use stage_value() so they never touch a widget key directly.
# ─────────────────────────────────────────────────────────
def suggestion_pills(items: list, widget_key: str, group_id: str):
    """
    Render small inline suggestion buttons.
    widget_key: the true_key passed to the matching synced_text_input.
    group_id: must be unique across the entire app (e.g. 'qa_a', 'sc_b').
    """
    cols = st.columns(len(items))
    for i, (label, value) in enumerate(items):
        with cols[i]:
            if st.button(label, key=f"pill_{group_id}_{i}",
                         use_container_width=True):
                stage_value(widget_key, value)
                st.rerun()


# ─────────────────────────────────────────────────────────
# ANIMATED MEDICAL ART  — pure CSS animations, no JS
# Each SVG is self-contained with its own unique IDs.
# Fixed wrapper keeps them 120×80px on inner pages.
# ─────────────────────────────────────────────────────────

# Dashboard: full-width animated ECG strip
DASHBOARD_ECG = """
<div class="dash-ecg-wrap">
  <svg viewBox="0 0 1200 80" preserveAspectRatio="none"
       xmlns="http://www.w3.org/2000/svg" class="dash-ecg">
    <defs>
      <filter id="d-glow">
        <feGaussianBlur stdDeviation="2.5" result="b"/>
        <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
      </filter>
      <linearGradient id="d-fade" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0"   stop-color="#00b4d8" stop-opacity="0"/>
        <stop offset="0.08" stop-color="#00b4d8" stop-opacity="1"/>
        <stop offset="0.92" stop-color="#00b4d8" stop-opacity="1"/>
        <stop offset="1"   stop-color="#00b4d8" stop-opacity="0"/>
      </linearGradient>
    </defs>
    <!-- Grid -->
    <line x1="0" y1="40" x2="1200" y2="40" stroke="#0d1f35" stroke-width="0.8"/>
    <line x1="0" y1="20" x2="1200" y2="20" stroke="#091525" stroke-width="0.4"/>
    <line x1="0" y1="60" x2="1200" y2="60" stroke="#091525" stroke-width="0.4"/>
    <!-- Animated waveform path -->
    <polyline filter="url(#d-glow)"
      stroke="url(#d-fade)" stroke-width="2" fill="none"
      class="ecg-wave"
      points="
        0,40 60,40 70,40 74,34 78,40 90,40 100,40 103,37 106,40
        118,40 124,40 128,12 132,68 136,40 142,28 148,40
        170,40 230,40 234,36 238,40 250,40 260,40 263,37 266,40
        278,40 284,40 288,12 292,68 296,40 302,28 308,40
        330,40 390,40 394,36 398,40 410,40 420,40 423,37 426,40
        438,40 444,40 448,12 452,68 456,40 462,28 468,40
        490,40 550,40 554,36 558,40 570,40 580,40 583,37 586,40
        598,40 604,40 608,12 612,68 616,40 622,28 628,40
        650,40 710,40 714,36 718,40 730,40 740,40 743,37 746,40
        758,40 764,40 768,12 772,68 776,40 782,28 788,40
        810,40 870,40 874,36 878,40 890,40 900,40 903,37 906,40
        918,40 924,40 928,12 932,68 936,40 942,28 948,40
        970,40 1030,40 1034,36 1038,40 1050,40 1060,40 1063,37 1066,40
        1078,40 1084,40 1088,12 1092,68 1096,40 1102,28 1108,40
        1130,40 1190,40 1200,40
      "/>
    <!-- Moving scan dot -->
    <circle r="3.5" fill="#00b4d8" class="ecg-dot" filter="url(#d-glow)">
      <animateMotion dur="4s" repeatCount="indefinite"
        path="M0,40 L60,40 L70,40 L74,34 L78,40 L90,40 L100,40 L103,37 L106,40
              L118,40 L124,40 L128,12 L132,68 L136,40 L142,28 L148,40
              L170,40 L230,40 L234,36 L238,40 L250,40 L260,40 L263,37 L266,40
              L278,40 L284,40 L288,12 L292,68 L296,40 L302,28 L308,40
              L330,40 L390,40 L394,36 L398,40 L410,40 L420,40 L423,37 L426,40
              L438,40 L444,40 L448,12 L452,68 L456,40 L462,28 L468,40
              L490,40 L550,40 L554,36 L558,40 L570,40 L580,40 L583,37 L586,40
              L598,40 L604,40 L608,12 L612,68 L616,40 L622,28 L628,40
              L1200,40"/>
    </circle>
  </svg>
</div>"""

# Inner pages: borderless animated art that sits directly on the
# page background — no boxed/floating card look, integrated into
# the hero row via normal flex layout (not position:absolute).
def page_art(art_id: str) -> str:
    """Returns a small animated SVG, transparent background, no border box."""
    arts = {
        "ecg": """
<svg viewBox="0 0 220 90" xmlns="http://www.w3.org/2000/svg" class="page-art-svg">
  <defs>
    <filter id="pa-ecg-glow">
      <feGaussianBlur stdDeviation="1.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <line x1="10" y1="45" x2="210" y2="45" stroke="#0f2238" stroke-width="0.6"/>
  <polyline filter="url(#pa-ecg-glow)" stroke="#1fa8cc" stroke-width="1.5" fill="none" opacity="0.85"
    points="10,45 28,45 32,45 34,38 36,52 38,45 42,45 44,28 46,62 48,45 52,37 56,45
    70,45 86,45 88,42 90,45 94,45 96,28 98,62 100,45 104,37 108,45
    122,45 138,45 140,42 142,45 146,45 148,28 150,62 152,45 156,37 160,45
    174,45 190,45 192,42 194,45 198,45 200,28 202,62 204,45 208,37 210,45">
    <animate attributeName="stroke-dasharray" from="0,800" to="800,0" dur="3s" repeatCount="indefinite"/>
  </polyline>
  <circle r="2.2" fill="#38c6e8" filter="url(#pa-ecg-glow)">
    <animateMotion dur="3s" repeatCount="indefinite"
      path="M10,45 L28,45 L32,45 L34,38 L36,52 L38,45 L42,45 L44,28 L46,62 L48,45 L52,37 L56,45
            L70,45 L86,45 L88,42 L90,45 L94,45 L96,28 L98,62 L100,45 L104,37 L108,45
            L122,45 L138,45 L140,42 L142,45 L146,45 L148,28 L150,62 L152,45 L156,37 L160,45
            L174,45 L190,45 L192,42 L194,45 L198,45 L200,28 L202,62 L204,45 L208,37 L210,45"/>
  </circle>
</svg>""",
        "heart": """
<svg viewBox="0 0 220 90" xmlns="http://www.w3.org/2000/svg" class="page-art-svg">
  <defs>
    <filter id="pa-h-glow">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="pa-hgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#1fa8cc" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#1fa8cc" stop-opacity="0.04"/>
    </linearGradient>
  </defs>
  <g transform="translate(110,45)">
    <path filter="url(#pa-h-glow)"
      d="M0,24 C-16,15 -32,4 -32,-9 C-32,-20 -23,-27 -13,-27 C-6,-27 -3,-23 0,-18 C3,-23 6,-27 13,-27 C23,-27 32,-20 32,-9 C32,4 16,15 0,24Z"
      fill="url(#pa-hgrad)" stroke="#1fa8cc" stroke-width="1" opacity="0.9">
      <animateTransform attributeName="transform" type="scale"
        values="1;1.06;1;1.04;1" dur="1.3s" repeatCount="indefinite" additive="sum"/>
    </path>
    <polyline filter="url(#pa-h-glow)" stroke="#cfeef8" stroke-width="1" fill="none" opacity="0.5"
      points="-25,0 -16,0 -13,-5 -10,5 -7,0 -3,0 -1,-9 1,12 3,0 6,-3 9,0 16,0 25,0"/>
  </g>
</svg>""",
        "pulse": """
<svg viewBox="0 0 220 90" xmlns="http://www.w3.org/2000/svg" class="page-art-svg">
  <defs>
    <filter id="pa-p-glow">
      <feGaussianBlur stdDeviation="1.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <radialGradient id="pa-pgrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="#1fa8cc" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#1fa8cc" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="110" cy="45" r="34" fill="url(#pa-pgrad)"/>
  <circle cx="110" cy="45" r="34" fill="none" stroke="#0f2238" stroke-width="0.7"/>
  <circle cx="110" cy="45" r="24" fill="none" stroke="#0f2238" stroke-width="0.7"/>
  <circle cx="110" cy="45" r="14" fill="none" stroke="#0f2238" stroke-width="0.7"/>
  <polyline filter="url(#pa-p-glow)" stroke="#1fa8cc" stroke-width="1.4" fill="none" opacity="0.85"
    points="78,45 88,45 90,45 92,39 94,51 96,45 100,45 102,35 104,55 106,45 110,41 114,45
    118,45 120,39 122,51 124,45 126,45 128,35 130,55 132,45 136,41 140,45"/>
  <circle cx="110" cy="45" r="2.5" fill="#38c6e8" filter="url(#pa-p-glow)">
    <animate attributeName="r" values="2.5;4;2.5" dur="1.3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.5;1" dur="1.3s" repeatCount="indefinite"/>
  </circle>
</svg>""",
        "shield": """
<svg viewBox="0 0 220 90" xmlns="http://www.w3.org/2000/svg" class="page-art-svg">
  <defs>
    <filter id="pa-s-glow">
      <feGaussianBlur stdDeviation="1.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="pa-sgrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#1fa8cc" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#1fa8cc" stop-opacity="0.03"/>
    </linearGradient>
  </defs>
  <path filter="url(#pa-s-glow)" transform="translate(110,45)"
    d="M0,-32 L26,-19 L26,7 C26,24 15,35 0,41 C-15,35 -26,24 -26,7 L-26,-19 Z"
    fill="url(#pa-sgrad)" stroke="#1fa8cc" stroke-width="1" opacity="0.9"/>
  <polyline filter="url(#pa-s-glow)" stroke="#38c6e8" stroke-width="2" fill="none"
    stroke-linecap="round" stroke-linejoin="round"
    points="98,45 108,55 122,37">
    <animate attributeName="stroke-dasharray" from="0,60" to="60,0" dur="1.6s"
      repeatCount="indefinite"/>
  </polyline>
</svg>""",
        "wave": """
<svg viewBox="0 0 220 90" xmlns="http://www.w3.org/2000/svg" class="page-art-svg">
  <defs>
    <filter id="pa-w-glow">
      <feGaussianBlur stdDeviation="1.3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="pa-wgrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%"   stop-color="#1fa8cc" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#1fa8cc" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="14" y1="32" x2="206" y2="32" stroke="#0f2238" stroke-width="0.4"/>
  <line x1="14" y1="58" x2="206" y2="58" stroke="#0f2238" stroke-width="0.4"/>
  <polygon fill="url(#pa-wgrad)"
    points="14,66 30,66 36,49 44,29 54,41 62,51 70,54 78,52 86,66
    92,66 98,49 106,29 116,41 124,51 132,54 140,52 148,66
    154,66 160,49 168,29 178,41 186,51 194,54 202,52 206,66"/>
  <polyline filter="url(#pa-w-glow)" stroke="#1fa8cc" stroke-width="1.6" fill="none" opacity="0.9"
    points="14,66 30,66 36,49 44,29 54,41 62,51 70,54 78,52 86,66
    92,66 98,49 106,29 116,41 124,51 132,54 140,52 148,66
    154,66 160,49 168,29 178,41 186,51 194,54 202,52 206,66">
    <animate attributeName="stroke-dasharray" from="0,900" to="900,0" dur="2.6s" repeatCount="indefinite"/>
  </polyline>
  <circle r="2.2" fill="#38c6e8" filter="url(#pa-w-glow)">
    <animateMotion dur="2.6s" repeatCount="indefinite"
      path="M14,66 L30,66 L36,49 L44,29 L54,41 L62,51 L70,54 L78,52 L86,66
            L92,66 L98,49 L106,29 L116,41 L124,51 L132,54 L140,52 L148,66
            L154,66 L160,49 L168,29 L178,41 L186,51 L194,54 L202,52 L206,66"/>
  </circle>
</svg>""",
    }
    return f'<div class="page-art-wrap">{arts.get(art_id, arts["ecg"])}</div>'


# ── Navigation ────────────────────────────────────────────
pages = [
    ("dashboard", "Dashboard"),
    ("search",    "Knowledge Search"),
    ("reqs",      "Requirements"),
    ("scenarios", "Scenario Generator"),
    ("protocol",  "Protocol Generator"),
    ("impact",    "Impact Analysis"),
]

# FIX: st.container(key=...) gives this row a stable, unique CSS
# class (st-key-navbar) that we can target directly in styles.css.
# The previous [data-testid="stHorizontalBlock"]:first-of-type
# selector was fragile — it silently matched whichever horizontal
# block happened to render first in the DOM, which on inner pages
# could be a SUGGESTION PILL row instead of the navbar, stripping
# pills of their background/border and making them look like plain
# text links with no visible button shape.
with st.container(key="navbar"):

    logo_col, *nav_cols, theme_col, _ = st.columns(
        [2] + [1.15] * len(pages) + [1.0, 0.35]
    )

    with logo_col:

        st.markdown(
            '<div class="logo">🩺 ALTA<span class="logo-ai"> AI</span></div>',
            unsafe_allow_html=True
        )

    for col, (key, label) in zip(nav_cols, pages):

        with col:

            if st.session_state.page == key:

                st.markdown(
                    '<div class="nav-pip"></div>',
                    unsafe_allow_html=True
                )

            if st.button(
                label,
                key=f"nav_{key}",
                use_container_width=True
            ):

                st.session_state.page = key
                st.rerun()

    with theme_col:

        icon = (
            "☀️"
            if st.session_state.theme == "dark"
            else "🌙"
        )

        st.button(
            icon,
            key="theme_switch",
            use_container_width=True,
            on_click=toggle_theme
        )

st.markdown('<div class="nav-line"></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════════════
if st.session_state.page == "dashboard":

    req_c = load_requirements().shape[0]
    rsk_c = count_md("master_data/risks.md",      "Risk ID:")
    scr_c = count_md("master_data/screens.md",    "Screen ID:")
    par_c = count_md("master_data/parameters.md", "Parameter ID:")

    # Hero
    st.markdown(f"""
<div class="hero">
  <div class="hero-eyebrow">BD HemoSphere ALTA · QA Intelligence Platform</div>
  <h1 class="hero-h1">Test Intelligence<br>
    <span class="hero-accent">for Medical Devices</span></h1>
  <p class="hero-p">AI-powered requirement analysis, scenario generation, formal protocol
  creation and change impact assessment — purpose-built for the ALTA verification team.</p>
</div>""", unsafe_allow_html=True)

    # Single animated ECG strip
    st.markdown(DASHBOARD_ECG, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # KPI row
    k1, k2, k3, k4 = st.columns(4)
    for col, num, lbl_t, color, icon in [
        (k1, req_c, "Requirements",   "#00b4d8", "📋"),
        (k2, rsk_c, "Clinical Risks", "#e05252", "⚠️"),
        (k3, scr_c, "Device Screens", "#2ec4b6", "🖥️"),
        (k4, par_c, "Parameters",     "#f4a261", "📊"),
    ]:
        with col:
            st.markdown(f"""
<div class="kpi-card">
  <div class="kpi-icon-row">{icon}</div>
  <div class="kpi-number" style="color:{color}">{num}</div>
  <div class="kpi-label">{lbl_t}</div>
</div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    rule()
    st.markdown('<p class="section-label">PLATFORM MODULES</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    for col, icon, title, dest, desc, tag, color in [
        (m1, "🔍", "Knowledge Search",   "search",
         "Ask plain-English questions about requirements, risks, screens and parameters.",
         "1 API call", "#00b4d8"),
        (m2, "🧪", "Scenario Generator", "scenarios",
         "Generate 27 structured test scenarios across 7 types from any feature or requirement.",
         "1 API call", "#2ec4b6"),
        (m3, "📝", "Protocol Generator", "protocol",
         "Generate a complete formal validation protocol with test steps, traceability and Excel export.",
         "2 API calls", "#f4a261"),
    ]:
        with col:
            st.markdown(f"""
<div class="mod-card" style="border-top-color:{color}">
  <div class="mod-top"><span class="mod-icon">{icon}</span>
  <span class="mod-tag" style="color:{color}">{tag}</span></div>
  <div class="mod-title">{title}</div>
  <div class="mod-desc">{desc}</div>
</div>""", unsafe_allow_html=True)
            if st.button(f"Open {title} →", key=f"dash_{dest}",
                         use_container_width=True):
                st.session_state.page = dest
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    m4, m5, m6 = st.columns(3)
    for col, icon, title, dest, desc, tag, color in [
        (m4, "📊", "Impact Analysis",   "impact",
         "Deterministic impact scoring across requirements, risks, screens and parameters.",
         "1 API call", "#e05252"),
        (m5, "📋", "Requirements",      "reqs",
         "Live search across all ALTA requirements with full traceability and criteria.",
         "0 API calls", "#a78bfa"),
        (m6, "🛡️", "Risk & Screen Intel", None,
         "Screen names and risk descriptions from master data — zero hallucination.",
         "Built-in", "#64748b"),
    ]:
        with col:
            st.markdown(f"""
<div class="mod-card mod-card-dim" style="border-top-color:{color}">
  <div class="mod-top"><span class="mod-icon">{icon}</span>
  <span class="mod-tag" style="color:{color}">{tag}</span></div>
  <div class="mod-title">{title}</div>
  <div class="mod-desc">{desc}</div>
</div>""", unsafe_allow_html=True)
            if dest:
                if st.button(f"Open {title} →", key=f"dash2_{dest}",
                             use_container_width=True):
                    st.session_state.page = dest
                    st.rerun()

    rule()
    st.markdown('<p class="section-label">SYSTEM STATUS</p>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    for col, label, sub in [
        (s1, "Gemini API",     "Connected · Flash model"),
        (s2, "Knowledge Base", "85 requirements loaded"),
        (s3, "SQLite DB",      "alta_poc.db active"),
        (s4, "Master Data",    "Screens · Risks · Params"),
    ]:
        with col:
            st.markdown(f"""
<div class="status-card">
  <span class="status-dot-green"></span>
  <div><div class="status-name">{label}</div>
  <div class="status-sub">{sub}</div></div>
</div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# KNOWLEDGE SEARCH
# ═══════════════════════════════════════════════════════════
elif st.session_state.page == "search":

    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("""
<div class="page-hero">
  <div class="page-eyebrow">🔍 AI Knowledge Search</div>
  <h2 class="page-h2">Ask Anything About ALTA</h2>
  <p class="page-sub">Search across requirements, risks, screens, parameters
  and traceability. Results powered by RAG over the ALTA knowledge base.</p>
</div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(page_art("heart"), unsafe_allow_html=True)

    rule()

    lbl("YOUR QUESTION")
    synced_text_input("Your question", "qa_input",
                      placeholder="e.g.  What risks are associated with HPI?",
                      label_visibility="collapsed")

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([5, 1])
    with c1:
        qa_go = st.button("🔍  Search Knowledge Base", key="qa_go",
                          use_container_width=True)
    with c2:
        if st.button("Clear", key="qa_clr", use_container_width=True):
            stage_value("qa_input", "")
            st.session_state.qa_result = ""
            st.session_state.qa_last   = ""
            st.rerun()

    # Suggestions — populate textbox ONLY, never auto-search
    st.markdown('<p class="sugg-label">Suggestions — click to fill, then press Search:</p>',
                unsafe_allow_html=True)
    suggestion_pills([
        ("What is HPI?",        "What is HPI?"),
        ("CAI overview",        "Tell me about CAI"),
        ("HPI Risks",           "What risks are associated with HPI?"),
        ("Smart Wedge screens", "Which screens use Smart Wedge?"),
    ], widget_key="qa_input", group_id="qa_a")
    suggestion_pills([
        ("CAI parameters",      "What parameters are related to CAI?"),
        ("RSK-015",             "What is RSK-015?"),
        ("HPI vs MAP",          "What is the relationship between HPI and MAP?"),
        ("Alarm management",    "How does alarm management work in ALTA?"),
    ], widget_key="qa_input", group_id="qa_b")

    if qa_go:
        q = nz(st.session_state.qa_input)
        if not q:
            st.warning("Please enter a question.")
        else:
            st.session_state.qa_last = q
            with st.spinner("Searching ALTA knowledge base…"):
                # FIX: single call only — previously ask_alta(q) ran twice
                st.session_state.qa_result = ask_alta(q)

    if st.session_state.qa_result:
        rule()
        st.markdown(f'<p class="result-label">Result for: <em>{st.session_state.qa_last}</em></p>',
                    unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
        st.markdown(st.session_state.qa_result)
        st.markdown('</div>', unsafe_allow_html=True)
        st.download_button("⬇  Download Result", st.session_state.qa_result,
                           "alta_result.md", "text/markdown")


# ═══════════════════════════════════════════════════════════
# REQUIREMENTS  — truly live search via on_change
# ═══════════════════════════════════════════════════════════
elif st.session_state.page == "reqs":

    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("""
<div class="page-hero">
  <div class="page-eyebrow">📋 Requirement Repository</div>
  <h2 class="page-h2">Browse Requirements</h2>
  <p class="page-sub">Results update as you type. Select any requirement to view
  full traceability, verification methods and acceptance criteria.</p>
</div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(page_art("shield"), unsafe_allow_html=True)

    rule()
    df = load_requirements()

    lbl("SEARCH")

    c1, c2 = st.columns([12, 1])
    with c1:
        search = synced_text_input(
            "Search", "req_search",
            placeholder="Type a feature, ID or keyword — e.g. HPI, ANA-001",
            label_visibility="collapsed",
        )
    with c2:
        if st.button("✕", key="req_clear", use_container_width=True):
            stage_value("req_search", "")
            st.rerun()

    if nz(search):
        filtered = df[
            df["id"].str.contains(search, case=False, na=False)
            | df["title"].str.contains(search, case=False, na=False)
            | df["feature"].str.contains(search, case=False, na=False)
        ].copy()

        n = len(filtered)
        st.markdown(f'<p class="result-label">{n} result{"s" if n!=1 else ""} for '
                    f'<em>"{search}"</em></p>', unsafe_allow_html=True)

        if n == 0:
            st.warning("No requirements matched. Try a broader keyword.")
        else:
            left, right = st.columns([1, 2], gap="large")
            ids    = filtered["id"].tolist()
            titles = dict(zip(filtered["id"], filtered["title"]))

            if st.session_state.sel_req not in ids:
                st.session_state.sel_req = ids[0]

            with left:
                st.markdown('<div class="list-header">Matching Requirements</div>',
                            unsafe_allow_html=True)
                sel = st.radio("req_radio", ids,
                               index=ids.index(st.session_state.sel_req),
                               format_func=lambda r: f"{r}  ·  {titles.get(r,'')[:38]}",
                               label_visibility="collapsed")
                st.session_state.sel_req = sel

            with right:
                row = get_req(st.session_state.sel_req)
                if row:
                    pri_color = {
                        "Critical": "#e05252", "High": "#f4a261",
                        "Medium": "#00b4d8",   "Low":  "#2ec4b6",
                    }.get(nz(row[3]), "#64748b")

                    st.markdown(f"""
<div class="req-card">
  <div class="req-id-badge">{nz(row[0])}</div>
  <div class="req-title">{nz(row[1])}</div>
  <div class="req-chips">
    <span class="chip-badge">{nz(row[2])}</span>
    <span class="chip-badge">{nz(row[4])}</span>
    <span class="chip-badge" style="color:{pri_color};border-color:{pri_color}44;">{nz(row[3])}</span>
  </div>
</div>""", unsafe_allow_html=True)

                    t1, t2 = st.columns(2)
                    with t1:
                        lbl("SCREENS");  st.info(nz(row[5]) or "—")
                    with t2:
                        lbl("PARAMETERS"); st.info(nz(row[6]) or "—")
                    t3, t4 = st.columns(2)
                    with t3:
                        lbl("RISKS");    st.warning(nz(row[7]) or "—")
                    with t4:
                        lbl("DEPENDENCIES"); st.info(nz(row[8]) or "—")

                    st.markdown("<br>", unsafe_allow_html=True)
                    lbl("REQUIREMENT TEXT")
                    st.markdown(f'<div class="result-box">', unsafe_allow_html=True)
                    st.markdown(nz(row[9]))
                    st.markdown('</div>', unsafe_allow_html=True)

                    if len(row) > 10 and nz(row[10]):
                        lbl("VERIFICATION METHOD")
                        st.markdown(f'<div class="body-text">{nz(row[10])}</div>',
                                    unsafe_allow_html=True)
                    if len(row) > 11 and nz(row[11]):
                        lbl("ACCEPTANCE CRITERIA")
                        st.markdown(f'<div class="body-text">{nz(row[11])}</div>',
                                    unsafe_allow_html=True)
                    if len(row) > 12 and nz(row[12]):
                        lbl("IMPACT KEYWORDS")
                        kw = " ".join(f'<span class="kw-tag">{k.strip()}</span>'
                                      for k in nz(row[12]).split(",") if k.strip())
                        st.markdown(f'<div class="kw-row">{kw}</div>',
                                    unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="empty-state">
  <div class="empty-icon">📋</div>
  <div class="empty-title">Start typing to search</div>
  <div class="empty-hint">Try: HPI · Smart Wedge · CAI · ANA-001 · ALM-010</div>
</div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# SCENARIO GENERATOR
# ═══════════════════════════════════════════════════════════
elif st.session_state.page == "scenarios":

    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("""
<div class="page-hero">
  <div class="page-eyebrow">🧪 Scenario Generator</div>
  <h2 class="page-h2">Generate Test Scenarios</h2>
  <p class="page-sub">27 scenarios across 7 types — Positive, Negative, Boundary,
  Alarm, Workflow, Error Handling and Regression. Uses <strong>1 API call</strong>.</p>
</div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(page_art("wave"), unsafe_allow_html=True)

    rule()

    sc_col, info_col = st.columns([3, 1], gap="large")
    with sc_col:
        lbl("FEATURE / REQUIREMENT / CHANGE DESCRIPTION")

        synced_text_input("Feature, requirement or change description", "sc_input",
                          placeholder="e.g.  HPI, ANA-001, Smart Wedge",
                          label_visibility="collapsed")

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2 = st.columns([5, 1])
        with b1:
            sc_go = st.button("🧪  Generate Scenarios", key="sc_go",
                              use_container_width=True)
        with b2:
            if st.button("Clear", key="sc_clr", use_container_width=True):
                stage_value("sc_input", "")
                st.session_state.sc_result = ""
                st.rerun()

        # Small suggestion pills below — fill input only, no auto-generate
        st.markdown('<p class="sugg-label">Feature suggestions:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("HPI",         "HPI"),
            ("CAI",         "CAI"),
            ("Smart Wedge", "Smart Wedge"),
            ("Alarm Mgmt",  "Alarm Management"),
        ], widget_key="sc_input", group_id="sc_a")

        st.markdown('<p class="sugg-label">Requirement suggestions:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("ANA-001", "ANA-001"),
            ("ALM-010", "ALM-010"),
            ("WAV-006", "WAV-006"),
            ("LOG-009", "LOG-009"),
        ], widget_key="sc_input", group_id="sc_b")

        if sc_go:
            if not nz(st.session_state.sc_input):
                st.warning("Please enter a feature, requirement or change description.")
            else:
                with st.spinner("Generating 27 scenarios — 1 API call…"):
                    st.session_state.sc_result = generate_scenarios(
                        st.session_state.sc_input)

    with info_col:
        st.markdown("""
<div class="info-panel">
  <div class="info-panel-title">SCENARIO TYPES</div>
  <div class="info-item"><span class="dot-g"></span>Positive (5)</div>
  <div class="info-item"><span class="dot-r"></span>Negative (5)</div>
  <div class="info-item"><span class="dot-y"></span>Boundary (5)</div>
  <div class="info-item"><span class="dot-o"></span>Alarm (3)</div>
  <div class="info-item"><span class="dot-b"></span>Workflow (3)</div>
  <div class="info-item"><span class="dot-c"></span>Error Handling (3)</div>
  <div class="info-item"><span class="dot-p"></span>Regression (3)</div>
  <div class="info-total">27 total · 1 API call</div>
</div>""", unsafe_allow_html=True)

    if st.session_state.sc_result:
        rule()
        r1, r2 = st.columns([5, 1])
        with r1:
            st.markdown(f'<p class="result-label">Scenarios for: '
                        f'<em>{st.session_state.sc_input}</em></p>',
                        unsafe_allow_html=True)
        with r2:
            st.download_button("⬇ Download",
                               st.session_state.sc_result,
                               f"{st.session_state.sc_input}_scenarios.md",
                               "text/markdown", use_container_width=True)
        st.markdown(st.session_state.sc_result)


# ═══════════════════════════════════════════════════════════
# PROTOCOL GENERATOR
# ═══════════════════════════════════════════════════════════
elif st.session_state.page == "protocol":

    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("""
<div class="page-hero">
  <div class="page-eyebrow">📝 Protocol Generator</div>
  <h2 class="page-h2">Generate Validation Protocols</h2>
  <p class="page-sub">Complete formal validation protocol with test steps,
  traceability matrix, coverage summary and Excel export.
  Uses <strong>2 API calls</strong>.</p>
</div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(page_art("ecg"), unsafe_allow_html=True)

    rule()

    pr_col, info_col = st.columns([3, 1], gap="large")
    with pr_col:
        lbl("FEATURE / REQUIREMENT / CHANGE DESCRIPTION")

        synced_text_input("Feature, requirement or change description", "pr_input",
                          placeholder="e.g.  HPI, Smart Wedge, Alarm Management",
                          label_visibility="collapsed")

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2 = st.columns([5, 1])
        with b1:
            pr_go = st.button("📝  Generate Protocol", key="pr_go",
                              use_container_width=True)
        with b2:
            if st.button("Clear", key="pr_clr", use_container_width=True):
                stage_value("pr_input", "")
                st.session_state.pr_result = ""
                st.rerun()

        st.markdown('<p class="sugg-label">Feature suggestions:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("HPI",         "HPI"),
            ("CAI",         "CAI"),
            ("Smart Wedge", "Smart Wedge"),
            ("ClearSight",  "ClearSight Technology"),
        ], widget_key="pr_input", group_id="pr_a")

        st.markdown('<p class="sugg-label">System area suggestions:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("Alarm Mgmt",    "Alarm Management"),
            ("AFM Protocol",  "AFM"),
            ("Data Export",   "Data Export"),
            ("Power Recovery","Power Failure Recovery"),
        ], widget_key="pr_input", group_id="pr_b")

        if pr_go:
            if not nz(st.session_state.pr_input):
                st.warning("Please enter a feature, requirement or change description.")
            else:
                with st.spinner("Generating protocol — 2 API calls…"):
                    st.session_state.pr_result = generate_protocol(
                        st.session_state.pr_input)

    with info_col:
        st.markdown("""
<div class="info-panel">
  <div class="info-panel-title">PROTOCOL INCLUDES</div>
  <div class="info-item"><span class="tick">✓</span>Protocol Information</div>
  <div class="info-item"><span class="tick">✓</span>Test Case Summary</div>
  <div class="info-item"><span class="tick">✓</span>Detailed Test Steps</div>
  <div class="info-item"><span class="tick">✓</span>Requirement Traceability</div>
  <div class="info-item"><span class="tick">✓</span>Risk Traceability</div>
  <div class="info-item"><span class="tick">✓</span>Coverage Summary</div>
  <div class="info-item"><span class="tick">✓</span>Excel Export — 5 sheets</div>
  <div class="info-total">2 API calls per run</div>
</div>""", unsafe_allow_html=True)

    if st.session_state.pr_result:
        rule()
        r1, r2 = st.columns([5, 1])
        with r1:
            st.markdown(f'<p class="result-label">Protocol for: '
                        f'<em>{st.session_state.pr_input}</em></p>',
                        unsafe_allow_html=True)
        with r2:
            excel = protocol_to_excel(st.session_state.pr_result)
            st.download_button("⬇ Excel", excel,
                               f"{st.session_state.pr_input}_protocol.xlsx",
                               "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                               use_container_width=True)
        st.markdown(st.session_state.pr_result)


# ═══════════════════════════════════════════════════════════
# IMPACT ANALYSIS
# ═══════════════════════════════════════════════════════════
elif st.session_state.page == "impact":

    h1, h2 = st.columns([5, 1])
    with h1:
        st.markdown("""
<div class="page-hero">
  <div class="page-eyebrow">📊 Impact Analysis</div>
  <h2 class="page-h2">Analyse Change Impact</h2>
  <p class="page-sub">Deterministic impact scoring across requirements, screens,
  risks and parameters. Uses <strong>1 API call</strong>.</p>
</div>""", unsafe_allow_html=True)
    with h2:
        st.markdown(page_art("pulse"), unsafe_allow_html=True)

    rule()

    ia_col, info_col = st.columns([3, 1], gap="large")
    with ia_col:
        lbl("CHANGE DESCRIPTION")

        synced_text_input("Change description", "ia_input",
                          placeholder="e.g.  HPI alarm threshold changed from 85 to 90",
                          label_visibility="collapsed")

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2 = st.columns([5, 1])
        with b1:
            ia_go = st.button("📊  Analyse Impact", key="ia_go",
                              use_container_width=True)
        with b2:
            if st.button("Clear", key="ia_clr", use_container_width=True):
                stage_value("ia_input", "")
                st.session_state.ia_result = ""
                st.rerun()

        st.markdown('<p class="sugg-label">Threshold change examples:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("HPI 85→90",     "HPI alarm threshold changed from 85 to 90"),
            ("MAP lower limit","MAP lower alarm limit changed from 60 to 55 mmHg"),
            ("HPI refresh",   "HPI parameter refresh interval changed from 20s to 15s"),
            ("CAI window",    "CAI latency alert window extended from 500ms to 750ms"),
        ], widget_key="ia_input", group_id="ia_a")

        st.markdown('<p class="sugg-label">Requirement change examples:</p>',
                    unsafe_allow_html=True)
        suggestion_pills([
            ("ANA-001",        "ANA-001 acceptance criteria updated for HPI accuracy"),
            ("ALM-010",        "ALM-010 alarm prioritisation logic modified"),
            ("Smart Wedge",    "Smart Wedge over-inflation timer changed from 15s to 12s"),
            ("Sensor timeout", "Sensor disconnect detection response time changed"),
        ], widget_key="ia_input", group_id="ia_b")

        if ia_go:
            if not nz(st.session_state.ia_input):
                st.warning("Please enter a change description.")
            else:
                with st.spinner("Analysing impact — 1 API call…"):
                    st.session_state.ia_result = generate_impact_analysis(
                        st.session_state.ia_input)

    with info_col:
        st.markdown("""
<div class="info-panel">
  <div class="info-panel-title">ANALYSIS COVERS</div>
  <div class="info-item"><span class="tick">✓</span>Change Classification</div>
  <div class="info-item"><span class="tick">✓</span>Requirement Impact</div>
  <div class="info-item"><span class="tick">✓</span>Screen Impact</div>
  <div class="info-item"><span class="tick">✓</span>Risk Exposure</div>
  <div class="info-item"><span class="tick">✓</span>Parameter Impact</div>
  <div class="info-item"><span class="tick">✓</span>Verification Activities</div>
  <div class="info-item"><span class="tick">✓</span>Regression Scope</div>
  <div class="info-item"><span class="tick">✓</span>Deterministic Score</div>
  <div class="info-total">1 API call per analysis</div>
</div>""", unsafe_allow_html=True)

    if st.session_state.ia_result:
        rule()
        r1, r2 = st.columns([5, 1])
        with r1:
            st.markdown(f'<p class="result-label">Analysis for: '
                        f'<em>{st.session_state.ia_input}</em></p>',
                        unsafe_allow_html=True)
        with r2:
            st.download_button("⬇ Export", st.session_state.ia_result,
                               "impact_analysis.md", "text/markdown",
                               use_container_width=True)
        st.markdown(st.session_state.ia_result)