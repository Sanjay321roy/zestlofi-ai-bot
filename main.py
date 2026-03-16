import streamlit as st
import os
import requests
from gtts import gTTS
import urllib.parse
import random

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Sidebar - YouTube Status Logic (Apna check)
st.sidebar.title("👹 Zestlofi Control")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Link: Active")
else:
    st.sidebar.error("❌ YouTube Link: Offline")

password = st.sidebar.text_input("Master Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Independent Dashboard")
    
    topic = st.text_input("Enter Topic", "Pure Heart Devil")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # 1. BRAIN ENGINE
    if st.button("✍️ 1. Generate Script"):
        try:
            prompt = f"Write a 4 line emotional Hindi story about {topic}. Dark aesthetic."
            # Hum isse apni tarah se process kar rahe hain
            api_url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}?model=openai"
            response = requests.get(api_url)
            st.session_state.script = response.text
            st.success("Brain Ready")
        except:
            st.error("Engine Fault")

    if st.session_state.script:
        st.info(st.session_state.script)
        
        # 2. VOICE ENGINE
        if st.button("🎙️ 2. Generate Voice"):
            tts = gTTS(text=st.session_state.script, lang='hi')
            tts.save("voice.mp3")
            st.audio("voice.mp3")
        
        # 3. VISUAL ENGINE (The Final Fix)
        if st.button("🖼️ 3. Generate Visuals"):
            # Image ko force load karne ke liye random seed
            seed = random.randint(1, 1000000)
            query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k")
            img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true&seed={seed}"
            
            st.write("### 🎨 Your Visual:")
            # Hum image ko seedha display karenge
            st.image(img_url, use_container_width=True)
            st.success("Visuals Created")
else:
    st.info("Sidebar mein password dalo.")
