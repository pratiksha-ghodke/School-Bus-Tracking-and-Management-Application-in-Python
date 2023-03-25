from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.list import MDList,ThreeLineListItem,OneLineListItem
from kivymd.toast import toast

Builder.load_file('Screens/Add_parent.kv')

Window.size = (310, 500)

class Add_parent(MDScreen):
    def add_p(self):
        p_user = self.ids.p_user.text
        p_pass = self.ids.p_pass.text

        con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q = "insert into parent values('" + p_user + "','" + p_pass + "')"
        cur = con.cursor()
        cur.execute(q)
        con.commit()
        con.close()
        toast(text="data saved..!")
        self.manager.current = "_AHomeScreen_"
        self.ids.p_user.text=''
        self.ids.p_pass.text=''