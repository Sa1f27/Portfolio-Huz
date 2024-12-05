#section/projects.py
import streamlit as st
from config import PROJECTS
import streamlit.components.v1 as components

def show_project_card(project):
    with st.container():
        cols = st.columns([2, 3])
        with cols[0]:
            st.image(project["image"], use_column_width=True)
        
        with cols[1]:
            st.subheader(project["title"])
            st.write(project["description"])
            
            # Tech stack as colored badges
            for tech in project["tech_stack"]:
                st.markdown(f"""
                    <span class="badge">{tech}</span>
                """, unsafe_allow_html=True)
            
            # Project links
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"[![GitHub]('images/github.png')]({project['github_link']})")
            with col2:
                # if project.get("demo_link"):
                #     st.markdown(f"[Live Demo]({project['demo_link']})")
                st.write("project")

def show_projects():
    st.header("🚀 Featured Projects")
    st.write("Here are some of my notable projects that showcase my skills and interests.")
    
    # Display featured projects in cards
    for project in PROJECTS:
        show_project_card(project)
        st.markdown("---")
    
    # GitHub Activity Calendar
    st.subheader("📊 GitHub Contributions")
    components.html(
        f"""
        <img src="https://ghchart.rshah.org/{PROJECTS[0]['github_link'].split('/')[-2]}" alt="2024 GitHub Contributions" style="width: 100%;"/>
        """,
        height=200
    )

if __name__ == "__main__":
    show_projects()