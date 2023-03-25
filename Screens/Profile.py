from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import mysql.connector as mq

Builder.load_file('Screens/Profile.kv')
Window.size = (310, 500)

class Profile(MDScreen):
    pass