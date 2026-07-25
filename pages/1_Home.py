import streamlit as st
from utils.storage import load_profile

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

profile = load_profile()

name = profile.get("name", "Guest")
career = profile.get("career", "Not Selected")
education = profile.get("education", "-")
study_hours = profile.get("study_hours", "-")
goal = profile.get("goal", "-")

st.markdown("""
<div style="background:linear-gradient(90deg,#6C63FF,#4F46E5);
padding:35px;
border-radius:20px;
text-align:center;
color:white;">
<h1>CareerPilot AI</h1>
<h2>Smart Career Guidance Platform</h2>
<p>Create your personalized roadmap and become job ready.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns([1,2])

with col1:

    st.markdown("## 👤 Your Profile")

    st.info(f"""
**Name:** {name}

**Career:** {career}

**Education:** {education}

**Study Hours:** {study_hours}

**Goal:** {goal}
""")

with col2:

    st.markdown("## 📊 Platform Statistics")

    a,b,c,d = st.columns(4)

    a.metric("Career Paths","10+")
    b.metric("Projects","100+")
    c.metric("Interview Qs","500+")
    d.metric("Certificates","50+")

st.write("")

st.markdown("## ✨ Features")

c1,c2 = st.columns(2)

with c1:
    st.success("🗺 Personalized Learning Roadmaps")
    st.success("💼 Industry Level Projects")
    st.success("📚 Free Learning Resources")
    st.success("📈 Progress Tracking")

with c2:
    st.success("🎤 Interview Preparation")
    st.success("🏆 Certifications")
    st.success("📄 PDF Download")
    st.success("🤖 Career Guidance")

st.write("")

st.markdown("---")

st.markdown("## ✨ Quick Start")

st.markdown("""
1. Open **Career Assistant**
2. Fill your details
3. Generate your roadmap
4. Complete projects
5. Practice interview questions
6. Download your roadmap PDF
""")

st.success("🎉 Welcome back! Continue your learning journey.")