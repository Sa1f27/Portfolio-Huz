import streamlit as st
print("Page config set.")
st.set_page_config(page_title="Huzaifah's Portfolio", layout="wide", page_icon='🤖')

import requests
import uuid
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from PIL import Image
from groq import Groq
from config import info, endorsements, SOCIAL_LINKS
from sections.about import show_about, show_education
from sections.projects import PortfolioApp
from sections.contact import show_contact, render_coworker_endorsements
from streamlit_option_menu import option_menu

# Groq API Configuration
GROQ_API_KEY = st.secrets["api_keys"]["groq_api_key"]
client = Groq(api_key=GROQ_API_KEY)

# Load Bio Info
with open("bio.txt", "r") as file:
    bio_info = file.read()

# ------------------- FUNCTIONS ------------------- #

# Load Lottie animation from URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:  # Explicitly use "r" mode for readability
        css_content = f.read()
        # Apply the CSS
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Call the function with the correct file path
local_css("style/style.css")  # Use forward slashes for cross-platform compatibility


# Fetch Groq AI Response
def ask_groq(input_text):
    prompt = f"""
    You are an AI assistant helping to present the portfolio of the following individual based on their biography. 
    Here's the bio:
    {bio_info}

    Respond concisely to the following query from a recruiter or visitor:
    {input_text}
    """
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting AI insights: {str(e)}"

# ------------------- SIDEBAR ------------------- #

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home_Page", "Skills/Projects", "Contact"],
        icons=["house", "graph-up", "person"],
        menu_icon="cast",
        default_index=0,
    )

# ------------------- HOME PAGE ------------------- #

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'''
        <div class="gradient-header">
            <h1 style="color: white; font-size: 3rem; margin-bottom: 0.5rem;">
                {content1}
            </h1>
            <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.2rem;">
                {content2}
            </p>
        </div>
    ''', unsafe_allow_html=True)

def gradient1(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)
    
def Home_Page():
    lottie_gif = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
    full_name = info['Full_Name']
    
    with st.container():
        col1, col2 = st.columns([8, 3])
        with col1:
            gradient1('#FFD4DD','#000395','e0fbfc', f"Hi, I'm {full_name}👋", info["Intro"])
  
            
            # Display Social Links with Emojis side by side
            st.markdown(
                '''
                <div style="display: flex; gap: 15px; font-size: 16px; align-items: center;">
                    <a href="https://github.com/Sa1f27" target="_blank" style="text-decoration: none;">👾 GitHub &nbsp; &nbsp; &nbsp;|</a>
                    <a href="https://www.linkedin.com/in/huzaifah-27o3/" target="_blank" style="text-decoration: none;">🇮🇳 LinkedIn</a>
                </div>
                ''',
                unsafe_allow_html=True
            )
        with col2:
            st.image("images/huz-ima.png", use_container_width=True)

    st.markdown("---")

    
    col5, col6 = st.columns([7, 3])
    with col5:
        user_input = st.text_input("Ask any question about my portfolio!", key="input")
        if user_input:
            response = ask_groq(user_input)
            st.markdown(f'<div class="response">{response}</div>', unsafe_allow_html=True)
        else:
            st.write("Hi, I'm Mohammed Huzaifah. I'm a passionate Machine Learning Engineer with a strong foundation in AI, Data Science and MLOps. Currently, I'm pursuing my degree in Computer Science with specialization in AI/ML. With experience in hackathons, innovative project implementations, and contributing to open-source projects, I'm confident in my ability to design, develop, and deploy scalable AI solutions. I'm immediately available for internship or project opportunities.")
    with col6:
        st_lottie(lottie_gif, height=280, key=str(uuid.uuid4()))
    st.markdown("---")
    with st.container():
        col7, col8 = st.columns([6, 3])
        with col7:
            show_about()
        with col8:
            show_education()
    st.markdown("---")
    resume()
    
# ------------------- RESUME ------------------- #

def resume():
    st.header("Professional Resume")
    file_id = "1EvyvcJoLZDoNe81qnk8KXDkkB3Xu6WHJ"
    pdf_url = f"https://drive.google.com/file/d/{file_id}/preview"
    pdf_display = f'<iframe src="{pdf_url}" width="100%" height="600px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# ------------------- SKILLS AND PROJECTS ------------------- #

def skills():
    gitleet()
    st.markdown("---")
    portfolio = PortfolioApp()
    portfolio.run()

#--------------------Leetcode/Github----------------------#

import streamlit as st
import streamlit.components.v1 as components

def gitleet():
    # Using Streamlit's header for styled headings
    st.header("💻 LeetCode Achievements")
    
    # HTML for LeetCode card
    st.markdown("""
    <a href="https://leetcode.com/huzaif027/" target="_blank">
        <img align="top" src="https://leetcard.jacoblin.cool/huzaif027?theme=dark&font=Nunito&ext=heatmap" alt="LeetCode Profile" />
    </a>
    """, unsafe_allow_html=True)
    
    # GitHub section with Streamlit header
    st.header("👾 GitHub Achievements")
    
    # HTML for GitHub cards
    st.markdown("""
    <a href="https://github.com/Sa1f27" target="_blank">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sa1f27&hide=HTML&langs_count=8&layout=compact&theme=react&border_radius=10&size_weight=0.5&count_weight=0.5&exclude_repo=github-readme-stats" alt="GitHub Stats" />
    </a>
    <a href="https://github.com/Sa1f27" target="_blank">
        <img src="https://github-readme-streak-stats.herokuapp.com/?user=Sa1f27&theme=react&hide_border=false" alt="GitHub Streak Stats" />
    </a>
    """, unsafe_allow_html=True)
    
    # Contribution calendar
    st.subheader("Contribution Calendar")
    components.html(
        """
        <script src="https://unpkg.com/github-calendar@latest/dist/github-calendar.min.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/github-calendar@latest/dist/github-calendar-responsive.css"/>
        <div class="calendar">Loading...</div>
        <script>
            GitHubCalendar(".calendar", "Sa1f27");
        </script>
        """,
        height=180
    )



# ------------------- CONTACT ------------------- #

def Contact():
    col5, col6 = st.columns([2, 2])
    with col5:
        render_coworker_endorsements(endorsements)
    with col6:
        show_contact()

# ------------------- MAIN ------------------- #

if selected == "Home_Page":
    Home_Page()
elif selected == "Skills/Projects":
    skills()
elif selected == "Contact":
    Contact()
