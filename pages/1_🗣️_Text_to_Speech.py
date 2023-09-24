import streamlit as st
import gtts

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
lang_choice = {'Afrikaans':'af','Arabic':'ar','Bengali':'bn','Bosnian':'bs','Catalan':'ca','Czech':'cs',
    'Welsh':'cy','Danish':'da','German':'de','Greek':'el','English':'en','Esperanto':'eo','Spanish':'es',
    'Estonian':'et','Finnish':'fi','French':'fr','Gujarati':'gu','Hindi':'hi','Croatian':'hr','Hungarian':'hu',
    'Armenian':'hy','Indonesian':'id','Icelandic':'is','Italian':'it','Japanese':'ja','Javanese':'jw','Khmer':'km',
    'Kannada':'kn','Korean':'ko','Latin':'la','Latvian':'lv','Macedonian':'mk','Malayalam':'ml','Marathi':'mr',
    'Myanmar (Burmese)':'my','Nepali':'ne','Dutch':'nl','Norwegian':'no','Polish':'pl','Portuguese':'pt',
    'Romanian':'ro','Russian':'ru','Sinhala':'si','Slovak':'sk','Albanian':'sq','Serbian':'sr','Sundanese':'su',
    'Swedish':'sv','Swahili':'sw','Tamil':'ta','Telugu':'te','Thai':'th','Filipino':'tl','Turkish':'tr',
    'Ukrainian':'uk','Urdu':'ur','Vietnamese':'vi','Chinese':'zh-CN'}

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
