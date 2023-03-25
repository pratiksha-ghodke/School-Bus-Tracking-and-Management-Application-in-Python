from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq

Builder.load_file('Screens/A_remove.kv')

Window.size = (310, 500)

class A_remove(MDScreen):
    def remove(self):
        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        uname = self.ids.user2.text
        print(uname)
        qr = "delete from admin where username = " + uname
        cur = self.con.cursor()
        cur.execute(qr)

        print("deleted...")
