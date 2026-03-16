import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import base64

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

# Sidebar
st.sidebar.title("🤖 Status")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Voice Lab")
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # 1. Generate Script
    if st.button("✍️ 1. Generate Script"):
        with st.spinner("Gemini is writing..."):
            try:
                prompt = f"Write a very short 30-40 second YouTube Shorts script about {topic} in Hindi. Emotional and dark lofi style."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                st.success("Script Taiyar!")
            except Exception as e:
                st.error(f"Error: {e}")

    if st.session_state.script:
        st.text_area("Script Content", st.session_state.script, height=150)
        
        # 2. Generate Voice
        if st.button("🎙️ 2. Convert to Voice"):
            with st.spinner("Converting to Hindi Voice..."):
                try:
                    tts = gTTS(text=st.session_state.script, lang='hi')
                    tts.save("voice.mp3")
                    
                    # Audio Player
                    audio_file = open("voice.mp3", "rb")
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3')
                    st.success("Bhai, awaaz suno! Mast hai?")
                except Exception as e:
                    st.error(f"Voice Error: {e}")
else:
    st.info("Sidebar mein password dalo.")
