import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Setup Gemini with correct model path
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Hum model ko bina version specify kiye call karenge
    model = genai.GenerativeModel('gemini-1.5-flash')

# Sidebar Status
st.sidebar.title("🤖 System Status")
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    st.sidebar.success("✅ YouTube Connected")

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Control")
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if 'script' not in st.session_state:
        st.session_state.script = ""

    if st.button("🚀 GENERATE SCRIPT"):
        with st.status("Gemini is thinking...", expanded=True) as status:
            try:
                prompt = f"Write a 1-minute YouTube Shorts script about {topic} in Hindi. Make it emotional and powerful."
                # Simple generation call
                response = model.generate_content(prompt)
                st.session_state.script = response.text
                status.update(label="✅ Script Generated!", state="complete")
                st.balloons()
            except Exception as e:
                st.error(f"Gemini Error: {e}")

    if st.session_state.script:
        st.subheader("📝 Your AI Script:")
        st.text_area("", st.session_state.script, height=300)
        st.success("Bhai, script taiyar hai! Kya ab iski Awaaz (Audio) banayein?")
else:
    st.info("Sidebar mein password 'zest123' dalo.")
