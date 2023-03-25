from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('Screens/Screen1.kv')

Window.size = (310, 500)

class Screen1(MDScreen):
    def on_start(self):
        Clock.schedule_once(self.change_screen, 5)