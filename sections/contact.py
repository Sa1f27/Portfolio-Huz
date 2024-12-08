import streamlit as st
from config import endorsements
import requests

# Function to load custom CSS
def local_css(file_name):
    with open(file_name, "r") as f:
        css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

#======= Endorsements Section ========
def render_coworker_endorsements(endorsements):
    st.header("💬 My Journey Through Others' Words")
    st.write("Acknowledgments from mentors, professors, and peers who value the skills I bring to every project and collaboration.")
    
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

#======= Contact Section ========
def show_contact():
    st.header("📬 Get in Touch")
    
    with st.container():
        # Contact form header
        st.title("Contact Us")
        with st.form(key='contact_form'):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submit_button = st.form_submit_button("Send")

        if submit_button:
            # Prepare the data to be sent to FormSubmit
            form_data = {
                "name": name,
                "email": email,
                "message": message
            }

            # FormSubmit URL with your email address
            formsubmit_url = "https://formsubmit.co/huzaif027@gmail.com"  # Replace with your email address

            # Send the form data to FormSubmit
            response = requests.post(formsubmit_url, data=form_data)

            # Check if the submission was successful
            if response.status_code == 200:
                st.success("Thank you for your message! We'll get back to you soon.")
            else:
                st.error("There was an issue submitting the form. Please try again later.")

#======= Main Run Function ========
def run():
    # Load custom CSS styles
    local_css("style/style.css")

    # Show Contact and Endorsements sections
    show_contact()
    
    render_coworker_endorsements(endorsements)


# Run the app
if __name__ == "__main__":
    run()
