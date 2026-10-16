from kivy.app import App
from kivy.uix.button import Button


class traktorApp(App):
    def build(self):
        return Button(text="Cerus alebo Nazdár?", font_size="60sp", color=(0, 1, 0, 1))

traktorApp().run()


from kivy.app import App
from kivy.uix.textinput import TextInput

class MojaApp(App):
    def build(self) -> TextInput:
        return TextInput(hint_text="Sem píš…", font_size="24sp", multiline=False)

MojaApp().run()
