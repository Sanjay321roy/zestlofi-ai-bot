import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import urllib.parse

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Setup - Seedha aur Saaf
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Hum seedha gemini-pro use karenge jo 100% stable hai
    model = genai.GenerativeModel('gemini-pro')

# Sidebar
st.sidebar.title("🤖 Status")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI Dashboard")
    
    topic = st.text_input("Video Topic", "Pure Heart Devil")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # 1. SCRIPT
    if st.button("✍️ 1. Generate AI Script"):
        try:
            prompt = f"Write 4 lines emotional Hindi story about {topic}."
            response = model.generate_content(prompt)
            st.session_state.script = response.text
            st.balloons()
        except Exception as e:
            st.error(f"Error: {e}")

    if st.session_state.script:
        st.info(st.session_state.script)
        
        # 2. VOICE
        if st.button("🎙️ 2. Convert to Voice"):
            tts = gTTS(text=st.session_state.script, lang='hi')
            tts.save("voice.mp3")
            st.audio("voice.mp3")
        
        # 3. IMAGES
        if st.button("🖼️ 3. Generate AI Images"):
            query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k")
            img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true"
            st.image(img_url)
else:
    st.info("Sidebar mein password dalo.")
