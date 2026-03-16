import streamlit as st
import os
import requests
from gtts import gTTS
import urllib.parse
import random

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Sidebar
st.sidebar.title("👹 Zestlofi Master")
if os.path.exists("token.json"):
    st.sidebar.success("✅ System Independent")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Independent Dashboard")
    
    topic = st.text_input("Topic", "Pure Heart Devil")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # 1. BRAIN (No Gemini, No Google API)
    if st.button("✍️ 1. Start Brain"):
        with st.status("Engine thinking...", expanded=False) as status:
            try:
                prompt = f"Write 4 lines emotional Hindi story about {topic}. Dark aesthetic."
                api_url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}?model=openai&cache=false"
                response = requests.get(api_url)
                st.session_state.script = response.text
                status.update(label="✅ Brain Ready", state="complete")
            except:
                st.error("Try again!")

    if st.session_state.script:
        st.info(st.session_state.script)
        
        # 2. VOICE
        if st.button("🎙️ 2. Start Voice"):
            with st.spinner("Converting..."):
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
        
        # 3. VISUALS (Full Control Fix)
        if st.button("🖼️ 3. Start Visuals"):
            # Har baar ek naya seed taaki nayi photo aaye
            seed = random.randint(1, 999999)
            query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k cinematic")
            img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true&seed={seed}"
            
            with st.status("Rendering Image...", expanded=True) as status:
                # Direct image loading logic
                st.image(img_url, use_container_width=True)
                # Backup display if st.image fails
                st.markdown(f'<img src="{img_url}" width="100%">', unsafe_allow_ Harris=True)
                status.update(label="🎨 Visuals Live!", state="complete")
else:
    st.info("Password dalo bhai.")
