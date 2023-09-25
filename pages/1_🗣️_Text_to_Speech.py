import streamlit as st
import gtts
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

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
    while True:
        try:
            text = st.text_input("Your text to convert: ")
            st.write('###')

            lang = language()
            st.write('###')

            speed = ask_speed()
            st.write('###')

            convert(text,lang,speed)
            st.write('###')

            sentiment_detection(text)
            break
        except EOFError:
            break
        except:
            pass

# language
def language(l):
    lang_choices = {'Afrikaans':'af','Arabic':'ar','Bengali':'bn','Bosnian':'bs','Catalan':'ca','Czech':'cs',
    'Welsh':'cy','Danish':'da','German':'de','Greek':'el','English':'en','Esperanto':'eo','Spanish':'es',
    'Estonian':'et','Finnish':'fi','French':'fr','Gujarati':'gu','Hindi':'hi','Croatian':'hr','Hungarian':'hu',
    'Armenian':'hy','Indonesian':'id','Icelandic':'is','Italian':'it','Japanese':'ja','Javanese':'jw','Khmer':'km',
    'Kannada':'kn','Korean':'ko','Latin':'la','Latvian':'lv','Macedonian':'mk','Malayalam':'ml','Marathi':'mr',
    'Myanmar (Burmese)':'my','Nepali':'ne','Dutch':'nl','Norwegian':'no','Polish':'pl','Portuguese':'pt',
    'Romanian':'ro','Russian':'ru','Sinhala':'si','Slovak':'sk','Albanian':'sq','Serbian':'sr','Sundanese':'su',
    'Swedish':'sv','Swahili':'sw','Tamil':'ta','Telugu':'te','Thai':'th','Filipino':'tl','Turkish':'tr',
    'Ukrainian':'uk','Urdu':'ur','Vietnamese':'vi','Chinese':'zh-CN'}

    choice = st.selectbox('Choose a language:', lang_choices.keys())
    language = lang_choices[choice]
    return language

# speed
def ask_speed():
    speed = st.radio(
        "Do you want to hear the speech slowly?",
        [":rainbow[YES PLEASE]", "NO THANKS"])
    if speed == ':rainbow[YES PLEASE]':
        return True
    return False

# Converting
def convert(text,lang,speed):
    result = gtts.gTTS(text=text, lang=lang, slow=speed)
    result.save('audio.mp3')
    st.audio("audio.mp3")

def sentiment_detection(text):
    class_output = translator.translate(text, dest='en')
    text = getattr(class_output, 'text')

    analyze = TextBlob(text)
    rate = analyze.sentiment.polarity
    if rate == 0:
        return st.info('Sentiment analysis: Your text is neutral')
    elif rate > 0:
        return st.success('Sentiment analysis: Your text is positive')
    return st.warning('Sentiment analysis: Your text is negative')

main()
