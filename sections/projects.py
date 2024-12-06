import streamlit as st
from config import PROJECTS
from config import SKILLS

# Custom CSS for badges and styling
st.markdown(
    """
    <style>
    .badge {
        display: inline-block;
        padding: 5px 10px;
        margin: 5px 3px;
        background-color: #f0f0f0;
        color: #333;
        border-radius: 5px;
        font-size: 14px;
    }
    .project-card {
        padding: 15px;
        border-radius: 10px;
        background: #f9f9f9;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .project-title {
        color: #333;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#============projects================
def show_project_card(project):
    with st.container():
        # Static fallback for testing
        try:
            st.image("images/kids.png", use_container_width=True)
        except Exception as e:
            st.error(f"Failed to load static image: {e}")


        
        st.markdown(f"<h3 class='project-title'>{project['title']}</h3>", unsafe_allow_html=True)
        st.write(project["description"])

        # Tech Stack Badges
        tech_stack_html = " ".join(f"<span class='badge'>{tech}</span>" for tech in project["tech_stack"])
        st.markdown(tech_stack_html, unsafe_allow_html=True)

        # Project Links
        col1, col2 = st.columns(2)
        with col1:
            if "github_link" in project:
                st.markdown(
                    f"[![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github&logoColor=white)]({project['github_link']})",
                    unsafe_allow_html=True,
                )
        with col2:
            if "live_link" in project:
                st.markdown(
                    f"[![Live Demo](https://img.shields.io/badge/-Live%20Demo-green?style=flat-square&logo=heroku&logoColor=white)]({project['live_link']})",
                    unsafe_allow_html=True,
                )

def show_projects():
    st.header("🚀 Featured Projects")
    st.write("Explore some of my notable projects that demonstrate my skills and expertise.")
    
    for project in PROJECTS:
        with st.container():
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            show_project_card(project)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("---")  # Separator between projects

#===========skills============
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
    st.markdown("---")

if __name__ == "__main__":
    show_projects()
    show_skills()
    
