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
