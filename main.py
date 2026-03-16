import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Zestlofi AI Master", page_icon="👹", layout="wide")

# Sidebar Status
st.sidebar.title("🤖 System Status")
if os.path.exists("token.json") and os.path.exists("client_secret.json"):
    st.sidebar.success("✅ YouTube Connected")

# Setup Gemini with Auto-Model Selection
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Check available models automatically
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Pehla working model utha lo
        model_name = available_models[0] if available_models else "models/gemini-pro"
        model = genai.GenerativeModel(model_name)
    except:
        model = genai.GenerativeModel('gemini-pro')

password = st.sidebar.text_input("Enter Password", type="password")

if password == "zest123":
    st.title("👹 Zestlofi AI - Master Control")
    topic = st.text_input("Video Topic", "Pure Heart Devil Story")
    
    if st.button("🚀 GENERATE SCRIPT"):
        with st.status("Searching for active AI model...", expanded=True) as status:
            try:
                prompt = f"Write a short, powerful YouTube Shorts script about {topic} in Hindi."
                response = model.generate_content(prompt)
                st.subheader("📝 Your Script:")
                st.write(response.text)
                status.update(label="✅ Success!", state="complete")
                st.balloons()
            except Exception as e:
                st.error(f"Last try failed: {e}")
                st.info("Bhai, ek baar API key check karo ya thoda wait karo, Google API kabhi kabhi time leti hai.")
else:
    st.info("Sidebar mein password 'zest123' dalo.")
