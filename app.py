import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from config import info, endorsements
from PIL import Image
from groq import Groq

# Configure Streamlit page
st.set_page_config(page_title="Huzaifah's Portfolio", layout="wide", page_icon='🤖')

st.markdown(
    """
    <style>
    .big-header {
        font-size: 90px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .sub-header {
        font-size: 30px;
        color: #333;
        text-align: center;
    }
    </style>
    <div class="big-header"> Welcome to My Portfolio 🤖</div>
    <div class="sub-header"> Hi, I'm Huzaifah - AI/ML Enthusiast and Developer </div>
    """,
    unsafe_allow_html=True
)

# Groq Configuration - Hardcoded API Key
GROQ_API_KEY = "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"  # Replace with your Groq API key
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


# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

import uuid

with st.container():
    col5, col6 = st.columns([8, 3])

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
    else:
        st.write("nooooo")


with col6:
    st_lottie(lottie_gif, height=280, key=str(uuid.uuid4()))


with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    
with col2:
    # Path to the image file
    image_path = "images/huz-bat.png" 
    st.image(image_path, width=200)


# -----------------  resume  -----------------  #

import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

with open("images/resume-huz.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)

# ----------------- timeline ----------------- #
from sections.header import show_header
from sections.about import show_about
from sections.skills import show_skills
from sections.projects import show_projects
from sections.education import show_education
from sections.contact import show_contact
from sections.github_activity import show_github_activity

show_header()
    
# About Me Section
show_about()

# Skills Section
show_skills()

# Projects Section (Featured)
show_projects()

# Education & Certifications
show_education()

# GitHub Activity
show_github_activity()

# Contact Form
show_contact()

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👄 Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
