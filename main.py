import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Google AI Setup
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Sabse stable model call
    model = genai.GenerativeModel('gemini-pro')

# Sidebar for Status
st.sidebar.title("🤖 System Status")

# Check YouTube Keys
yt_status = "❌ Missing"
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    yt_status = "✅ YouTube Connected"
    st.sidebar.success(yt_status)
else:
    st.sidebar.error(yt_status)

# Login
password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Control")
    st.write(f"System Status: {yt_status}")
    
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if st.button("🚀 GENERATE SCRIPT"):
        with st.spinner("Gemini is thinking..."):
            try:
                prompt = f"Write a short YouTube Shorts script about {topic} in Hindi."
                response = model.generate_content(prompt)
                st.subheader("📝 Your Script:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Sidebar mein password 'zest123' dalo.")
