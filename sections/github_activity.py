
import streamlit as st
import streamlit.components.v1 as components
# from config import GITHUB_USERNAME

def show_github_activity():
    st.header("📊 GitHub Activity")
    
    # GitHub stats using metrics.lecoq.io
    st.markdown(f"""
    #### GitHub Statistics
    ![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Sa1f27&show_icons=true&theme=radical)
    """)
    
    # Language statistics
    st.markdown(f"""
    #### Most Used Languages
    ![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Sa1f27&layout=compact&theme=radical)
    """)
    
    # Contribution calendar
    st.subheader("Contribution Calendar")
    components.html(
        f"""
        <script src="https://unpkg.com/github-calendar@latest/dist/github-calendar.min.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/github-calendar@latest/dist/github-calendar-responsive.css"/>
        <div class="calendar">Loading...</div>
        <script>
            GitHubCalendar(".calendar", "Sa1f27");
        </script>
        """,
        height=200
    )

if __name__ == "__main__":
    show_github_activity()