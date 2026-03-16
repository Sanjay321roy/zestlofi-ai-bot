import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Auto-Selection Logic
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        model = genai.GenerativeModel(models[0] if models else "gemini-pro")
    except:
        model = genai.GenerativeModel('gemini-pro')

# Sidebar Status (YouTube Connection Check)
st.sidebar.title("🤖 Status")
if os.path.exists("token.json"):
    st.sidebar.success("✅ YouTube Connected")
else:
    st.sidebar.error("❌ YouTube Disconnected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Dashboard")
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    if st.button("✍️ 1. Generate AI Script"):
        with st.spinner("Gemini is thinking..."):
            try:
                prompt = f"Write a 4-line emotional Hindi story about {topic} for YouTube Shorts."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")

    if st.session_state.script:
        st.subheader("📝 Script Content:")
        st.write(st.session_state.script)
        
        if st.button("🎙️ 2. Convert to Voice"):
            try:
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
            except Exception as e:
                st.error(f"Voice Error: {e}")
else:
    st.info("Sidebar mein password dalo.")
