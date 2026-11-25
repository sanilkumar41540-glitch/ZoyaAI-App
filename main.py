from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#050B1A")

class ZoyaAI(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=25
        )

        title = Label(
            text="[b]ZOYA AI[/b]",
            markup=True,
            font_size="38sp",
            color=(0, 0.85, 1, 1)
        )

        avatar = Label(
            text="◉",
            font_size="110sp",
            color=(0, 0.85, 1, 1)
        )

        status = Label(
            text="YOUR AI ASSISTANT\nGemini Brain • Voice Ready",
            font_size="17sp",
            color=(0.5, 0.85, 1, 1)
        )

        button = Button(
            text="ACTIVATE ZOYA",
            font_size="20sp",
            size_hint=(1, 0.2),
            background_color=(0, 0.65, 1, 1)
        )

        layout.add_widget(title)
        layout.add_widget(avatar)
        layout.add_widget(status)
        layout.add_widget(button)

        return layout

ZoyaAI().run()
