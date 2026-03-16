import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import urllib.parse

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Setup - Sabse Safe Tareeka
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # 404 se bachne ke liye direct stable name use kar rahe hain
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        model = genai.GenerativeModel('gemini-pro')

# Sidebar
st.sidebar.title("🤖 Master Control")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Dashboard")
    
    topic = st.text_input("Video Topic", "Lonely Devil in Rain")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # MISSION 1: SCRIPT
    if st.button("✍️ 1. Generate AI Script"):
        with st.status("Gemini is thinking...", expanded=False) as status:
            try:
                prompt = f"Write a 4-line emotional Hindi story about {topic}. Dark lofi style."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                status.update(label="✅ Script Ready!", state="complete")
            except Exception as e:
                # Agar 404 aaye toh hum models/ prefix ke saath try karenge backup mein
                try:
                    model_backup = genai.GenerativeModel('models/gemini-pro')
                    response = model_backup.generate_content(prompt)
                    st.session_state.script = response.text
                    status.update(label="✅ Script Ready (Backup)!", state="complete")
                except:
                    st.error(f"Error: {e}")

    if st.session_state.script:
        st.info(st.session_state.script)
        
        # MISSION 2: VOICE
        if st.button("🎙️ 2. Convert to Voice"):
            with st.spinner("AI Awaaz ban rahi hai..."):
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
        
        # MISSION 3: IMAGES
        if st.button("🖼️ 3. Generate AI Images"):
            with st.status("Visuals loading...", expanded=True) as status:
                query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k")
                # Image ko seedha direct URL se display kar rahe bina kisi display logic ke
                img_tag = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true"
                st.image(img_tag)
                status.update(label="🎨 Visuals Ready!", state="complete")
else:
    st.info("Sidebar mein password dalo.")
