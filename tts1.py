import streamlit as st
import gtts
from playsound import playsound
import os

def gtts_speak(language, tld, speech):
    tts = gtts.gTTS(speech, lang=language, tld=tld)
    tts.save("hello.mp3")
    playsound("hello.mp3")
    os.remove("hello.mp3")  # Clean up the file after playing

st.title("Text-to-Speech Application")

engine_choice = st.radio("Choose Speech Synthesis Engine", ["gtts"])

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
