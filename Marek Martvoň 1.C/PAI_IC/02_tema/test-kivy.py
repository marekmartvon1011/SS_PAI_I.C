from kivy.app import App
from kivy.uix.button import Button


class PrveOknoApp(App):
    def build(self):
        return Button(text="Ahoj, Kivy!")


PrveOknoApp().run()


x = int(input("x: ")
y = int(input("y: ")
z = int(input("z: ")
if x >= y:
    max = x
else:
    max = y
if max >= z:
    print("Najväčšie číslo je:", max)
else:
    print("Najväčšie číslo je:", z)