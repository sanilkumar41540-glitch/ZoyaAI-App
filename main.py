from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import webbrowser, datetime, os

GEMINI_KEY = "PASTE_YOUR_GEMINI_KEY_HERE"

class ZoyaUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.add_widget(Label(text="✨ ZOYA ✨", font_size=32, bold=True, color=(1,0.3,0.8,1), size_hint_y=0.15))
        self.avatar = Label(text="🤖\nI am listening...", font_size=24, size_hint_y=0.25)
        self.add_widget(self.avatar)
        self.chat = Label(text="Hello Abhi! I am ZOYA.\nBoliye, kya karu?", font_size=18, size_hint_y=None, height=200)
        scroll = ScrollView(size_hint_y=0.4)
        scroll.add_widget(self.chat)
        self.add_widget(scroll)
        self.input = TextInput(hint_text="Hey Zoya... kuch bolo...", font_size=18, size_hint_y=0.15, multiline=False)
        self.input.bind(on_text_validate=self.ask_zoya)
        self.add_widget(self.input)
        btn_row = BoxLayout(size_hint_y=0.15, spacing=5)
        btn_row.add_widget(Button(text="ASK", on_press=self.ask_zoya))
        btn_row.add_widget(Button(text="WAKE UP", on_press=self.wakeup))
        btn_row.add_widget(Button(text="YOUTUBE", on_press=lambda x: webbrowser.open("https://youtube.com")))
        btn_row.add_widget(Button(text="TIME", on_press=self.tell_time))
        self.add_widget(btn_row)

    def wakeup(self, inst):
        self.chat.text = "Yes Abhi! I am awake.\nHey Zoya bolne se main jaag gayi!"
        self.avatar.text = "👁️✨\nAWAKE!"

    def tell_time(self, inst):
        now = datetime.datetime.now().strftime("%I:%M %p")
        self.chat.text = f"Abhi time ho raha hai: {now}"

    def ask_zoya(self, inst):
        q = self.input.text.strip().lower()
        if not q: return
        self.input.text = ""
        if "youtube" in q or "video" in q:
            self.chat.text = "YouTube khol rahi hu..."
            webbrowser.open("https://youtube.com")
        elif "time" in q or "baj" in q:
            self.tell_time(None)
        elif "kaun ho" in q or "who are you" in q:
            self.chat.text = "Main ZOYA hu, Abhi ki personal AI assistant. Jarvis jaisi!"
        elif "hello" in q or "hi" in q or "hey" in q:
            self.chat.text = "Hello Abhi! Kaisa hai tu? Bata kya karu?"
        else:
            self.chat.text = f"Tune bola: {q}\n\nGemini Brain ke liye apni API Key main.py me daal. Tab main har sawaal ka jawab dungi!"
        self.avatar.text = "💬\nSpeaking..."

class ZoyaApp(App):
    def build(self):
        return ZoyaUI()

if __name__ == "__main__":
    ZoyaApp().run()
