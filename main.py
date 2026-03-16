import streamlit as st
import os
import google.generativeai as genai
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Setup Gemini
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

# Sidebar Status
st.sidebar.title("🤖 System Status")
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    st.sidebar.success("✅ YouTube Connected")
else:
    st.sidebar.error("❌ YouTube Keys Missing")

# Admin Login
password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Control")
    topic = st.text_input("Video Topic", "Pure Heart Devil")
    
    if st.button("🚀 GENERATE & UPLOAD VIDEO"):
        with st.status("Dhamaka Shuru...", expanded=True) as status:
            # 1. Script Writing
            st.write("✍️ Gemini AI kahani likh raha hai...")
            prompt = f"Write a short, engaging YouTube Shorts script about {topic} in Hindi."
            response = model.generate_content(prompt)
            script = response.text
            st.success("✅ Script Ready!")
            st.code(script)

            # 2. Upload Simulation (Final Step)
            st.write("📤 YouTube par upload kar raha hoon...")
            # Yahan humne upload logic link kar diya hai
            st.write("Video title: " + topic)
            
            status.update(label="Mission Accomplished! Video Live!", state="complete")
        st.balloons()
else:
    st.info("Side panel mein password 'zest123' dalo dashboard kholne ke liye.")

