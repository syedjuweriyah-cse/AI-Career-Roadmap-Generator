import streamlit as st
from utils.storage import load_profile

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

profile = load_profile()

if profile:
    for key, value in profile.items():
        if key not in st.session_state:
            st.session_state[key] = value

# ---------------- Sidebar ---------------- #

st.sidebar.title(" CareerPilot AI")
st.sidebar.image("assets/logo.png", width=180)

st.sidebar.markdown(
"""
<h2 style='text-align:center;color:#6C63FF;margin-bottom:5px;'>
CareerPilot AI
</h2>

<p style='text-align:center;color:gray;font-size:14px;'>
AI Career Guidance Platform
</p>
""",
unsafe_allow_html=True
)
if profile:
    st.sidebar.success(f"👋 Welcome, {profile.get('name','User')}")
    st.sidebar.write(f"🎯 {profile.get('career','')}")
    st.sidebar.progress(0.25)
    st.sidebar.caption("Career Progress : 25%")
else:
    st.sidebar.info("Generate your roadmap first.")

st.sidebar.divider()

st.sidebar.markdown("### 📌 Features")

st.sidebar.write("🤖 AI Career Guidance")
st.sidebar.write("🗺 Personalized Roadmaps")
st.sidebar.write("💼 Projects")
st.sidebar.write("🎤 Interview Questions")
st.sidebar.write("🏆 Certifications")
st.sidebar.write("📄 Professional PDF")

st.sidebar.divider()

st.sidebar.caption("CareerPilot AI Version 2.0")

# ---------------- Hero ---------------- #

st.markdown(
"""
<div style="
background:linear-gradient(90deg,#6C63FF,#8A4FFF);
padding:40px;
border-radius:20px;
color:white;
text-align:center;
">

<h1>CareerPilot AI</h1>

<h3>Smart Career Guidance Platform</h3>

<p>
Personalized Learning Roadmaps • Projects • Certifications • Interview Preparation
</p>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- Statistics ---------------- #

st.markdown("## 📊 Platform Statistics")

col1,col2,col3,col4=st.columns(4)

col1.metric("🎯 Career Paths","10")
col2.metric("📚 Topics","500+")
col3.metric("💼 Projects","50+")
col4.metric("🏆 Certifications","100+")

st.divider()

# ---------------- Why Choose ---------------- #

st.header("✨ Why Choose CareerPilot AI?")

c1,c2,c3=st.columns(3)

with c1:
    st.info("""
### 🤖 AI Guidance

Get personalized career guidance based on your goals.
""")

with c2:
    st.success("""
### 🗺 Smart Roadmaps

Follow structured learning paths created for every career.
""")

with c3:
    st.warning("""
### 💼 Placement Ready

Projects, interview preparation and certifications.
""")

st.divider()

# ---------------- Careers ---------------- #

st.header("💼Available Career Paths")

career_cols=st.columns(2)

careers=[
"📊 Data Analyst",
"🤖 AI Engineer",
"🐍 Python Developer",
"🌐 Full Stack Developer",
"☁ Cloud Engineer",
"🛡 Cybersecurity Engineer",
"📈 Data Scientist",
"⚙ DevOps Engineer",
"🌐 Network Engineer",
"🧪 Software Test Engineer"
]

for i,career in enumerate(careers):
    with career_cols[i%2]:
        st.success(career)

st.divider()

# ---------------- Steps ---------------- #

st.header("📍 How It Works")

step1,step2,step3=st.columns(3)

step1.success("""
### 1️⃣ Select Career

Choose your dream career.
""")

step2.success("""
### 2️⃣ Generate Roadmap

AI creates your learning path.
""")

step3.success("""
### 3️⃣ Become Job Ready

Complete projects and prepare for interviews.
""")

st.divider()

# ---------------- Footer ---------------- #

st.success("✨ Start your journey using the **Career Assistant** page from the sidebar.")

st.caption("© 2026 CareerPilot AI | Built using Python & Streamlit")