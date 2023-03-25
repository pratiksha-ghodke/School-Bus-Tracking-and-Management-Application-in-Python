from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.clock import Clock
import mysql.connector as mq
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDList,OneLineListItem,ThreeLineAvatarIconListItem
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IconLeftWidget
from kivy_garden.mapview import MapView
from kivymd.uix.label import MDLabel
import datetime
Builder.load_file('Screens/DHomeScreen.kv')

Window.size = (310, 500)

class DHomeScreen(MDScreen):

    def on_enter(self, *args):
        """Event fired when the screen is displayed: the entering animation is
        complete."""

        def on_enter1(interval):
            con2 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            cur = con2.cursor()
            q1 = "SELECT * FROM `student` where user_d = '" + self.manager.get_screen("_DriverLogin_").ids.d_user.text +"'"
            cur.execute(q1)
            ls = cur.fetchall()
            icons = list(md_icons.keys())
            for i in ls:
                self.ids.list_two1.add_widget(
                    ListItemWithCheckbox4(text="Roll No : " + i[0], secondary_text="Student Name: " + i[1],
                                         tertiary_text="Class: " + i[6]))
            con2.commit()
            con2.close()

        Clock.schedule_once(on_enter1)
        self.ids.list_two1.clear_widgets()



    def profile(self):

        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `s_driver` where user_d = '" + self.manager.get_screen("_DriverLogin_").ids.d_user.text+"'"
        cur = self.con.cursor()
        cur.execute(q1)
        ls = cur.fetchall()

        for val in ls:
            self.ids.box.add_widget(
                MDLabel(
                    text="Name:  "+str(val[0]),
                    halign="center"
                ))
            self.ids.box2.add_widget(
                MDLabel(
                    text="ID:  " + str(val[4]),
                    halign="center"
                ))

        self.manager.get_screen("_DriverLogin_").ids.d_user.text=''
        self.manager.get_screen("_DriverLogin_").ids.d_pass.text=''


class ListItemWithCheckbox4(ThreeLineAvatarIconListItem):
    """Custom right container."""
    def on_checkbox_active(self):
        print("okk")
        idate = str(datetime.date.today())
        con5 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q = "insert into attendance values('" + idate + "')"
        cur = con5.cursor()
        cur.execute(q)
        con5.commit()
        con5.close()

class RightCheckbox(IRightBodyTouch,MDCheckbox):
    """Custom right container."""




