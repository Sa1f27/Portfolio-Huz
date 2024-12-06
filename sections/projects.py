import streamlit as st
from config import PROJECTS, SKILLS

class PortfolioApp:
    def __init__(self):
        self.apply_custom_styles()
    
    def apply_custom_styles(self):
        st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    /* Skill Badge */
    .skill-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        background: linear-gradient(135deg, #cfd8dc 0%, #b0bec5 100%); /* Blue-gray gradient */
        border-radius: 8px;
        border: 1px solid #90a4ae; /* Lighter blue-gray border */
        transition: transform 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #263238; /* Dark text for contrast */
    }
    .skill-badge:hover {
        transform: translateY(-2px);
    }
    .skill-icon {
        margin-right: 0.5rem;
        color: #607d8b; /* Darker blue-gray for the icons */
    }

    /* Project Card */
    .project-card {
        background: #263238; /* Light blue-gray background */
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #90a4ae;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        color: #263238; /* Dark text for readability */
    }
    .project-card:hover {
        transform: translateY(-3px);
    }

    /* Project Title */
    .project-title {
        color: #eceff1; /* Dark blue-gray for the title */
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* Tech Stack */
    .tech-stack {
        margin: 1rem 0;
        color: #607d8b; /* Soft blue-gray text for tech stack */
    }

    /* Section Header */
    .section-header {
        border-bottom: 2px solid #607d8b; /* Darker blue-gray border */
        padding-bottom: 0.5rem;
        margin-bottom: 2rem;
        color: #263238; /* Dark text for section header */
    }

    /* Soft Skill Item */
    .soft-skill-item {
        background: #f5f5f5; /* Light gray for a soft contrast */
        padding: 0.75rem;
        border-radius: 6px;
        margin: 0.5rem 0;
        border-left: 4px solid #607d8b; /* Blue-gray left border */
        color: #263238; /* Dark text for contrast */
    }
</style>

        """, unsafe_allow_html=True)

    def get_icon_for_skill(self, skill_name):
        # Map skills to Font Awesome icons
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
            # Add default icon for unknown skills
            'default': 'fas fa-code'
        }
        return icon_mapping.get(skill_name, icon_mapping['default'])

    def show_project_card(self, project):
        st.markdown(f"""
            <div class="project-card">
                <h3 class="project-title">{project['title']}</h3>
                <p>{project['description']}</p>
                <div class="tech-stack">
                    {''.join([f'<span class="skill-badge"><i class="{self.get_icon_for_skill(tech)} skill-icon"></i>{tech}</span>' for tech in project['tech_stack']])}
                </div>
                <div style="display: flex; gap: 1rem;">
                    {'<a href="' + project.get('github_link', '#') + '" target="_blank"><i class="fab fa-github"></i> GitHub</a>' if project.get('github_link') else ''}
                    {'<a href="' + project.get('live_link', '#') + '" target="_blank"><i class="fas fa-external-link-alt"></i> Live Demo</a>' if project.get('live_link') else ''}
                </div>
            </div>
        """, unsafe_allow_html=True)

    def show_skills_section(self, title, skills, columns=2):
        st.markdown(f'<h3 class="section-header">{title}</h3>', unsafe_allow_html=True)
        cols = st.columns(columns)
        for idx, skill in enumerate(skills):
            with cols[idx % columns]:
                st.markdown(f"""
                    <div class="skill-badge">
                        <i class="{self.get_icon_for_skill(skill)} skill-icon"></i>
                        {skill}
                    </div>
                """, unsafe_allow_html=True)

    def show_soft_skills(self):
        st.markdown('<h3 class="section-header">Soft Skills</h3>', unsafe_allow_html=True)
        for skill in SKILLS['soft_skills']:
            st.markdown(f"""
                <div class="soft-skill-item">
                    <i class="fas fa-check-circle" style="color: #0366d6; margin-right: 0.5rem;"></i>
                    {skill}
                </div>
            """, unsafe_allow_html=True)

    def run(self):
        col1, col2 = st.columns([4, 2])

        # In the first column, display Featured Projects
        with col1:
            st.header("Featured Projects")
            for project in PROJECTS:
                self.show_project_card(project)
        
        # In the second column, create two rows for Skills & Expertise and Tools & Platforms
        with col2:
            # First row: Skills & Expertise
            st.header("Skills & Expertise")
            col3, col4 = st.columns([1, 1])
            with col3:
                # Programming Languages
                self.show_skills_section("Programming Languages", SKILLS['programming_languages'])
                
                # Technologies & Frameworks
                tech_sections = {
                    "Machine Learning": SKILLS.get('machine_learning_frameworks', []),
                    "Cloud Technologies": SKILLS.get('cloud_technologies', []),
                    "Data Management": SKILLS.get('data_management', []),
                    "Data Visualization": SKILLS.get('data_visualization', [])
                }
                for title, skills in tech_sections.items():
                    if skills:  # Only show sections with skills
                        self.show_skills_section(title, skills)
            
            with col4:
                # Tools & Platforms
                self.show_skills_section("Tools & Platforms", SKILLS['tools'], columns=3)
                
                # Soft Skills
                self.show_soft_skills()


if __name__ == "__main__":
    portfolio = PortfolioApp()
    portfolio.run()