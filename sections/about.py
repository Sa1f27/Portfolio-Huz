import streamlit as st
from config import ABOUT_ME, INTERESTS

def show_about():
    st.header("🧔 About Me")
    
    # Main about text
    st.write(ABOUT_ME)
    
    # Interests
    st.subheader("What I Love")
    cols = st.columns(3)
    for idx, interest in enumerate(INTERESTS):
        with cols[idx % 3]:
            st.markdown(f"""
            ##### {interest['title']}
            {interest['description']}
            """)
    
    # Stats or Quick Facts
    st.subheader("Quick Facts")
    stat_cols = st.columns(4)
    with stat_cols[0]:
        st.metric("Years of Experience", "3+")
    with stat_cols[1]:
        st.metric("Projects Completed", "20+")
    with stat_cols[2]:
        st.metric("GitHub Repos", "30+")
    with stat_cols[3]:
        st.metric("Happy Clients", "15+")


if __name__ == "__main__":
    show_about()