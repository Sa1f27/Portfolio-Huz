import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from config import info, endorsements
from PIL import Image
from groq import Groq
from config import SOCIAL_LINKS, endorsements
import uuid

# Configure Streamlit page
st.set_page_config(page_title="Huzaifah's Portfolio", layout="wide", page_icon='🤖')

#-----------------Groq Configuration------------------#

GROQ_API_KEY = st.secrets["api_keys"]["groq_api_key"]  # Replace with your Groq API key
client = Groq(api_key=GROQ_API_KEY)

# Load bio data (if you still want to use bio.txt or another source)
with open("bio.txt", "r") as file:
    bio_info = file.read()

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

# -----------------  loading assets  ----------------- #

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")
lottie_gif = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

# ----------------- info ----------------- #

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    # Social Links
    social_cols = st.columns(len(SOCIAL_LINKS))
    for idx, (platform, link) in enumerate(SOCIAL_LINKS.items()):
        with social_cols[idx]:
            st.markdown(f"[![{platform}](images/{platform.lower()}.png)]({link})")
    
with col2:
    st.image("images/huz-bat.png", width=200)


with st.container():
    col5, col6 = st.columns([6, 3])

# Get user input
with col5:
    def get_text():
        return st.text_input(
            "Ask any question about my portfolio!",
            key="input"  # Unique key using uuid
        )

    user_input = get_text()

    # Generate response
    if user_input:
        response = ask_groq(user_input)
        st.markdown(response)

with col6:
    st_lottie(lottie_gif, height=280, key=str(uuid.uuid4()))

# -----------------  resume  -----------------  #

import base64

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

with open("images/resume-huz.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)

# ----------------- timeline ----------------- #

from sections.about import show_about, show_education
from sections.projects import show_skills, show_projects
from sections.contact import show_contact, render_coworker_endorsements


col1, col2 = st.columns([4, 2])

# In the first column, display About Me
with col1:
    show_about()

# In the second column, display Education & Certifications
with col2:
    show_education()#

col3, col4 = st.columns([2, 2])

# In the first column, display About Me
with col3:
    # Skills Section
    show_skills()
with col4:
    # Projects Section (Featured)
    show_projects()


col5, col6 = st.columns([4, 2])

# In the first column, display About Me
with col5:
    #endorsements
    render_coworker_endorsements(endorsements)
with col6:
    # Contact Form
    show_contact()
