import streamlit as st
from config import PERSONAL_INFO

def show_contact():
    st.header("📬 Get in Touch")
    
    with st.container():
        # Contact form
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{PERSONAL_INFO["email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        
        # Direct contact info
        st.markdown("---")
        st.subheader("Or reach out directly:")
        st.markdown(f"""
        📧 Email: [Huzaifah](mailto:{PERSONAL_INFO["email"]}
        🔗 LinkedIn: [Connect with me](https://linkedin.com/in/yourprofile)
        💬 Schedule a call: [Calendly](https://calendly.com/yourname)
        """)

if __name__ == "__main__":
    show_contact()