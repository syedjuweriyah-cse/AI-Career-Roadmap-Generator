import streamlit as st
from data.careers import CAREERS

st.set_page_config(page_title="Interview Hub", page_icon="🎤", layout="wide")

if "career" not in st.session_state:
    st.warning("Please complete Career Assistant first.")
    st.stop()

career = st.session_state["career"]
career_data = CAREERS[career]

st.title("🎤 Interview Hub")

st.write("Practice the most commonly asked interview questions.")

st.divider()

questions = career_data["interview_questions"]

for i, question in enumerate(questions, start=1):

    with st.expander(f"Question {i}"):

        st.markdown(f"### ❓ {question}")

        st.text_area(
            "Write your answer here",
            height=120,
            key=f"answer_{i}"
        )

        st.button("Mark as Practiced", key=f"practice_{i}")

st.divider()

st.subheader("💡 Interview Tips")

tips = [
    "Dress professionally.",
    "Maintain eye contact.",
    "Explain your projects confidently.",
    "Practice Python and SQL basics.",
    "Communicate clearly and confidently."
]

for tip in tips:
    st.success(tip)

st.balloons()