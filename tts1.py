import streamlit as st
import gtts
from playsound import playsound
import pyttsx3
import os

def gtts_speak(language, tld, speech):
    tts = gtts.gTTS(speech, lang=language, tld=tld)
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove("hello.mp3")  # Clean up the file after playing

def pyttsx3_speak(voice_choice, speech):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if voice_choice == '1':
        engine.setProperty('voice', voices[0].id) 
    elif voice_choice == '2':
        engine.setProperty('voice', voices[1].id) 
    else:
        engine.setProperty('voice', voices[0].id)
    
    engine.setProperty('rate', 150)
    engine.say(speech)
    engine.runAndWait()
    engine.stop()

st.title("Text-to-Speech Application")

engine_choice = st.radio("Choose Speech Synthesis Engine", ["gtts", "pyttsx3"])

if engine_choice == "gtts":
    st.subheader("Google Text-to-Speech (gtts)")
    language_preference = st.selectbox("Choose language", ["english", "hindi"])
    
    if language_preference == "hindi":
        language = "hi"
        tld = "co.in"
    else:
        language = "en"
        accent_preference = st.selectbox("Choose accent", ["us", "uk", "india", "australia"])
        
        if accent_preference == "uk":
            tld = "co.uk"
        elif accent_preference == "india":
            tld = "co.in"
        elif accent_preference == "australia":
            tld = "com.au"
        else:
            tld = "com"
    
    speech = st.text_area("Enter text")
    if st.button("Play Speech"):
        gtts_speak(language, tld, speech)
        st.success("Speech played with Google TTS.")

elif engine_choice == "pyttsx3":
    st.subheader("pyttsx3")
    voice_choice = st.selectbox("Choose voice", ["1: Male", "2: Female"])
    speech = st.text_area("Enter text")
    
    if st.button("Play Speech"):
        pyttsx3_speak(voice_choice, speech)
        st.success("Speech played with pyttsx3.")
