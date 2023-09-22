import streamlit as st

st.set_page_config(page_title = "Text to Speech",
                   page_icon = ":space_invader:",
                   layout = "wide")

#___________SIDE BAR____________

st.sidebar.success("Select a page above ^")
st.sidebar.image('Images/sidebar.png', output_format='png')
st.sidebar.header('📸 Caution')
st.sidebar.info(
    'Made by Tran Bao Tien\n\n'
    'For more information, contact me through my email: baotiendancer@gmail.com'
    )

#___________MAIN CONTENT____________

st.title("Google Text to Speech Library")
st.write("""
###
- In Python, gtts stands for Google Text-to-Speech, which is a library 
and tool that can convert text to audio using the Google Translate API.
- It can create audio files or play sounds from any text in various 
languages and accents.
- It is easy to install and use, and it has some options to customize 
the speech such as speed, pitch, and pre-processing.
""")
