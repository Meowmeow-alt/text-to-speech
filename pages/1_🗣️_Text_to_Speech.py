import streamlit as st
from gtts import gTTS

#___________SIDE BAR____________

st.sidebar.success("Select a page above ^")
st.sidebar.image('Images/sidebar.png', output_format='png')
st.sidebar.header('📸 Caution')
st.sidebar.info(
    'Made by Tran Bao Tien\n\n'
    'For more information, contact me through my email: baotiendancer@gmail.com'
    )

def css(file):
     with open(file) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")

#___________MAIN CONTENT____________

st.title('CONVERT TEXT TO SPEECH')
st.write('###')

def main():
     text = text_()
     st.write('###')
     language = language_()
     st.write('###')
     speed = speed_()
     st.write('###')
     try:
          converting(text,language,speed)
     except AssertionError:
          pass

# text to convert
def text_():
     text = st.text_input('Your text to convert:')
     return text

# language
lang_choice = {'Afrikaans':'af','Albanian':'sq','Arabic':'ar','Armenian':'hy','Bengali':'bn',
'Bosnian':'bs','Catalan':'ca','Chinese':'zh','Chinese (Mandarin/China)':'zh-cn',
'Chinese (Mandarin/Taiwan)':'zh-tw','Chinese (Cantonese)':'zh-yue','Croatian':'hr','Czech':'cs',
'Danish':'da','Dutch':'nl','English':'en','English (Australia)':'en-au',
'English (United Kingdom)':'en-uk','English (United States)':'en-us','Esperanto':'eo',
'Finnish':'fi','French':'fr','German':'de','Greek':'el','Hindi':'hi','Hungarian':'hu',
'Icelandic':'is','Indonesian':'id','Italian':'it','Japanese':'ja','Korean':'ko','Spanish':'es',
'Spanish (Spain)':'es-es','Spanish (United States)':'es-us','Vietnamese':'vi','Thai': 'th'}

def language_():
     choice = st.selectbox('Choose a language:', lang_choice.keys())
     language = lang_choice[choice]
     return language

# speed
def speed_():
     speed = st.radio(
          "Do you want to hear the speech slowly?",
          [":rainbow[YES PLEASE]", "NO THANKS"])
     if speed == ':rainbow[YES PLEASE]':
          return True
     return False

# Converting
def converting(text, language, speed):
     result = gtts.gTTS(text,lang=language,slow=speed)
     result.save('result.mp3')
     st.audio('result.mp3')

main()
