from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.list import MDList,ThreeLineListItem,OneLineListItem
from kivymd.toast import toast
Builder.load_file('Screens/RemoveBus.kv')

Window.size = (310, 500)
class RemoveBus(MDScreen):
    def remove_bus(self,b_no):
        if self.ids.b_no.text=='':
            toast(text="Please enter bus number")
        else:
            con1 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q1 = "delete from bus where bus_no = " + b_no
            cur = con1.cursor()
            cur.execute(q1)
            con1.commit()
            con1.close()
            toast("Data deleted....!")
            self.ids.b_no.text=''
            self.ids.a_driver.text=''