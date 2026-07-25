import streamlit as st
from data.careers import CAREERS

st.set_page_config(page_title="Free Resources", page_icon="📚", layout="wide")

if "career" not in st.session_state:
    st.warning("Please complete Career Assistant first.")
    st.stop()

career = st.session_state["career"]
career_data = CAREERS[career]

st.title("📚 Free Learning Resources")

st.write(f"Learn **{career}** using these free platforms.")

st.divider()

icons = {
    "Microsoft Learn": "📘",
    "freeCodeCamp": "🎥",
    "W3Schools": "💻"
}

for resource in career_data["resources"]:

    icon = icons.get(resource, "📖")

    with st.container(border=True):
        st.subheader(f"{icon} {resource}")

        st.write("✔ Free Learning Platform")
        st.write("✔ Beginner Friendly")
        st.write("✔ Recommended for Placements")

st.divider()

st.success("💡 Learn every day for at least 2 hours to stay consistent.")