from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq

Builder.load_file('Screens/AdminSignUp.kv')

Window.size = (310, 500)

class AdminSignUp(MDScreen):
    def signup(self):
        username = self.ids.user.text
        email=self.ids.email.text
        password=self.ids.password.text
        con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q = "insert into admin values('" + username + "','" + email + "','" + password + "')"
        cur = con.cursor()
        cur.execute(q)
        con.commit()
        con.close()
        print("data saved..!")
        self.manager.current = "My"

