from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button

Builder.load_file('Screens/ResetPassword.kv')

Window.size = (310, 500)

class ResetPassword(MDScreen):
    pass