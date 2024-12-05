import streamlit as st
from config import EDUCATION

def show_education():
    st.header("🎓 Education")
    
    with st.container():
        cols = st.columns([4, 1])
        
        with cols[0]:
            st.subheader(EDUCATION["degree"])
            st.write(EDUCATION["university"])
            st.write(f"*{EDUCATION['duration']}*")
            
            if EDUCATION.get("relevant_courses"):
                st.markdown("**Relevant Courses:**")
                for course in EDUCATION["relevant_courses"]:
                    st.markdown(f"- {course}")
        
        with cols[1]:
            if EDUCATION.get("logo"):
                st.image(EDUCATION["logo"], width=100)
    
    st.markdown("---")

if __name__ == "__main__":
    show_education()
