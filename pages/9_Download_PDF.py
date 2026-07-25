import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from data.careers import CAREERS

st.set_page_config(
    page_title="Download PDF",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Download Professional Career Roadmap")

if "career" not in st.session_state:
    st.warning("⚠ Please generate a roadmap first.")
    st.stop()

career = st.session_state["career"]
name = st.session_state["name"]

career_data = CAREERS[career]


def create_pdf():

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b><font size=22>CareerPilot AI</font></b>", styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {name}", styles["Normal"]))
    story.append(Paragraph(f"<b>Career:</b> {career}", styles["Normal"]))
    story.append(Paragraph(f"<b>Duration:</b> {career_data['estimated_duration']}", styles["Normal"]))
    story.append(Paragraph(f"<b>Salary:</b> {career_data['salary']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Career Overview</b>", styles["Heading2"]))
    story.append(Paragraph(career_data["overview"], styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Learning Roadmap</b>", styles["Heading1"]))

    for phase in career_data["roadmap"]:

        story.append(Paragraph(f"<b>{phase['phase']}</b>", styles["Heading2"]))

        story.append(Paragraph(f"Duration : {phase['duration']}", styles["Normal"]))

        story.append(Paragraph("<b>Skills</b>", styles["Heading3"]))

        for skill in phase["skills"]:
            story.append(Paragraph(f"• {skill}", styles["Normal"]))

        story.append(Paragraph("<b>Topics</b>", styles["Heading3"]))

        for topic in phase["topics"]:
            story.append(Paragraph(f"• {topic}", styles["Normal"]))

        story.append(Paragraph("<b>Sub Topics</b>", styles["Heading3"]))

        for sub in phase["subtopics"]:
            story.append(Paragraph(f"• {sub}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Projects</b>", styles["Heading2"]))

    for project in career_data["projects"]:
        story.append(Paragraph(f"• {project}", styles["Normal"]))

    story.append(Paragraph("<b>Interview Questions</b>", styles["Heading2"]))

    for q in career_data["interview_questions"]:
        story.append(Paragraph(f"• {q}", styles["Normal"]))

    story.append(Paragraph("<b>Certifications</b>", styles["Heading2"]))

    for cert in career_data["certifications"]:
        story.append(Paragraph(f"• {cert}", styles["Normal"]))

    story.append(Paragraph("<b>Resources</b>", styles["Heading2"]))

    for resource in career_data["resources"]:
        story.append(Paragraph(f"• {resource}", styles["Normal"]))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf


pdf = create_pdf()

st.download_button(
    label="📥 Download Professional PDF",
    data=pdf,
    file_name=f"{career}_Roadmap.pdf",
    mime="application/pdf"
)

st.success("✅ Your professional roadmap PDF is ready!")