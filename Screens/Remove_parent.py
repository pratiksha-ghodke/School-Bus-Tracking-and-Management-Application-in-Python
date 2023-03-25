from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.list import MDList,ThreeLineListItem,OneLineListItem
from kivymd.toast import toast

Builder.load_file('Screens/Remove_parent.kv')

Window.size = (310, 500)
class Remove_parent(MDScreen):
    def remove_parent(self,p_pass1):

        con1 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "DELETE FROM `parent` WHERE p_pass=" + p_pass1
        cur = con1.cursor()
        cur.execute(q1)
        con1.commit()
        con1.close()
        toast(text="Data deleted....!")
        self.ids.p_user1.text = ''
        self.ids.p_pass1.text = ''
