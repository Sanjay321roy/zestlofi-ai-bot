import streamlit as st
import os

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹")

# Sidebar Status
st.sidebar.title("🤖 System Status")
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    st.sidebar.success("✅ YouTube Connected")
else:
    st.sidebar.error("❌ Keys Missing")

st.title("👹 Zestlofi AI - Master Control")

# Admin Login
password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.success("Access Granted! Welcome Sanjay.")
    topic = st.text_input("Video Topic", "Pure Heart Devil")
    if st.button("🚀 START AUTOMATION"):
        st.write("Processing... Gemini is writing script...")
        st.balloons()
else:
    st.info("Side panel mein password 'zest123' dalo dashboard kholne ke liye.")
