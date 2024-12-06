import streamlit as st
from config import PERSONAL_INFO
import streamlit.components.v1 as components

#=======endorsements========
def render_coworker_endorsements(endorsements):
    # -----------------  endorsement  ----------------- #
    st.header("My Journey Through Others' Words")
    st.write("Acknowledgments from mentors, professors, and peers who value the skills I bring to every project and collaboration.")
    # CSS for custom cards
    st.markdown(
        """
        <style>
        .endorsement-card {
            border-radius: 10px;
            padding: 20px;
            margin: 15px 0;
            color: white;
            font-family: Arial, sans-serif;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        .endorsement-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .endorsement-content {
            font-size: 16px;
            line-height: 1.5;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display the endorsements dynamically
    for endorsement in endorsements:
        st.markdown(
            f"""
            <div class="endorsement-card" style="background: {endorsement['gradient']}">
                <div class="endorsement-title">{endorsement['title']}</div>
                <div class="endorsement-content">{endorsement['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


#======contact========
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
    render_coworker_endorsements()