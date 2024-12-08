import streamlit as st
print("Page config set.")
st.set_page_config(page_title="Huzaifah's Portfolio", layout="wide", page_icon='🤖')

import requests
import uuid
import streamlit.components.v1 as components
from PIL import Image
from groq import Groq
from config import info, endorsements, gitleet, html_code
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
    You are an AI assistant presenting my portfolio based on my biography. Use the provided bio to respond concisely, acting as if you are me.

    my bio:
    {bio_info}

    Task:
    Respond to the following query from a recruiter or visitor in a professional and confident tone:
    {input_text}

    Guidelines:
    Provide responses that are clear, to the point, and professional.
    Use bullet points if applicable to ensure readability.
    If specific details are unavailable, share my contact information for further discussion.
    Showcase my strengths, experiences, and relevant achievements wherever relevant.
    Craft the best possible response to reflect my skills and professionalism.
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

# Add gradient to the sidebar
def apply_sidebar_gradient(color1, color2, color3):
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background: linear-gradient(to bottom, {color1}, {color2}, {color3});
            border-radius: 10px;
            padding: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
apply_sidebar_gradient('#FFD4DD','#000395','#e0fbfc')

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home_Page", "Skills/Projects", "Contact"],
        icons=["house", "graph-up", "person"],
        menu_icon="cast",
        default_index=0,
        styles={
        "container": {"padding": "5px", "background-color": "#063D75"},  # Background of the sidebar
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "5px",
            "--hover-color": "#262730",  # Hover color for links
        },
        "nav-link-selected": {
            "background-color": "cyan",  # Color for the selected tab
            "color": "black",  # Text color for the selected tab
        },
    },
    )

# ------------------- HOME PAGE ------------------- #

def gradient1(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)
    
def Home_Page():
    
    full_name = info['Full_Name']
    
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            gradient1('#FFD4DD','#000395','#e0fbfc', f"Hi, I'm {full_name}👋", info["Intro"])
  
            
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
            st.image("images/huz-ima.png", width=180)


    st.markdown("---")

    
    col5, col6 = st.columns([8, 3])
    with col5:
        user_input = st.text_input("Ask any question about my portfolio!", key="input")
        if user_input:
            response = ask_groq(user_input)
            st.markdown(f'<div class="response">{response}</div>', unsafe_allow_html=True)
        else:
            st.write("Hi, I'm Mohammed Huzaifah. I'm a passionate Machine Learning Engineer with a strong foundation in AI, Data Science and MLOps. Currently, I'm pursuing my degree in Computer Science with specialization in AI/ML. With experience in hackathons, innovative project implementations, and contributing to open-source projects, I'm confident in my ability to design, develop, and deploy scalable AI solutions. I'm immediately available for internship or project opportunities.")
    with col6:
        st.components.v1.html(html_code, height=250)
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
    st.markdown("# 🚀 My Technical Journey")
    portfolio = PortfolioApp()
    portfolio.run()
    gitleet()
    st.markdown("---")

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
