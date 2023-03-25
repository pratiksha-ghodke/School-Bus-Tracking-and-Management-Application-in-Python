from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button

Builder.load_file('Screens/ForgotPassword.kv')

Window.size = (310, 500)

class ForgotPassword(MDScreen):
    pass