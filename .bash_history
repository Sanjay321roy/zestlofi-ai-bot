            time.sleep(60)

if __name__ == "__main__": main()
EOF

python devil_bot.py
rm bg_music.mp3 v.mp3 final_output.mp4; cat << 'EOF' > devil_bot.py
import requests, os, time, random
from gtts import gTTS
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
BG_MUSIC = "bg_music.mp3"
OUTPUT = "final_output.mp4"

def get_ai_stuff():
    moods = ["Darkness", "Revenge", "Pain", "Ego"]
    m = random.choice(moods)
    print(f"--- 🤖 Gemini: {m} dialogue likh raha hai... ---")
    prompt = f"Write a unique 4-line dark anime dialogue in Hindi about {m}. Format: Dialogue | Keyword"
    try:
        r = requests.post(GEMINI_URL, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15).json()
        res = r['candidates'][0]['content']['parts'][0]['text'].strip()
        return res.split('|') if "|" in res else [res, "darkness"]
    except: return "अंधेरा ही मेरी ताकत है।", "fire"

def download_assets(kw):
    print(f"--- 🎬 Scene: '{kw}' download ho raha hai... ---")
    headers = {"Authorization": PEXELS_API}
    try:
        # Video
        v_res = requests.get(f"https://api.pexels.com/videos/search?query={kw}&per_page=10&orientation=portrait", headers=headers).json()
        v_url = random.choice(v_res['videos'])['video_files'][0]['link']
        with open("temp.mp4", 'wb') as f: f.write(requests.get(v_url).content)
        # Nayi Fresh Music File (Link Updated)
        if not os.path.exists(BG_MUSIC) or os.path.getsize(BG_MUSIC) < 1000:
            m_url = "https://www.bensound.com/bensound-music/bensound-creepy.mp3" 
            print("--- 🎵 Nayi Music Download Ho Rahi Hai... ---")
            with open(BG_MUSIC, 'wb') as f: f.write(requests.get(m_url).content)
        return True
    except: return False

def edit_and_upload(youtube, script):
    print("--- ✂️ Editing Video (FFmpeg)... ---")
    gTTS(text=script, lang='hi').save("v.mp3")
    # Neon Style Subtitles
    cmd = (f"ffmpeg -y -stream_loop -1 -i temp.mp4 -i v.mp3 -i {BG_MUSIC} -filter_complex "
           f"\"[1:a]volume=3.5[voice];[2:a]volume=0.3[bg];[voice][bg]amix=inputs=2:duration=first[a];"
           f"[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
           f"drawtext=text='{script}':fontcolor=red:fontsize=32:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.6\" "
           f"-map 0:v -map '[a]' -c:v libx264 -t 25 -preset superfast {OUTPUT}")
    os.system(cmd)
    
    if os.path.exists(OUTPUT):
        print("--- ☁️ YouTube Uploading... ---")
        media = MediaFileUpload(OUTPUT)
        youtube.videos().insert(part="snippet,status", body={
            "snippet": {"title": f"डेविल: {script[:30]}... #Shorts", "description": script, "categoryId": "1"},
            "status": {"privacyStatus": "public"}
        }, media_body=media).execute()
        return True
    return False

def main():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None
    if os.path.exists('token.json'): creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
            creds = flow.run_local_server(port=8090, prompt='consent', open_browser=False)
        with open('token.json', 'w') as token: token.write(creds.to_json())
    
    youtube = build("youtube", "v3", credentials=creds)
    for i in range(5):
        print(f"\n🚀 MISSION {i+1} START")
        script, kw = get_ai_stuff()
        if download_assets(kw):
            if edit_and_upload(youtube, script): print(f"--- ✅ Mission {i+1} Live! ---")
            else: print("--- ❌ Editing Failed ---")
        if i < 4:
            print("--- 1 Minute ka break ---")
            time.sleep(60)

if __name__ == "__main__": main()
EOF

python devil_bot.py
rm bg_music.mp3 v.mp3 final_output.mp4; cat << 'EOF' > devil_bot.py
import requests, os, time, random
from gtts import gTTS
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
OUTPUT = "final_output.mp4"

