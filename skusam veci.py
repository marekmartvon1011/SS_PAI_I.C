from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import Button
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

class Moja(App):
    def build(self) -> BoxLayout:
        loyout(orientationkoren = BoxL="vertical")
        koren.add_widget(Label(text="KALKULAČKA?", color=(1,1,1,1), font_size="70sp"))
        koren.add_widget(Button(text=" 1 ", color=(0,0,1,1), font_size="50sp", background_color=(1,1,9,10)))
        koren.add_widget(Button(text=" 2 ", color=(1,0,0,1), font_size="50sp", background_color=(9,1,1,10)))
        koren.add_widget(Button(text=" 3 ", color=(1,0,1,1),font_size="50sp", background_color=(6,1,6,10)))
        koren.add_widget(Button(text=" 4 ", color=(0,0,1,1), font_size="50sp", background_color=(1,1,9,10)))
        koren.add_widget(Button(text=" 5 ", color=(1,0,0,1), font_size="50sp", background_color=(9,1,1,10)))
        koren.add_widget(Button(text=" 6 ", color=(1,0,1,1),font_size="50sp", background_color=(6,1,6,10)))
        return koren

Moja().run()