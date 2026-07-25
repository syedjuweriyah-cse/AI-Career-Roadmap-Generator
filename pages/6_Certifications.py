import streamlit as st
from data.careers import CAREERS

st.set_page_config(page_title="Certifications", page_icon="🏆", layout="wide")

if "career" not in st.session_state:
    st.warning("Please complete Career Assistant first.")
    st.stop()

career = st.session_state["career"]
career_data = CAREERS[career]

st.title("🏆 Recommended Certifications")

st.write(f"These certifications are recommended for becoming a **{career}**.")

st.divider()

for cert in career_data["certifications"]:

    with st.container(border=True):

        st.subheader(cert)

        st.write("✔ Industry Recognized")

        st.write("✔ Resume Booster")

        st.write("✔ Helps During Placements")

        st.button(f"Completed - {cert}", key=cert)

st.divider()

st.subheader("🎯 Certification Goal")

completed = st.slider(
    "How many certifications have you completed?",
    0,
    10,
    0
)

st.progress(completed / 10)

if completed >= 5:
    st.success("Excellent progress! Keep going.")
else:
    st.info("Try completing at least 2 certifications before placements.")