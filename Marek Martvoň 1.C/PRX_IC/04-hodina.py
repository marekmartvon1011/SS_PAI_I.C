from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import Button
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class Moja(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="partí ananás na pizzu?", color=(1,1,1,1), font_size="70sp"))
        koren.add_widget(Button(text="ano", color=(0,0,1,1), font_size="50sp", background_color=(1,1,9,10)))
        koren.add_widget(Button(text="nie", color=(1,0,0,1), font_size="50sp", background_color=(9,1,1,10)))
        koren.add_widget(Button(text="možno", color=(1,0,1,1),font_size="50sp", background_color=(6,1,6,10)))
        return koren

Moja().run()

