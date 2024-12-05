import streamlit as st
from config import SOCIAL_LINKS

def show_header():
    with st.container():
        cols = st.columns([2, 1])
        
        with cols[0]:
            st.title(f"Hi! I'm Huzaifah")
            st.subheader("Data Scientist")
            st.write("""
            Welcome to my portfolio! I'm passionate about creating innovative solutions 
            and bringing ideas to life through code.
            """)
            
            # Social Links
            social_cols = st.columns(len(SOCIAL_LINKS))
            for idx, (platform, link) in enumerate(SOCIAL_LINKS.items()):
                with social_cols[idx]:
                    st.markdown(f"[![{platform}](images/{platform.lower()}.png)]({link})")
        

if __name__ == "__main__":
    show_header()