def get_ai_stuff():
    moods = ["Darkness", "Revenge", "Pain", "Ego"]
    m = random.choice(moods)
    print(f"--- 🤖 Gemini: {m} dialogue likh raha hai... ---")
    prompt = f"Write a unique 4-line dark anime dialogue in Hindi about {m}. Format: Dialogue | Keyword"
    try:
        r = requests.post(GEMINI_URL, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15).json()
        res = r['candidates'][0]['content']['parts'][0]['text'].strip()
        return res.split('|') if "|" in res else [res, "darkness"]
    except: return "अंधेरा ही मेरी ताकत है।", "fire"

def download_video(kw):
    print(f"--- 🎬 Scene: '{kw}' download ho raha hai... ---")
    headers = {"Authorization": PEXELS_API}
    try:
        v_res = requests.get(f"https://api.pexels.com/videos/search?query={kw}&per_page=10&orientation=portrait", headers=headers).json()
        v_url = random.choice(v_res['videos'])['video_files'][0]['link']
        with open("temp.mp4", 'wb') as f: f.write(requests.get(v_url).content)
        return True
    except: return False

def edit_and_upload(youtube, script):
    print("--- ✂️ Editing Video (No-Fail Mode)... ---")
    gTTS(text=script, lang='hi').save("v.mp3")
    
    # Bina background music wala safe command
    cmd = (f"ffmpeg -y -stream_loop -1 -i temp.mp4 -i v.mp3 -filter_complex "
           f"\"[1:a]volume=4.0[voice];"
           f"[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
           f"drawtext=text='{script}':fontcolor=white:fontsize=32:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.6\" "
           f"-map 0:v -map 1:a -c:v libx264 -t 25 -preset superfast {OUTPUT}")
    
    os.system(cmd)
    
    if os.path.exists(OUTPUT):
        print("--- ☁️ YouTube Uploading... ---")
        media = MediaFileUpload(OUTPUT)
        youtube.videos().insert(part="snippet,status", body={
            "snippet": {"title": f"डेविल: {script[:30]}... #Shorts", "description": script, "categoryId": "1"},
            "status": {"privacyStatus": "public"}
        }, media_body=media).execute()
        return True
    return False

def main():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None
    if os.path.exists('token.json'): creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
            creds = flow.run_local_server(port=8090, prompt='consent', open_browser=False)
        with open('token.json', 'w') as token: token.write(creds.to_json())
    
    youtube = build("youtube", "v3", credentials=creds)
    for i in range(5):
        print(f"\n🚀 MISSION {i+1} START")
        script, kw = get_ai_stuff()
        if download_video(kw):
            if edit_and_upload(youtube, script): print(f"--- ✅ Mission {i+1} Live! ---")
            else: print("--- ❌ Editing Failed ---")
        if i < 4:
            print("--- 1 Minute ka break ---")
            time.sleep(60)

if __name__ == "__main__": main()
EOF

python devil_bot.py
cat << 'EOF' > devil_bot.py
import requests, os, time, random
from gtts import gTTS
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# --- CONFIG ---
API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
OUTPUT = "final_output.mp4"

def get_unique_ai_content():
    # Har baar alag mood taaki Gemini repeat na kare
    moods = ["Dark Revenge", "Lonely Soul", "God Mode", "Broken Heart", "Villain Speech"]
    selected_mood = random.choice(moods)
    print(f"--- 🤖 Gemini: {selected_mood} mood par naya dialogue soch raha hai... ---")
    
    prompt = f"Write a unique 4-line dark anime dialogue in Hindi about {selected_mood}. Format: Dialogue | Keyword (English 1 word for video background)"
    
    try:
        r = requests.post(GEMINI_URL, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15).json()
        res = r['candidates'][0]['content']['parts'][0]['text'].strip()
        if "|" in res:
            p = res.split('|')
            return p[0].strip(), p[1].strip()
        return res, "darkness"
    except:
        return "अंधेरा ही मेरा घर है।", "fire"

def download_random_video(kw):
    # Har baar keyword ke base par naya scene dhundega
    print(f"--- 🎬 Scene: '{kw}' ki nayi clip dhund raha hoon... ---")
    headers = {"Authorization": PEXELS_API}
    if os.path.exists("temp.mp4"): os.remove("temp.mp4")
    
    try:
        url = f"https://api.pexels.com/videos/search?query={kw}&per_page=20&orientation=portrait"
        r = requests.get(url, headers=headers, timeout=15).json()
        v_list = r['videos']
        v_url = random.choice(v_list)['video_files'][0]['link']
        with open("temp.mp4", 'wb') as f: f.write(requests.get(v_url).content)
        return "temp.mp4"
    except:
        return None

