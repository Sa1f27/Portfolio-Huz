import streamlit as st
from config import PROJECTS, SKILLS

class PortfolioApp:
    def __init__(self):
        self.apply_custom_styles()
    
    def apply_custom_styles(self):
        st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <style>
                /* Global Styles */
                .stApp {
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    color: #e2e8f0;
                }
                
                /* Skill Badge */
                .skill-badge {
                    display: inline-flex;
                    align-items: center;
                    padding: 0.5rem 1rem;
                    margin: 0.3rem;
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
                    border-radius: 12px;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    backdrop-filter: blur(10px);
                    color: #e2e8f0;
                }
                .skill-badge:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
                    border-color: rgba(255, 255, 255, 0.2);
                }
                .skill-icon {
                    margin-right: 0.5rem;
                    color: #60a5fa;
                }

                /* Project Card */
                .project-card {
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
                    border-radius: 16px;
                    padding: 2rem;
                    margin: 1.5rem 0;
                    border: 1px solid rgba(255, 255, 255, 0.1);
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                    backdrop-filter: blur(10px);
                    transition: all 0.3s ease;
                }
                .project-card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.3);
                }

                /* Project Title */
                .project-title {
                    color: #60a5fa;
                    font-size: 1.75rem;
                    font-weight: 700;
                    margin-bottom: 1.5rem;
                    letter-spacing: 0.5px;
                }

                /* Tech Stack */
                .tech-stack {
                    margin: 1.5rem 0;
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0.5rem;
                }

                /* Section Header */
                .section-header {
                    color: #60a5fa;
                    font-size: 1.5rem;
                    font-weight: 600;
                    margin: 2rem 0 1rem 0;
                    padding-bottom: 0.5rem;
                    border-bottom: 2px solid rgba(96, 165, 250, 0.3);
                }

                /* Links */
                .project-links {
                    display: flex;
                    gap: 1rem;
                    margin-top: 1.5rem;
                }
                .project-link {
                    display: inline-flex;
                    align-items: center;
                    padding: 0.5rem 1rem;
                    background: rgba(96, 165, 250, 0.1);
                    border-radius: 8px;
                    color: #60a5fa;
                    text-decoration: none;
                    transition: all 0.3s ease;
                }
                .project-link:hover {
                    background: rgba(96, 165, 250, 0.2);
                    transform: translateY(-2px);
                }
                .project-link i {
                    margin-right: 0.5rem;
                }

                /* Soft Skills */
                .soft-skill-item {
                    background: linear-gradient(135deg, rgba(96, 165, 250, 0.1) 0%, rgba(96, 165, 250, 0.05) 100%);
                    padding: 1rem;
                    border-radius: 12px;
                    margin: 0.75rem 0;
                    border-left: 4px solid #60a5fa;
                    backdrop-filter: blur(10px);
                }

                /* Streamlit Overrides */
                .stMarkdown {
                    color: #e2e8f0;
                }
                .stHeader {
                    color: #60a5fa !important;
                    font-weight: 700;
                }
                
                /* Skills Grid */
                .skills-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                    gap: 1rem;
                    margin: 1rem 0;
                }
            </style>
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



    def show_skills_section(self, title, skills):
        st.markdown(f'<h3 class="section-header">{title}</h3>', unsafe_allow_html=True)
        st.markdown('<div class="skills-grid">', unsafe_allow_html=True)
        for skill in skills:
            st.markdown(f"""
                <div class="skill-badge">
                    <i class="{self.get_icon_for_skill(skill)} skill-icon"></i>
                    {skill}
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def show_soft_skills(self):
        st.markdown('<h3 class="section-header">Soft Skills</h3>', unsafe_allow_html=True)
        for skill in SKILLS['soft_skills']:
            st.markdown(f"""
                <div class="soft-skill-item">
                    <i class="fas fa-star" style="color: #60a5fa; margin-right: 0.5rem;"></i>
                    {skill}
                </div>
            """, unsafe_allow_html=True)

    def run(self):
        # Main container with padding
        st.markdown('<div style="padding: 2rem 0;">', unsafe_allow_html=True)
        
        # Two-column layout
        col1, col2 = st.columns([5, 3])

        with col1:
            st.header("Featured Projects")
            for project in PROJECTS:
                self.show_project_card(project)
                st.markdown("---")
                st.markdown('<div class="skills-grid">', unsafe_allow_html=True)
        
        with col2:
            st.header("Skills & Expertise")
            
            # Programming Languages
            self.show_skills_section("Programming Languages", SKILLS['programming_languages'])
            
            # Other technical sections
            tech_sections = {
                "Machine Learning": SKILLS.get('machine_learning_frameworks', []),
                "Cloud Technologies": SKILLS.get('cloud_technologies', []),
                "Data Management": SKILLS.get('data_management', []),
                "Data Visualization": SKILLS.get('data_visualization', [])
            }
            
            for title, skills in tech_sections.items():
                if skills:
                    self.show_skills_section(title, skills)
            
            # Tools & Platforms
            self.show_skills_section("Tools & Platforms", SKILLS['tools'])
            
            # Soft Skills
            self.show_soft_skills()
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    portfolio = PortfolioApp()
    portfolio.run()