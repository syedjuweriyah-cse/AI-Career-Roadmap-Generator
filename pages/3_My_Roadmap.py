import streamlit as st
from data.careers import CAREERS

st.set_page_config(
    page_title="My Roadmap",
    page_icon="🗺️",
    layout="wide"
)

# -----------------------------
# Check User
# -----------------------------
if "career" not in st.session_state:
    st.warning("⚠ Please complete Career Assistant first.")
    st.stop()

career = st.session_state["career"]
name = st.session_state["name"]

career_data = CAREERS[career]

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(
    f"""
    <div style="
        background:linear-gradient(90deg,#6C63FF,#8A4FFF);
        padding:25px;
        border-radius:20px;
        color:white;
    ">
        <h1>{career_data['title']}</h1>
        <h3>Welcome back, {name}</h3>
        <p>{career_data['overview']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# CAREER STATS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Salary",
        career_data["salary"]
    )

with col2:
    st.metric(
        "⏳ Duration",
        career_data["estimated_duration"]
    )

with col3:
    st.metric(
        "📚 Phases",
        len(career_data["roadmap"])
    )

# Calculate Progress
total_topics = 0
completed_topics = 0

for phase in career_data["roadmap"]:
    total_topics += len(phase["topics"])

progress = 0

with col4:
    st.metric(
        "📈 Progress",
        f"{progress}%"
    )

st.progress(progress / 100)

st.divider()

st.header("🗺 Career Learning Journey")

# -----------------------------
# ROADMAP
# -----------------------------
for phase in career_data["roadmap"]:

    st.markdown(
        f"""
        <div style="
            background:#F8F9FF;
            padding:18px;
            border-left:8px solid #7C3AED;
            border-radius:15px;
            box-shadow:0 2px 10px rgba(0,0,0,.08);
            margin-bottom:10px;
        ">
        <h2>{phase['phase']}</h2>
        <b>⏱ Duration:</b> {phase['duration']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("🛠 Skills")

    skill_cols = st.columns(3)

    for i, skill in enumerate(phase["skills"]):
        skill_cols[i % 3].success(skill)

    st.write("")

    st.subheader("📚 Topics")

    cols = st.columns(2)

    half = (len(phase["topics"]) + 1) // 2

    with cols[0]:
        for topic in phase["topics"][:half]:

            checked = st.checkbox(
                topic,
                key=phase["phase"] + topic
            )

            if checked:
                completed_topics += 1

    with cols[1]:
        for topic in phase["topics"][half:]:

            checked = st.checkbox(
                topic,
                key=phase["phase"] + topic
            )

            if checked:
                completed_topics += 1

    st.subheader("📌 Sub Topics")

    chips = ""

    for sub in phase["subtopics"]:
        chips += f"`{sub}` "

    st.markdown(chips)

    st.divider()
    # -----------------------------
# UPDATE PROGRESS
# -----------------------------
if total_topics > 0:
    progress = int((completed_topics / total_topics) * 100)
else:
    progress = 0

st.header("📈 Overall Progress")

st.progress(progress / 100)

st.success(f"🎯 You have completed **{progress}%** of your roadmap.")

st.divider()

# -----------------------------
# PROJECTS
# -----------------------------
st.header("💼 Recommended Projects")

project_cols = st.columns(2)

for i, project in enumerate(career_data["projects"]):
    with project_cols[i % 2]:
        st.markdown(
            f"""
<div style="
background:#EEF2FF;
padding:18px;
border-radius:15px;
margin-bottom:15px;
border-left:6px solid #7C3AED;">
<h4>🎈 {project}</h4>
<p>Complete this project to strengthen your portfolio.</p>
</div>
""",
            unsafe_allow_html=True,
        )

st.divider()

# -----------------------------
# INTERVIEW QUESTIONS
# -----------------------------
st.header("🎤 Interview Preparation")

for i, question in enumerate(career_data["interview_questions"], start=1):
    with st.expander(f"Question {i}"):
        st.write(question)

st.divider()

# -----------------------------
# CERTIFICATIONS
# -----------------------------
st.header("🏆 Recommended Certifications")

cert_cols = st.columns(2)

for i, cert in enumerate(career_data["certifications"]):
    with cert_cols[i % 2]:
        st.success(f"📜 {cert}")

st.divider()

# -----------------------------
# FREE RESOURCES
# -----------------------------
st.header("📚 Free Learning Resources")

for resource in career_data["resources"]:
    st.markdown(f"- 🔗 {resource}")

st.divider()

# -----------------------------
# NEXT STEP
# -----------------------------
st.info(
    "✅ Complete all phases, build the recommended projects, "
    "practice interview questions, and earn certifications "
    "to become job-ready."
)