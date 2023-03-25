from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen

Builder.load_file('Screens/DriverWelcome.kv')

Window.size = (310, 500)

class DriverWelcome(MDScreen):
    pass
