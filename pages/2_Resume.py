import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

import streamlit as st
from PIL import Image

# Path to the image file
image_path = "images/huz-bat.png"  # Adjust the path as needed

# Display the image in the sidebar
st.sidebar.image(image_path, width=200)  # You can adjust the width as needed

# If you want to add a clickable link, you can use markdown like this:
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/huzaifah-27o3/)")

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open("images/resume-huz.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
