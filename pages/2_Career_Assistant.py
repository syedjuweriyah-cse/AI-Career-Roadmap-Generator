import streamlit as st
from utils.storage import save_profile, load_profile
from data.careers import CAREERS

st.set_page_config(page_title="Career Assistant", page_icon="🤖")

# --------------------------
# Load Saved Profile
# --------------------------
profile = load_profile()

career_options = list(CAREERS.keys())

education_options = [
    "B.Tech",
    "B.Sc",
    "MCA",
    "M.Tech",
    "Other"
]

goal_options = [
    "Get an Internship",
    "Get a Job",
    "Upskill",
    "Career Switch"
]

st.title("🤖 Career Assistant")
st.write("Fill in your details to generate your personalized learning roadmap.")

name = st.text_input(
    "👤 Your Name",
    value=profile.get("name", "")
)

career = st.selectbox(
    "🎯 Select Your Career",
    career_options,
    index=career_options.index(profile.get("career", "Data Analyst"))
    if profile.get("career", "Data Analyst") in career_options
    else 0
)

education = st.selectbox(
    "🎓 Education",
    education_options,
    index=education_options.index(profile.get("education", "B.Tech"))
    if profile.get("education", "B.Tech") in education_options
    else 0
)

study_hours = st.slider(
    "📚 Study Hours Per Day",
    1,
    8,
    profile.get("study_hours", 2)
)

goal = st.selectbox(
    "🎯 Your Goal",
    goal_options,
    index=goal_options.index(profile.get("goal", "Get a Job"))
    if profile.get("goal", "Get a Job") in goal_options
    else 0
)

if st.button("🚀 Generate My Roadmap"):

    st.session_state["name"] = name
    st.session_state["career"] = career
    st.session_state["education"] = education
    st.session_state["study_hours"] = study_hours
    st.session_state["goal"] = goal

    save_profile({
        "name": name,
        "career": career,
        "education": education,
        "study_hours": study_hours,
        "goal": goal
    })

    st.success("✅ Your information has been saved!")

    st.info("➡️ Open 'My Roadmap' from the sidebar.")