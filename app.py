
import time
import streamlit as st

from llm import ask_llm, DETAIL_LEVELS
from prompt_templates import TECHNIQUES, build_prompt

st.set_page_config(
    page_title="Prompt AI Master",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

TECHNIQUE_COLORS = {
    "Zero-Shot": "#A78BFA",
    "One-Shot": "#22D3EE",
    "Few-Shot": "#34D399",
    "Chain of Thought (CoT)": "#FBBF24",
    "Tree of Thought (ToT)": "#F472B6",
}

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #080B16;
    --panel: #111629;
    --border: #29324C;
    --purple: #A78BFA;
    --cyan: #22D3EE;
    --text: #F1F5F9;
    --muted: #98A4BD;
}

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 10% 0%, #211744 0%, transparent 38%),
        radial-gradient(ellipse at 95% 20%, #102C42 0%, transparent 30%),
        var(--bg);
    color: var(--text);
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101326, #090D1B) !important;
    border-right: 1px solid #29324C;
}

[data-testid="stSidebar"] > div:first-child {
    background: transparent;
}

[data-testid="stSidebar"] * {
    color: #E2E8F0;
}

[data-testid="stSidebar"] hr {
    border-color: #29324C;
}

.brand-logo {
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    background: linear-gradient(135deg, #8B5CF6, #4338CA 55%, #0891B2);
    box-shadow: 0 8px 35px #7C3AED35;
    color: white;
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 16px;
}

.brand-name {
    font-size: 25px;
    font-weight: 900;
    letter-spacing: -1px;
    color: #FFFFFF;
    line-height: 1.2;
}

.brand-name span {
    color: #A78BFA;
}

.brand-caption {
    color: #8E9AB5;
    font-size: 11px;
    margin-top: 8px;
    letter-spacing: 1px;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 36px;
    border: 1px solid #39345F;
    border-radius: 25px;
    background: linear-gradient(
        115deg,
        #201747D9,
        #151D35E8 55%,
        #103047B8
    );
    margin-bottom: 26px;
    box-shadow: 0 15px 50px #00000020;
}

.eyebrow {
    color: #67E8F9;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 12px;
}

.hero h1 {
    font-size: clamp(32px, 4vw, 48px);
    line-height: 1.12;
    letter-spacing: -2px;
    font-weight: 900;
    color: #FFFFFF;
    margin: 0 0 14px 0;
}

.hero p {
    color: #B8C4DB;
    font-size: 15px;
    line-height: 1.8;
    max-width: 650px;
}

.section-title {
    font-size: 21px;
    font-weight: 800;
    color: #F8FAFC;
    margin: 26px 0 5px;
}

.section-subtitle {
    color: #98A4BD;
    font-size: 13px;
    margin-bottom: 18px;
}

.metric-card {
    background: linear-gradient(145deg, #171D34, #101629);
    border: 1px solid #303A58;
    border-radius: 18px;
    padding: 20px;
    min-height: 120px;
    transition: 0.2s ease;
}

.metric-number {
    color: #C4B5FD;
    font-size: 31px;
    font-weight: 900;
    letter-spacing: -1px;
}

.metric-label {
    color: #A7B2C9;
    font-size: 12px;
    margin-top: 8px;
}

.metric-top {
    color: #67E8F9;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.result-head {
    background: linear-gradient(90deg, #272047, #18263C);
    color: #FFFFFF;
    padding: 15px 18px;
    border: 1px solid #343C5C;
    border-bottom: none;
    border-radius: 14px 14px 0 0;
    font-weight: 800;
}

.result-body {
    background: #101629;
    border: 1px solid #343C5C;
    border-radius: 0 0 14px 14px;
    padding: 20px;
    margin-bottom: 22px;
    color: #E2E8F0;
}

.stTextArea textarea,
.stTextInput input {
    background: #101629 !important;
    color: #F8FAFC !important;
    border: 1px solid #35405F !important;
    border-radius: 13px !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: #A78BFA !important;
    box-shadow: 0 0 0 1px #A78BFA !important;
}

.stSelectbox [data-baseweb="select"] > div,
.stMultiSelect [data-baseweb="select"] > div {
    background: #141A30;
    border-color: #35405F;
    border-radius: 11px;
}

.stButton > button {
    border: 1px solid #3B4261;
    border-radius: 12px;
    background: #171D34;
    color: #F8FAFC;
    font-weight: 700;
    min-height: 44px;
    transition: 0.2s ease;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #7C3AED, #5B4DE8, #087EA4);
    border: none;
    color: white;
    font-weight: 800;
    box-shadow: 0 7px 24px #6D28D930;
}

.stButton > button:hover {
    border-color: #A78BFA;
    color: white;
    transform: translateY(-1px);
}

div[data-testid="stMetric"] {
    background: #141A30;
    border: 1px solid #303A58;
    border-radius: 15px;
    padding: 18px;
}

.stRadio label, .stCheckbox label {
    color: #DCE5F5 !important;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.footer {
    text-align: center;
    color: #74819C;
    font-size: 12px;
    border-top: 1px solid #252D45;
    padding-top: 22px;
    margin-top: 45px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("""
    <div style="padding:12px 4px 20px">
        <div class="brand-logo">✦</div>
        <div class="brand-name">PROMPT AI<br><span>MASTER</span></div>
        <div class="brand-caption">YOUR AI PROMPT WORKSPACE</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### ⚙️ Model Settings")

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    detail = st.selectbox(
        "Response Detail",
        list(DETAIL_LEVELS.keys()),
        index=min(2, len(DETAIL_LEVELS) - 1)
    )

    show_prompt = st.checkbox(
        "Show generated prompt",
        value=False
    )

    st.divider()
    st.markdown("### ✧ Prompt Strategies")

    st.markdown("""
    <div style="background:#171B31;border:1px solid #303653;
                padding:13px;border-radius:12px;margin-bottom:9px">
        <b style="color:#C4B5FD">01 · Zero-Shot</b><br>
        <small>Start without examples</small>
    </div>
    <div style="background:#171B31;border:1px solid #303653;
                padding:13px;border-radius:12px;margin-bottom:9px">
        <b style="color:#67E8F9">02 · One-Shot</b><br>
        <small>Learn from one example</small>
    </div>
    <div style="background:#171B31;border:1px solid #303653;
                padding:13px;border-radius:12px;margin-bottom:9px">
        <b style="color:#6EE7B7">03 · Few-Shot</b><br>
        <small>Use multiple examples</small>
    </div>
    <div style="background:#171B31;border:1px solid #303653;
                padding:13px;border-radius:12px;margin-bottom:9px">
        <b style="color:#FCD34D">04 · Chain of Thought</b><br>
        <small>Organize the task into stages</small>
    </div>
    <div style="background:#171B31;border:1px solid #303653;
                padding:13px;border-radius:12px">
        <b style="color:#F9A8D4">05 · Tree of Thought</b><br>
        <small>Explore different approaches</small>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.caption("Powered by your configured AI provider")


# ---------------- MAIN DASHBOARD ----------------

st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ INTELLIGENT PROMPT ENGINEERING</div>
    <h1>Think Better.<br>Prompt Smarter.</h1>
    <p>
        Welcome to Prompt AI Master — your creative AI workspace.
        Build powerful prompts, test different strategies, and
        compare AI-generated responses in one place.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- METRIC CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

metrics = [
    (f"{len(TECHNIQUES):02d}", "AVAILABLE STRATEGIES", "PROMPT TOOLS"),
    ("02", "ANALYSIS MODES", "WORKFLOW"),
    ("01", "AI WORKSPACE", "GENERATION"),
    (f"{temperature:.1f}", "CREATIVITY LEVEL", "CONFIGURATION")
]

for col, (number, label, top) in zip(
    [col1, col2, col3, col4], metrics
):
    with col:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top">{top}</div>
            <div class="metric-number">{number}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


# ---------------- TASK INPUT ----------------

st.markdown(
    '<div class="section-title">Create Your Prompt</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Describe your task and let AI help you explore the best approach.</div>',
    unsafe_allow_html=True
)

task = st.text_area(
    "Task",
    height=150,
    placeholder="Example: Explain Artificial Intelligence to a beginner...",
    label_visibility="collapsed"
)


# ---------------- ANALYSIS SETTINGS ----------------

col1, col2 = st.columns([1, 1.3])

with col1:
    mode = st.radio(
        "Analysis Mode",
        ["Single Strategy", "Compare Strategies"],
        horizontal=True
    )

with col2:
    if mode == "Single Strategy":
        selected = st.selectbox(
            "Prompt Strategy",
            list(TECHNIQUES.keys())
        )
        selected_techniques = [selected]
    else:
        defaults = [
            x for x in [
                "Zero-Shot",
                "Few-Shot",
                "Chain of Thought (CoT)"
            ]
            if x in TECHNIQUES
        ]

        selected_techniques = st.multiselect(
            "Select Strategies",
            list(TECHNIQUES.keys()),
            default=defaults
        )


st.markdown("")
run_button = st.button(
    "✦  Run Prompt Analysis",
    type="primary",
    use_container_width=True
)


# ---------------- GENERATE RESPONSE ----------------

def render_response(technique):
    generated_prompt = build_prompt(technique, task)

    if show_prompt:
        st.markdown("**Generated Prompt**")
        st.code(generated_prompt, language="text")

    start_time = time.time()

    try:
        with st.spinner(f"Generating response using {technique}..."):
            answer = ask_llm(
                generated_prompt,
                detail=detail,
                temperature=temperature
            )

        elapsed = time.time() - start_time
        color = TECHNIQUE_COLORS.get(technique, "#A78BFA")

        st.markdown(
            f"""
            <div class="result-head"
                 style="border-left:5px solid {color}">
                ✦ &nbsp; {technique}
            </div>
            <div class="result-body">
            """,
            unsafe_allow_html=True
        )

        st.markdown(answer)
        st.markdown("</div>", unsafe_allow_html=True)

        st.caption(
            f"Strategy: {technique}  ·  "
            f"Detail: {detail}  ·  "
            f"Generation time: {elapsed:.2f} seconds"
        )

    except Exception as e:
        st.error(f"Unable to generate response: {e}")


# ---------------- RUN ANALYSIS ----------------

if run_button:
    if not task.strip():
        st.warning("Please enter a task first.")

    elif not selected_techniques:
        st.warning("Please select at least one strategy.")

    else:
        st.markdown(
            '<div class="section-title">AI Results</div>',
            unsafe_allow_html=True
        )

        if mode == "Single Strategy":
            render_response(selected_techniques[0])

        else:
            columns = st.columns(len(selected_techniques))

            for column, technique in zip(
                columns, selected_techniques
            ):
                with column:
                    render_response(technique)


# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
    ✦ PROMPT AI MASTER &nbsp; | &nbsp;
    Intelligent Prompt Engineering Workspace
</div>
""", unsafe_allow_html=True)