def edit_and_upload(youtube, script, v_file):
    if not v_file: return False
    print("--- ✂️ Editing Video (Unique Scene)... ---")
    gTTS(text=script, lang='hi').save("v.mp3")
    
    cmd = (f"ffmpeg -y -i {v_file} -i v.mp3 -filter_complex "
           f"\"[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
           f"drawtext=text='{script}':fontcolor=white:fontsize=32:line_spacing=10:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.6[v]\" "
           f"-map \"[v]\" -map 1:a -c:v libx264 -t 25 -preset superfast {OUTPUT}")
    os.system(cmd)
    
    if os.path.exists(OUTPUT):
        print("--- ☁️ YouTube Uploading... ---")
        media = MediaFileUpload(OUTPUT)
        youtube.videos().insert(part="snippet,status", body={
            "snippet": {"title": f"डेविल: {script[:30]}... #Shorts", "description": script, "categoryId": "1"},
            "status": {"privacyStatus": "public"}
        }, media_body=media).execute()
        return True
    return False

def main():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None
    if os.path.exists('token.json'): creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
            creds = flow.run_local_server(port=8090, prompt='consent', open_browser=False)
        with open('token.json', 'w') as token: token.write(creds.to_json())
    
    youtube = build("youtube", "v3", credentials=creds)
    
    for i in range(5):
        print(f"\n🚀 MISSION {i+1} START")
        script, kw = get_unique_ai_content()
        v_file = download_random_video(kw)
        if edit_and_upload(youtube, script, v_file):
            print(f"--- ✅ Mission {i+1} Success! Video Uploaded. ---")
        
        if i < 4:
            print("--- 1 Minute ka break (Nayi video ki taiyari) ---")
            time.sleep(60)

if __name__ == "__main__": main()
EOF

python devil_bot.py
cat << 'EOF' > devil_bot.py
import requests, os, time, random
from gtts import gTTS
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# --- CONFIG ---
API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
OUTPUT = "final_output.mp4"

def get_unique_ai_content():
    moods = ["Revenge", "Darkness", "Broken Heart", "Warrior Ego", "Pain", "Villain Origin"]
    selected_mood = random.choice(moods)
    print(f"--- 🤖 Gemini: {selected_mood} par naya dialogue soch raha hai... ---")
    prompt = f"Write a unique 4-line dark anime dialogue in Hindi about {selected_mood}. Format: Dialogue | Keyword"
    try:
        r = requests.post(GEMINI_URL, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=15).json()
        res = r['candidates'][0]['content']['parts'][0]['text'].strip()
        if "|" in res:
            p = res.split('|')
            return p[0].strip(), p[1].strip()
        return res, "darkness"
    except: return "दर्द ही मेरा इकलौता साथी है।", "darkness"

def download_video(kw):
    print(f"--- 🎬 Scene: '{kw}' ki unique clip dhund raha hoon... ---")
    headers = {"Authorization": PEXELS_API}
    try:
        url = f"https://api.pexels.com/videos/search?query={kw}&per_page=30&orientation=portrait"
        r = requests.get(url, headers=headers).json()
        v_url = random.choice(r['videos'])['video_files'][0]['link']
        with open("temp.mp4", 'wb') as f: f.write(requests.get(v_url).content)
        return True
    except: return False

def edit_and_upload(youtube, script):
    print("--- ✂️ Editing Video... ---")
    gTTS(text=script, lang='hi').save("v.mp3")
    if os.path.exists(OUTPUT): os.remove(OUTPUT)
    
    cmd = (f"ffmpeg -y -i temp.mp4 -i v.mp3 -filter_complex "
           f"\"[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
           f"drawtext=text='{script}':fontcolor=white:fontsize=32:line_spacing=10:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.6[v]\" "
           f"-map \"[v]\" -map 1:a -c:v libx264 -t 25 -preset superfast {OUTPUT}")
    os.system(cmd)
    
    if os.path.exists(OUTPUT):
        print("--- ☁️ YouTube Uploading... ---")
        media = MediaFileUpload(OUTPUT)
        youtube.videos().insert(part="snippet,status", body={
            "snippet": {"title": f"डेविल: {script[:30]}... #Shorts", "description": script, "categoryId": "1"},
            "status": {"privacyStatus": "public"}
        }, media_body=media).execute()
        return True
    return False

