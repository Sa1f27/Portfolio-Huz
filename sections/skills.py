#section/skills.py
import streamlit as st
from config import SKILLS

def create_skill_progress(skill, proficiency):
    """Display a skill with a progress bar for proficiency."""
    st.markdown(f"**{skill}**")
    st.progress(proficiency)

def show_skills():
    st.header("⚡ Skills & Expertise")
    
    # 1. Programming Languages
    st.subheader("Programming Languages")
    cols = st.columns(2)
    for idx, lang in enumerate(SKILLS["programming_languages"]):
        with cols[idx % 2]:
            create_skill_progress(lang, 85 - (idx * 5))
    
    # 2. Technologies & Frameworks
    st.subheader("Technologies & Frameworks")
    tech_categories = [
        ("Machine Learning Frameworks", "machine_learning_frameworks"),
        ("Cloud Technologies", "cloud_technologies"),
        ("Data Management", "data_management"),
        ("Data Visualization", "data_visualization")
    ]
    
    for category_name, key in tech_categories:
        st.markdown(f"### {category_name}")
        cols = st.columns(2)
        for idx, tech in enumerate(SKILLS.get(key, [])):
            with cols[idx % 2]:
                create_skill_progress(tech, 80 - (idx * 5))
    
    # 3. Tools & Platforms
    st.subheader("Tools & Platforms")
    cols = st.columns(3)
    for idx, tool in enumerate(SKILLS["tools"]):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center;">
                    <img src="images/{tool.lower().replace(' ', '_')}.png" alt="{tool}" width="30" style="margin-right: 10px;"/>
                    <span>{tool}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # 4. Soft Skills
    st.subheader("Soft Skills")
    for skill in SKILLS["soft_skills"]:
        st.markdown(f"- {skill}")

if __name__ == "__main__":
    show_skills()