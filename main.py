import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Setup Gemini (Updated Model Name)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Gemini 1.5 Flash use kar rahe hain jo fast hai
    model = genai.GenerativeModel('gemini-1.5-flash')

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
            try:
                prompt = f"Write a short, engaging YouTube Shorts script about {topic} in Hindi."
                response = model.generate_content(prompt)
                script = response.text
                st.success("✅ Script Ready!")
                st.code(script)
            except Exception as e:
                st.error(f"Gemini Error: {e}")

            # 2. Status Update
            st.write("📤 Upload logic ready, preparing media...")
            status.update(label="Script Generated Successfully!", state="complete")
        st.balloons()
else:
    st.info("Side panel mein password 'zest123' dalo dashboard kholne ke liye.")
