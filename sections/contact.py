import streamlit as st
from config import PERSONAL_INFO
import streamlit.components.v1 as components

#=======endorsements========
def render_coworker_endorsements(endorsements):
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