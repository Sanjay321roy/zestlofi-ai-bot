import requests, os, time, random
from gtts import gTTS
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# --- MERA CONFIG (Sanjay Roy Creations) ---
API_KEY = "AIzaSyA339LTkHKG8257vB7r1_y7l562B1XcE7I"
PEXELS_API = "563492ad6f91700001000001e4034e32766e40998b646c0780249826"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
BG_MUSIC = "bg_music.mp3"
OUTPUT = "/sdcard/Download/Zestlofi_Final.mp4"
TAGS = "#hindi #anime #ai #devil #dark #sanjayroy #shorts #viral"

def get_ai_content():
    print("--- 🤖 Gemini Dialogue Aur Scene Soch Raha Hai... ---")
    prompt = "Write a powerful 4-line dark anime speech in Hindi about pain and power. Also, give a 1-word English keyword for a matching background video (e.g., 'rain', 'fire', 'darkness', 'forest'). Format: Dialogue | Keyword. ONLY Hindi text for dialogue."
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        r = requests.post(GEMINI_URL, json=payload, timeout=15)
        res = r.json()['candidates'][0]['content']['parts'][0]['text'].strip()
        parts = res.split('|')
        return parts[0].strip(), parts[1].strip()
    except:
        return "दर्द को मैंने अपना गहना बना लिया है, अब तबाही से मुझे डर नहीं लगता।", "fire"

def download_ai_video(keyword):
    print(f"--- 🎬 Scene: '{keyword}' Ki Video Dhund Raha Hoon... ---")
    headers = {"Authorization": PEXELS_API}
    url = f"https://api.pexels.com/videos/search?query={keyword}&per_page=1&orientation=portrait"
    try:
        r = requests.get(url, headers=headers)
        v_url = r.json()['videos'][0]['video_files'][0]['link']
        v_data = requests.get(v_url)
        with open("temp_vid.mp4", 'wb') as f: f.write(v_data.content)
        return "temp_vid.mp4"
    except:
        print("Stock video nahi mili, fallback use kar rahe hain.")
        return "temp_vid.mp4"

def make_video(script, v_file):
    print("--- 🎙️ Voiceover Ban Raha Hai... ---")
    tts = gTTS(text=script, lang='hi')
    tts.save("v.mp3")
    
    print("--- ✂️ AI Video Editing Shuru (Neon Red Subtitles)... ---")
    # FFmpeg: Loop video, Mix Music/Voice, Add Red Subtitles & Watermark
    cmd = (f"ffmpeg -y -stream_loop -1 -i {v_file} -i v.mp3 -i {BG_MUSIC} -filter_complex "
           f"\"[1:a]volume=3.5[voice];[2:a]volume=0.2[bg];[voice][bg]amix=inputs=2:duration=first[a];"
           f"[0:v]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,"
           f"drawtext=text='{script}':fontcolor=0xFF3333:fontsize=38:line_spacing=15:x=(w-text_w)/2:y=(h-text_h)/2:box=1:boxcolor=black@0.7,"
           f"drawtext=text='Sanjay Roy Creations':fontcolor=white@0.4:fontsize=22:x=w-tw-20:y=h-th-20\" "
           f"-map 0:v -map '[a]' -c:v libx264 -t 35 -preset fast {OUTPUT}")
    os.system(cmd)

def upload_to_yt(youtube, script):
    print("--- ☁️ YouTube Par Upload Ho Raha Hai... ---")
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"डेविल: {script[:30]}... #Shorts {TAGS}",
                "description": f"{script}\n\nCreadited to: Sanjay Roy Creations\n{TAGS}",
                "categoryId": "1",
                "defaultLanguage": "hi"
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=MediaFileUpload(OUTPUT)
    )
    request.execute()
    print("--- ✅ SUCCESS! Video Live Ho Gayi! ---")

def main():
    # Background music download (ek baar)
    if not os.path.exists(BG_MUSIC):
        print("--- 🎵 Background Music Download Ho Raha Hai... ---")
        music_url = "https://www.chosic.com/wp-content/uploads/2021/07/The-Searching-Dark-Ambient.mp3"
        r = requests.get(music_url)
        with open(BG_MUSIC, 'wb') as f: f.write(r.content)

    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes)
    # Browser na khulne ka jugaad
    credentials = flow.run_local_server(port=8080, prompt='consent', open_browser=False)
    youtube = build("youtube", "v3", credentials=credentials)

    # Loop: 3 Videos ki generation
    for i in range(3):
        print(f"\n🚀 MISSION {i+1} START 🚀")
        script, keyword = get_ai_content()
        v_file = download_ai_video(keyword)
        make_video(script, v_file)
        if os.path.exists(OUTPUT):
            upload_to_yt(youtube, script)
            print("15 Second Break... Agli video ki taiyari.")
            time.sleep(15)

if __name__ == "__main__":
    main()
