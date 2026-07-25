import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("About CareerPilot AI")

st.markdown("""
## 🎯 Project Overview

CareerPilot AI is an AI-powered career guidance platform designed to help students
choose the right career path through personalized learning roadmaps, project
recommendations, interview preparation, certifications, and free learning resources.

The goal of this project is to make career planning simple, organized, and
accessible for every student.
""")

st.divider()

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
🤖 AI Career Guidance

🗺 Personalized Learning Roadmaps

💼 Real-world Projects

🎤 Interview Preparation

📚 Free Learning Resources
""")

with col2:
    st.success("""
🏆 Certification Suggestions

📈 Progress Dashboard

📄 Downloadable Roadmap

🎯 Career Tracking

💡 Easy-to-use Interface
""")

st.divider()

st.header("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("""
### Frontend

• Streamlit

• HTML

• CSS
""")

with tech2:
    st.info("""
### Backend

• Python

• JSON

• Session State
""")

with tech3:
    st.info("""
### Development

• VS Code

• GitHub

• Streamlit Cloud
""")

st.divider()

st.header("🚀 Future Scope")

st.markdown("""
- AI Chat Assistant
- User Login System
- Progress Synchronization
- Interactive Quizzes
- Resume Builder
- Job Recommendation System
- Skill Assessment
- Personalized Learning Analytics
""")

st.divider()

st.header("👩‍💻 Developer")

st.info("""
**Project Name:** CareerPilot AI

**Developed By:** Syed Juweriyah

**Branch:** Computer Science Engineering

**Purpose:** Final Year Academic Project
""")

st.divider()

st.markdown(
"""
<div style='text-align:center; color:gray;'>

<h3>CareerPilot AI</h3>

Helping students build successful careers through AI-powered guidance.

Version 2.0

</div>
""",
unsafe_allow_html=True
)