from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Builder.load_file('Screens/AddExtDriver.kv')

Window.size = (310, 500)

class AddExtDriver(MDScreen):
    pass