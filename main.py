import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS

# Page Config
st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Setup - Sabse naya model stable tarike se
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Version fix: 'gemini-1.5-flash' bina kisi extra prefix ke
    model = genai.GenerativeModel('gemini-1.5-flash')

# Sidebar Status & Login
st.sidebar.title("🤖 Master Control")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Dashboard")
    st.write("Bhai, yahan se tera poora automation control hoga.")
    
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    # Session state to store script
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # MISSION 1: SCRIPT
    if st.button("✍️ 1. Generate AI Script"):
        with st.spinner("Gemini is writing..."):
            try:
                prompt = f"Write a 4-line emotional Hindi story about {topic} for YouTube Shorts. Dark lofi style."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                st.success("Script Taiyar!")
            except Exception as e:
                st.error(f"Gemini Error: {e}")

    # MISSION 2: VOICE
    if st.session_state.script:
        st.subheader("📝 Script Content:")
        st.write(st.session_state.script)
        
        if st.button("🎙️ 2. Convert to Voice"):
            with st.spinner("Converting to Audio..."):
                try:
                    tts = gTTS(text=st.session_state.script, lang='hi')
                    tts.save("voice.mp3")
                    audio_file = open("voice.mp3", "rb")
                    st.audio(audio_file.read(), format='audio/mp3')
                    st.balloons()
                except Exception as e:
                    st.error(f"Voice Error: {e}")
else:
    st.info("Side panel mein password 'zest123' dalo.")
