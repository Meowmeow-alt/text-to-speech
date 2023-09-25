# TEXT TO SPEECH AND SENTIMENT ANALYSIS
---

## **CONTENTS**

- [INTRODUCTION](#introduction)

- [DESCRIPTION](#description)

- [TO-DO](#to-do)

- [LIBRARIES INCLUDE](#libraries-include)

---


#### INTRODUCTION:
- With the text you provided, we can create a speech and analyze the sentiment of it. How amazing?!

Text-to-speech (TTS) is a technology that can convert written text into spoken audio. Sentiment analysis is a technique that can detect the emotions and opinions expressed in text. Both of these applications have many potential benefits and challenges for various domains and users. In this project, I want to make a program that can combine TTS and sentiment analysis to create a more engaging and interactive experience.

#### DESCRIPTION:
This code is a web app that can convert text to speech and analyze its sentiment using Python and streamlit. It uses the gtts module to generate speech from text, the textblob module to perform sentiment analysis, and the googletrans module to translate text. 

The web app has four main functions: main, language, ask_speed, and convert. The main function is the main logic of the web app and it asks the user to input some text, a language, and a speed option using streamlit widgets. The language function takes the user's choice from a selectbox widget and returns the corresponding language code from a dictionary of languages. 

The ask_speed function takes the user's answer from a radio widget and returns a boolean value for the speed option. The convert function takes the text, language, and speed arguments and creates a gTTS object that saves and displays an audio file of the speech using streamlit widgets. The web app also has a sentiment_detection function that takes the text argument and translates it to English using the Translator class. Then, it uses the TextBlob class to calculate the polarity of the text and displays a string indicating whether the text is neutral, positive, or negative using streamlit widgets. 

#### TO-DO:
- Change text sentiment analysis into emotion detection.
I think it is going to be more awesome if we can see how the text express in each category of emotions, not only knowing it's positive or negative or neutral.

#### LIBRARIES INCLUDE:
I use many libraries to achieve my goal in this project, they are:
- gtts
- streamlit
- googletrans
- textblob