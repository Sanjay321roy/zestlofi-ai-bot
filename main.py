import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Gemini Auto-Selection Logic
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Ye block khud dhoondhega kaunsa model chal raha hai
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Pehla working model uthayega (usually gemini-pro)
        selected_model = models[0] if models else "gemini-pro"
        model = genai.GenerativeModel(selected_model)
    except:
        model = genai.GenerativeModel('gemini-pro')

# Sidebar Status
st.sidebar.title("🤖 Status")
password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Dashboard")
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    if st.button("✍️ 1. Generate AI Script"):
        with st.status("Dhoondh raha hoon working AI model...", expanded=True) as status:
            try:
                prompt = f"Write a 4-line emotional Hindi story about {topic} for YouTube Shorts."
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                status.update(label="✅ Script Ready!", state="complete")
                st.balloons()
            except Exception as e:
                st.error(f"Abhi bhi error hai: {e}. Bhai, ek baar Google AI Studio mein ja kar naya API key bana kar 'Secrets' mein update kar.")

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
