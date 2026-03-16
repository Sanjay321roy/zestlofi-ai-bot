import streamlit as st
import os
import requests
from gtts import gTTS
import urllib.parse

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Sidebar
st.sidebar.title("🤖 Status")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI Dashboard (v2.0)")
    topic = st.text_input("Video Topic", "Pure Heart Devil")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # MISSION 1: SCRIPT (Using a different Free AI API - No API Key Needed)
    if st.button("✍️ 1. Generate AI Script"):
        with st.spinner("AI is thinking..."):
            try:
                # Hum ek free text generator use kar rahe hain jo fail nahi hota
                prompt = f"Write a short 4 line emotional story in Hindi about {topic}. Dark lofi aesthetic."
                api_url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}"
                response = requests.get(api_url)
                if response.status_code == 200:
                    st.session_state.script = response.text
                    st.success("Script Ready!")
                else:
                    st.error("AI Busy hai, ek baar fir click karo.")
            except Exception as e:
                st.error(f"Error: {e}")

    if st.session_state.script:
        st.info(st.session_state.script)
        
        # MISSION 2: VOICE
        if st.button("🎙️ 2. Convert to Voice"):
            with st.spinner("Awaaz ban rahi hai..."):
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
        
        # MISSION 3: IMAGES
        if st.button("🖼️ 3. Generate AI Images"):
            with st.spinner("Visuals loading..."):
                query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k")
                img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true"
                st.image(img_url)
else:
    st.info("Sidebar mein password 'zest123' dalo.")
