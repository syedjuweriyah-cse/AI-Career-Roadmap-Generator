import streamlit as st

st.set_page_config(
    page_title="Progress Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Progress Dashboard")

if "career" not in st.session_state:
    st.warning("Please generate your roadmap first.")
    st.stop()

career = st.session_state.get("career", "Not Selected")
name = st.session_state.get("name", "User")

st.success(f"Welcome back, {name}! Keep learning every day.")

st.write("")

# ==========================
# Overall Progress
# ==========================

st.subheader("🎯 Overall Career Progress")

progress = 25

st.progress(progress / 100)

st.write(f"### {progress}% Completed")

st.divider()

# ==========================
# Dashboard Cards
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📚 Topics", "8 / 40")

with col2:
    st.metric("💼 Projects", "1 / 5")

with col3:
    st.metric("🏆 Certificates", "0 / 3")

with col4:
    st.metric("🔥 Learning Streak", "7 Days")

st.divider()

# ==========================
# Career Summary
# ==========================

st.subheader("🎯 Career Summary")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
### Career Goal

**{career}**
""")

with col2:
    st.success("""
### Estimated Completion

**4 Months Left**
""")

st.divider()

# ==========================
# Skill Progress
# ==========================

st.subheader("📈 Skill Progress")

skills = {
    "Python": 70,
    "SQL": 55,
    "Projects": 20,
    "Interview": 15,
    "Communication": 60,
}

for skill, value in skills.items():
    st.write(f"**{skill}**")
    st.progress(value / 100)

st.divider()

# ==========================
# Motivation
# ==========================

st.success(
    "✨ Every topic you complete brings you one step closer to your dream career!"
)