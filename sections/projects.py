import streamlit as st
from config import PROJECTS, SKILLS

class PortfolioApp:
    # Load custom CSS
    def local_css(file_name):
        with open(file_name, "r") as f:  # Explicitly use "r" mode for readability
            css_content = f.read()
            # Apply the CSS
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # Call the function with the correct file path
    local_css("style/style.css") 

    def get_icon_for_skill(self, skill_name):
        icon_mapping = {
            'Python': 'fab fa-python',
            'JavaScript': 'fab fa-js',
            'Java': 'fab fa-java',
            'React': 'fab fa-react',
            'AWS': 'fab fa-aws',
            'Docker': 'fab fa-docker',
            'Git': 'fab fa-git-alt',
            'HTML': 'fab fa-html5',
            'CSS': 'fab fa-css3',
            'Node.js': 'fab fa-node',
            'Machine Learning': 'fas fa-brain',
            'Deep Learning': 'fas fa-network-wired',
            'Data Science': 'fas fa-chart-line',
            'default': 'fas fa-code'
        }
        return icon_mapping.get(skill_name, icon_mapping['default'])

    def show_project_card(self, project):
        # Display project title
        st.markdown(f"<h3>{project['title']}</h3>", unsafe_allow_html=True)

        # Display project image using st.image
        if project.get('image'):
            st.image(project['image'], use_container_width=True)

        # Display project description
        st.markdown(f"<p>{project['description']}</p>", unsafe_allow_html=True)

        # Display tech stack
        st.markdown(f"""
            <div class="tech-stack">
                {''.join([f'<span class="skill-badge"><i class="{self.get_icon_for_skill(tech)} skill-icon"></i>{tech}</span>' for tech in project['tech_stack']])}
            </div>
        """, unsafe_allow_html=True)

        # Display project links (if any)
        st.markdown(f"""
            <div class="project-links">
                {'<a href="' + project.get('github_link', '#') + '" class="project-link" target="_blank"><i class="fab fa-github"></i> GitHub</a>' if project.get('github_link') else ''}
            </div>
        """, unsafe_allow_html=True)

    def get_icon_for_skill(self, skill_name):
        icon_mapping = {
            'Python': 'fab fa-python',
            'JavaScript': 'fab fa-js',
            'Java': 'fab fa-java',
            'React': 'fab fa-react',
            'AWS': 'fab fa-aws',
            'Docker': 'fab fa-docker',
            'Git': 'fab fa-git-alt',
            'HTML': 'fab fa-html5',
            'CSS': 'fab fa-css3',
            'Node.js': 'fab fa-node',
            'Machine Learning': 'fas fa-brain',
            'Deep Learning': 'fas fa-network-wired',
            'Data Science': 'fas fa-chart-line',
            'default': 'fas fa-code'
        }
        return icon_mapping.get(skill_name, icon_mapping['default'])

    def show_skills_section(self, title, skills):
        st.markdown(f'<h3 class="section-header">{title}</h3>', unsafe_allow_html=True)
        st.markdown('<div class="skills-grid">', unsafe_allow_html=True)
        for skill in skills:
            st.markdown(f"""
                <div class="skill-badge">
                    <i class="{self.get_icon_for_skill(skill)} skill-icon" style="margin-right: 8px;"></i>
                    {skill}
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def run(self):
        # Main container with padding
        st.markdown('<div style="padding: 2rem 0;">', unsafe_allow_html=True)

        # Row 1: Projects side by side
        st.header("Featured Projects")
        project_cols = st.columns(len(PROJECTS))  # Create a column for each project
        
        for col, project in zip(project_cols, PROJECTS):
            with col:
                self.show_project_card(project)  # Display project card

        # Separator
        st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

        # Row 2: Skills side by side
        st.header("Skills & Expertise")
        skill_categories = {
            "Programming Languages": SKILLS.get('programming_languages', []),
            "Machine Learning": SKILLS.get('machine_learning_frameworks', []),
            "Cloud Technologies": SKILLS.get('cloud_technologies', []),
            "Data Management": SKILLS.get('data_management', []),
            "Data Visualization": SKILLS.get('data_visualization', []),
            "Tools & Platforms": SKILLS.get('tools', []),
        }

        skill_cols = st.columns(len(skill_categories))  # Create a column for each skill category
        
        for col, (title, skills) in zip(skill_cols, skill_categories.items()):
            with col:
                if skills:
                    self.show_skills_section(title, skills)

        # Closing the container
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    portfolio = PortfolioApp()
    portfolio.run()
