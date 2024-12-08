import streamlit as st
import streamlit.components.v1 as components

info = {
   "Pronoun": "Him",
   "Name": "Huzaifah",
   "Full_Name": "Md Huzaifah",
   "Intro": "Machine Learning and AI Enthusiast | Developer | Hacker | Problem Solver",
   "LinkedIn":"https://www.linkedin.com/in/huzaifah-27o3/",
   "City":"Hyderabad, India",
   "Photo": """<a href="https://www.linkedin.com/in/huzaifah-27o3/"><img src="images\huz-bat.png" width="200" alt="Profile" title="Profile"></a>""",
   "Email": "huzaif027@gmail.com"
}

endorsements = [
            {
                "title": "Outstanding Developer",
                "content": "Recognized for exceptional problem-solving skills and innovative solutions.",
                "gradient": "linear-gradient(to right, #4CAF50, #81C784)"
            },
            {
                "title": "Team Player",
                "content": "Praised for seamless collaboration and communication within diverse teams.",
                "gradient": "linear-gradient(to right, #2196F3, #64B5F6)"
            },
            {
                "title": "AI Enthusiast",
                "content": "Contributed to groundbreaking projects in machine learning and AI.",
                "gradient": "linear-gradient(to right, #FF5722, #FF8A65)"
            }
        ]

# Personal Information
PERSONAL_INFO = {
    "name": "Huzaifah",
    "title": "Computer Science Student | Aspiring AI & Machine Learning Engineer",
    "email": "huzaif027@gmail.com",
    "github": "https://github.com/Sa1f27",
    "linkedin": "https://www.linkedin.com/in/huzaifah-27o3/",
    "about": """
    I am a passionate Computer Science student specializing in AI and Machine Learning. 
    I love solving real-world problems using data-driven solutions and am actively seeking 
    opportunities to apply my skills in impactful projects.
    """
}

# Project Showcase
PROJECTS = [
    {
        "title": "KidsCare Pro",
        "description": "Smart pediatric health solution for monitoring children's growth and development.",
        "tech_stack": ["Python", "AWS", "Scikit-learn", "LightGBM", "Llama"],
        "github_link": "https://github.com/Sa1f27/KidsCare-Pro.git",
        "image": r"images/kids.png"
    },
    {
        "title": "Disease Prediction",
        "description": "Machine learning model to predict disease using modular code.",
        "tech_stack": ["KNN Classifier", "Scikit-learn", "Tensorflow", "Gemini"],
        "github_link": "https://github.com/Sa1f27/Disease-Prediction.git",
        "image": r"images/health.png"
    }
]

# Education Details
EDUCATION = {
    "university": "Lords Institute of Engineering and Technology",
    "degree": "Bachelor of Technology in Computer Science",
    "duration": "2022 - 2026",
    "gpa": "8.7/10",
    "relevant_courses": [
        "Machine Learning",
        "Artificial Intelligence",
        "Data Structures & Algorithms",
        "Database Systems"
    ]
}

# Skills Configuration
SKILLS = {
    "programming_languages": ["Python", "C", "C++", "Java", "HTML", "CSS", "JavaScript"],
    "machine_learning_frameworks": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras", "OpenCV"],
    "cloud_technologies": ["AWS", "Azure"],
    "data_management": ["SQL", "Pandas"],
    "data_visualization": ["Matplotlib", "Seaborn"],
    "tools": ["Git", "Docker", "Jupyter Notebooks", "VS Code"],
    "soft_skills": ["Problem Solving", "Team Collaboration", "Communication"]
}

# Social Media Links
SOCIAL_LINKS = {
    "GitHub": "https://github.com/Sa1f27",
    "LinkedIn": "https://www.linkedin.com/in/huzaifah-27o3/"
}

# About Section
ABOUT_ME = """
I am a Computer Science student with a passion for AI, Machine Learning, and emerging technologies. 
I enjoy participating in hackathons, solving coding challenges, and working on innovative projects. 
Currently seeking opportunities to enhance my skills and contribute to impactful projects.
"""

INTERESTS = [
    {
        "title": "Machine Learning",
        "description": "Building models that solve real-world problems using data."
    },
    {
        "title": "Web Development",
        "description": "Creating user-friendly web applications with modern frameworks."
    },
    {
        "title": "Hackathons",
        "description": "Competing in hackathons to develop innovative solutions under pressure."
    }
]

html_code = """
<script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
<dotlottie-player 
    src="https://lottie.host/99cb5d48-31ac-49de-a7b3-096b769beae0/x7Y2HyZsp6.lottie" 
    background="transparent" 
    speed="1" 
    style="width: 250px; height: 250px" 
    loop 
    autoplay>
</dotlottie-player>
"""
#--------------------Leetcode/Github----------------------#
def gitleet():
    # Section 1: LeetCode Achievements
    st.header("💻 LeetCode Achievements")
    st.markdown("""
    <a href="https://leetcode.com/huzaif027/" target="_blank">
        <img align="top" src="https://leetcard.jacoblin.cool/huzaif027?theme=dark&font=Nunito&ext=heatmap" alt="LeetCode Profile" />
    </a>
    """, unsafe_allow_html=True)

    # Separator
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

    # Section 2: GitHub Achievements
    st.header("👾 GitHub Achievements")
    
    # Row 1: GitHub Stats
    github_stats_cols = st.columns(2)
    with github_stats_cols[0]:
        st.markdown("""
        <a href="https://github.com/Sa1f27" target="_blank">
            <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sa1f27&hide=HTML&langs_count=8&layout=compact&theme=react&border_radius=10&size_weight=0.5&count_weight=0.5&exclude_repo=github-readme-stats" alt="GitHub Top Languages" />
        </a>
        """, unsafe_allow_html=True)
    with github_stats_cols[1]:
        st.markdown("""
        <a href="https://github.com/Sa1f27" target="_blank">
            <img src="https://github-readme-streak-stats.herokuapp.com/?user=Sa1f27&theme=react&hide_border=false" alt="GitHub Streak Stats" />
        </a>
        """, unsafe_allow_html=True)

    # Separator
    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

    # Section 3: GitHub Contribution Calendar
    st.subheader("📆 Contribution Calendar")
    st.markdown("""
    <a href="https://github.com/Sa1f27" target="_blank">
        <img src="https://ghchart.rshah.org/Sa1f27" alt="GitHub Contribution Chart" style="width: 1000px; height: 170px; object-position: right;" />
    </a>
    """, unsafe_allow_html=True)


# Theme and Style Settings
THEME_COLOR = "#FF4B4B"
SECONDARY_COLOR = "#0083B8"
BACKGROUND_COLOR = "#F5F5F5"

# SEO and Meta Settings
SITE_TITLE = "Huzaifah - Machine Learning & AI Enthusiast"
SITE_DESCRIPTION = "Portfolio showcasing Huzaifah's projects, skills, and experience in AI and software development."
SITE_KEYWORDS = ["machine learning", "AI", "python", "portfolio", "computer science"]

# API Keys and External Services (Note: Use environment variables for production)
GITHUB_TOKEN = "your_github_token"  
EMAIL_SETTINGS = {
    "SMTP_SERVER": "smtp.gmail.com",
    "SMTP_PORT": 587,
    "SENDER_EMAIL": "huzaif0207@gmail.com"
}
