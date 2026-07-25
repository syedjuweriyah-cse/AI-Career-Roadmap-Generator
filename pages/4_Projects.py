import streamlit as st
from data.careers import CAREERS

st.set_page_config(
    page_title="Projects",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Career Projects")

if "career" not in st.session_state:
    st.warning("Please generate your roadmap first.")
    st.stop()

career = st.session_state["career"]
career_data = CAREERS[career]

st.markdown(
f"""
Learn by building real-world projects for your career path.

### 🎯 Selected Career
**{career}**
"""
)

st.divider()

projects = career_data["projects"]

for i, project in enumerate(projects, start=1):

    with st.container():

        st.markdown(
        f"""
<div style="
background:#F8F9FC;
padding:20px;
border-radius:15px;
border-left:6px solid #6C63FF;
margin-bottom:20px;
box-shadow:0px 2px 8px rgba(0,0,0,0.08);
">

<h3>💼 Project {i}</h3>

<h2>{project}</h2>

<b>⭐ Difficulty:</b> Intermediate

<br>

<b>⏱ Estimated Time:</b> 2–5 Days

<br>

<b>🛠 Skills:</b> Python • SQL • Problem Solving

<br><br>

Build this project to strengthen your portfolio and improve your interview readiness.

</div>
""",
        unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)

        with col1:
            st.button(f"👀 View Details {i}", key=f"view_{i}")

        with col2:
            st.button(f"✅ Mark Complete {i}", key=f"complete_{i}")

st.divider()

st.success("✨ Complete these projects to build a strong portfolio.")