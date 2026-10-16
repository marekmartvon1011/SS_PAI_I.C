

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MojaApp(App):
    def build(self):
        return Label(text="Ahoj"), Button(text="Klik")   # POZOR: takto to NEPÔJDE

MojaApp().run()

from kivy.app import App
from kivy.uix.image import Image

class MojaApp(App):
    def build(self) -> Image:
        return Image(source="obrazok.png")

MojaApp().run()