def main():
    # Authentication Setup
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
            creds = flow.run_local_server(port=8090, prompt='consent', open_browser=False)
        with open('token.json', 'w') as token: token.write(creds.to_json())
    
    youtube = build("youtube", "v3", credentials=creds)

    # 30 DAYS LOOP (5 Videos Per Day)
    for day in range(1, 31):
        print(f"\n📅 DAY {day} OF 30 - MISSION STARTED")
        for i in range(1, 6):
            print(f"\n🚀 VIDEO {i} OF 5 (Day {day})")
            script, kw = get_unique_ai_content()
            if download_video(kw):
                if edit_and_upload(youtube, script):
                    print(f"✅ Day {day}, Video {i} Live!")
                else: print("❌ Editing Failed.")
            
            if i < 5: # Agli video ke liye 3 ghante ka gap
                print("--- Next video in 3 hours... Bot is active. ---")
                time.sleep(10800)
        
        print(f"--- Day {day} Complete. Sleeping until tomorrow... ---")
        time.sleep(28800) # Din khatam hone par 8 ghante ka extra rest

if __name__ == "__main__": main()
EOF

python devil_bot.py
pip install kivy kivymd
gcat << 'EOF' > dashboard.py
import os, time

def show_dashboard():
    os.system('clear')
    print("="*40)
    print("      ZESTLOFI AI - BUSINESS PANEL      ")
    print("="*40)
    print(f"  [+] Status: ACTIVE")
    print(f"  [+] Today's Uploads: 2/5")
    print(f"  [+] Estimated Earnings: $0.45")
    print(f"  [+] Next Video: In 2h 45m")
    print("-"*40)
    print("  1. Start Bot")
    print("  2. Change Niche (Anime/Motivation)")
    print("  3. Check YouTube Stats")
    print("  4. Build APK (App)")
    print("  5. Exit")
    print("-"*40)

show_dashboard()
EOF

python dashboard.py
cat << 'EOF' > dashboard.py
import os, time

def show_dashboard():
    os.system('clear')
    print("="*40)
    print("      ZESTLOFI AI - BUSINESS PANEL      ")
    print("="*40)
    print(f"  [+] Status: ACTIVE")
    print(f"  [+] Today's Uploads: 2/5")
    print(f"  [+] Estimated Earnings: $0.45")
    print(f"  [+] Next Video: In 2h 45m")
    print("-"*40)
    print("  1. Start Bot")
    print("  2. Change Niche (Anime/Motivation)")
    print("  3. Check YouTube Stats")
    print("  4. Build APK (App)")
    print("  5. Exit")
    print("-"*40)

show_dashboard()
EOF

python dashboard.py
cat << 'EOF' > main.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
import threading
import os

def run_bot_logic():
    print("Bot starting in background...")
    os.system("python devil_bot.py")

class ZestlofiAI(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"
        screen = MDScreen()
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)
        toolbar = MDTopAppBar(title="Zestlofi AI - Business App")
        self.status_label = MDLabel(
            text="Status: Ready to Earn 💸",
            halign="center",
            font_style="H5"
        )
        start_btn = MDRaisedButton(
            text="START AUTOMATION",
            pos_hint={"center_x": .5},
            size_hint=(.8, .1),
            on_release=self.start_automation
        )
        layout.add_widget(toolbar)
        layout.add_widget(self.status_label)
        layout.add_widget(start_btn)
        screen.add_widget(layout)
        return screen

    def start_automation(self, instance):
        self.status_label.text = "🚀 Bot is Running..."
        threading.Thread(target=run_bot_logic).start()

if __name__ == "__main__":
    ZestlofiAI().run()
EOF

cat << 'EOF' > devil_bot.py
import requests, os, time, random
from gtts import gTTS
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"

def main():
    # Yahan tumhara poora upload logic aayega jo pehle diya tha
    print("Bot Logic Running...")
    # ... (baaki code)
    
if __name__ == "__main__":
    main()
EOF

cp main.py devil_bot.py client_secret.json /sdcard/Download/
cat << 'EOF' > requirements.txt
streamlit
google-api-python-client
google-auth-oauthlib
requests
gtts
EOF

cp requirements.txt /sdcard/Download/
