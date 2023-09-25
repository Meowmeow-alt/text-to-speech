import streamlit as st
from googletrans import Translator

translator = Translator()

#___________SIDE BAR____________

st.sidebar.success("This is the second page.")
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

st.title('TRANSLATE')
st.write('###')

def main():
    while True:
        try:
            col1, col2 = st.columns([1, 1])

            with col1:
                st.write("Texts for translation:")
                text = st.text_area()
                dest = language()

            with col2:
                st.write("Translated result:")
                output = trans(text,dest)
                st.write(output)
            break
        except EOFError:
            break
        except:
            pass

def language():
    lang_choices = {'Afrikaans':'af','Arabic':'ar','Bengali':'bn','Bosnian':'bs','Catalan':'ca','Czech':'cs',
    'Welsh':'cy','Danish':'da','German':'de','Greek':'el','English':'en','Esperanto':'eo','Spanish':'es',
    'Estonian':'et','Finnish':'fi','French':'fr','Gujarati':'gu','Hindi':'hi','Croatian':'hr','Hungarian':'hu',
    'Armenian':'hy','Indonesian':'id','Icelandic':'is','Italian':'it','Japanese':'ja','Javanese':'jw','Khmer':'km',
    'Kannada':'kn','Korean':'ko','Latin':'la','Latvian':'lv','Macedonian':'mk','Malayalam':'ml','Marathi':'mr',
    'Myanmar (Burmese)':'my','Nepali':'ne','Dutch':'nl','Norwegian':'no','Polish':'pl','Portuguese':'pt',
    'Romanian':'ro','Russian':'ru','Sinhala':'si','Slovak':'sk','Albanian':'sq','Serbian':'sr','Sundanese':'su',
    'Swedish':'sv','Swahili':'sw','Tamil':'ta','Telugu':'te','Thai':'th','Filipino':'tl','Turkish':'tr',
    'Ukrainian':'uk','Urdu':'ur','Vietnamese':'vi','Chinese':'zh-CN'}

    choice = st.selectbox('Choose a language to translate into:', lang_choices.keys())
    language = lang_choices[choice]
    return language

def trans(text,dest):
    class_output = translator.translate(text, dest=dest)
    text = getattr(class_output, 'text')
    return text

main()
