import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS
import urllib.parse

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        model = genai.GenerativeModel('gemini-pro')

# Sidebar Status
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
        # Gemini jaisa loading niche dikhega
        with st.status("Gemini is writing your story...", expanded=False) as status:
            try:
                prompt = f"Write a 4-line emotional Hindi story about {topic}. Dark lofi style."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                status.update(label="✅ Script Ready!", state="complete")
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")

    if st.session_state.script:
        st.subheader("📝 Script Content:")
        st.info(st.session_state.script)
        
        # MISSION 2: VOICE
        if st.button("🎙️ 2. Convert to Voice"):
            with st.spinner("Creating AI Voiceover..."):
                tts = gTTS(text=st.session_state.script, lang='hi')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
        
        # MISSION 3: IMAGES (Fixing Visibility)
        if st.button("🖼️ 3. Generate AI Images"):
            # Niche loading dikhayega
            with st.status("Designing your Visuals...", expanded=True) as status:
                query = urllib.parse.quote(f"{topic} dark lofi anime aesthetic 4k")
                img_url = f"https://image.pollinations.ai/prompt/{query}?width=1080&height=1920&nologo=true"
                # Seed use kar rahe taaki image force load ho
                st.image(img_url, caption="Shorts Visual", use_container_width=True)
                status.update(label="🎨 Image Generated Successfully!", state="complete")
else:
    st.info("Sidebar mein password 'zest123' dalo.")
