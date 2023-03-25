from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.list import MDList,ThreeLineListItem,OneLineListItem
from kivymd.toast import toast

Builder.load_file('Screens/AddBus.kv')

Window.size = (310, 500)

class AddBus(MDScreen):
    def add_bus(self):
        if self.ids.bus_no.text=='' or self.ids.ass_driver.text=='' or self.ids.rute.text=='' or self.ids.d_con.text=='' or self.ids.d_age.text=='':
            toast(text="Please enter required information")
        else:
            bus_no = self.ids.bus_no.text
            ass_driver = self.ids.ass_driver.text
            rute = self.ids.rute.text
            d_con=self.ids.d_con.text
            d_age=self.ids.d_age.text
            con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q = "insert into bus values('" + bus_no + "','" + ass_driver+ "','" + rute + "','" + d_con + "','" + d_age + "')"
            cur = con.cursor()
            cur.execute(q)
            con.commit()
            con.close()
            toast(text="data saved..!")
            self.manager.current = "_AHomeScreen_"
            self.ids.bus_no.text=''
            self.ids.ass_driver.text=''
            self.ids.rute.text=''
            self.ids.d_con.text=''
            self.ids.d_age.text=''



