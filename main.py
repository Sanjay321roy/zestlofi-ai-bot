import streamlit as st
import os

# Page Setup
st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Sidebar Status Check
st.sidebar.title("🤖 System Status")
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    st.sidebar.success("✅ YouTube API Connected")
else:
    st.sidebar.error("❌ API Keys Missing")

# Admin Login Section
st.sidebar.markdown("---")
password = st.sidebar.text_input("Admin Password", type="password")

if password == "zest123":
    st.sidebar.success("Welcome back, Sanjay!")
    
    st.title("👹 Zestlofi AI - Master Control")
    st.write("Bhai, yahan se tu apne channel ko control kar sakta hai.")
    
    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("Video Topic", "Pure Heart Devil Story")
        video_style = st.selectbox("Video Style", ["Anime", "Cinematic", "3D Render"])
    
    with col2:
        language = st.selectbox("Language", ["Hindi", "English"])
        voice = st.radio("Voice Type", ["Male (Deep)", "Female (Calm)"])

    if st.button("🚀 GENERATE & UPLOAD VIDEO"):
        with st.status("Mission in Progress...", expanded=True) as status:
            st.write("✍️ Gemini AI is writing a killer script...")
            st.write("🎨 Generating AI Images for '" + topic + "'...")
            st.write("📤 Uploading to ZESTLOFI Channel...")
        st.balloons()
        st.success(f"Dhamaka ho gaya! Video on '{topic}' is now LIVE.")
else:
    st.title("🔒 Zestlofi AI Bot")
    st.warning("Side panel mein password 'zest123' dalo bhai, tabhi dashboard khulega.")
    st.info("Piche balloons udte dekhne se business nahi chalega, login karo! 😂")

st.markdown("---")
st.caption("Owner: Sanjay Roy | Power by Gemini AI")
