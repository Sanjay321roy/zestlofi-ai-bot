import streamlit as st
import os
import json
import requests
from gtts import gTTS
import urllib.parse
import random

# --- DUKAN KI SURAKSHA (Setup) ---
if not os.path.exists("assets"):
    os.makedirs("assets")
if not os.path.exists("zest_db.json"):
    with open("zest_db.json", "w") as f:
        json.dump({"scripts": [], "voice_count": 0}, f)

def save_to_db(topic, script):
    with open("zest_db.json", "r+") as f:
        data = json.load(f)
        data["scripts"].append({"topic": topic, "content": script})
        f.seek(0)
        json.dump(data, f)

st.set_page_config(page_title="Zestlofi Fortress", page_icon="👹", layout="wide")

st.sidebar.title("👹 Zestlofi Control")
password = st.sidebar.text_input("Master Password", type="password")

if password == "zest123":
    st.title("🛡️ Zestlofi AI - The Fortress v1.5")
    
    tab1, tab2 = st.tabs(["🚀 Generator", "📦 My Warehouse (Godaam)"])

    with tab1:
        topic = st.text_input("New Project Topic", "Dark Devil")
        
        if st.button("✍️ Create & Save Everything"):
            with st.spinner("Apni Dukaan mein saaman bhar raha hoon..."):
                # 1. Script Generation
                try:
                    prompt = f"Write 4 lines emotional Hindi story about {topic}."
                    script = requests.get(f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}").text
                    save_to_db(topic, script)
                    st.session_state.last_script = script
                except:
                    st.error("API Error, but checking database...")

                # 2. Voice Generation (Local Asset)
                tts = gTTS(text=st.session_state.last_script, lang='hi')
                voice_path = f"assets/{topic.replace(' ', '_')}.mp3"
                tts.save(voice_path)
                
                # 3. Image Generation (Local Asset)
                seed = random.randint(1, 9999)
                img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(topic)}?width=1080&height=1920&seed={seed}"
                img_data = requests.get(img_url).content
                img_path = f"assets/{topic.replace(' ', '_')}.jpg"
                with open(img_path, "wb") as f:
                    f.write(img_data)
                
                st.success("Everything saved in your permanent warehouse!")

    with tab2:
        st.header("📦 Your Permanent Assets")
        if os.path.exists("zest_db.json"):
            with open("zest_db.json", "r") as f:
                data = json.load(f)
                for item in reversed(data["scripts"]):
                    with st.expander(f"Topic: {item['topic']}"):
                        st.write(item['content'])
                        local_img = f"assets/{item['topic'].replace(' ', '_')}.jpg"
                        local_voice = f"assets/{item['topic'].replace(' ', '_')}.mp3"
                        if os.path.exists(local_img):
                            st.image(local_img, width=300)
                        if os.path.exists(local_voice):
                            st.audio(local_voice)
else:
    st.info("Password please.")
