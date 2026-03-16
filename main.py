import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import urllib.parse

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Auto-Selection
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(models[0] if models else "gemini-pro")
    except:
        model = genai.GenerativeModel('gemini-pro')

# Sidebar Status
st.sidebar.title("🤖 Status")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")
else:
    st.sidebar.error("❌ YouTube Disconnected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Dashboard")
    topic = st.text_input("Video Topic", "Lonely Devil in Rain")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    # MISSION 1: SCRIPT
    if st.button("✍️ 1. Generate AI Script"):
        try:
            prompt = f"Write a 4-line emotional Hindi story about {topic}. Dark lofi style."
            response = model.generate_content(prompt)
            st.session_state.script = response.text
            st.balloons()
        except Exception as e:
            st.error(f"Error: {e}")

    if st.session_state.script:
        st.subheader("📝 Script:")
        st.write(st.session_state.script)
        
        col1, col2 = st.columns(2)
        
        # MISSION 2: VOICE
        with col1:
            if st.button("🎙️ 2. Convert to Voice"):
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
        
        # MISSION 3: IMAGES
        with col2:
            if st.button("🖼️ 3. Generate AI Images"):
                st.subheader("🎨 AI Visuals:")
                # Topic ko URL safe bana rahe hain
                query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic high quality")
                img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true"
                st.image(img_url, caption="Generated for your Short", use_container_width=True)
                st.success("Bhai, image dekho! Kya mast vibe hai?")
else:
    st.info("Sidebar mein password dalo.")
