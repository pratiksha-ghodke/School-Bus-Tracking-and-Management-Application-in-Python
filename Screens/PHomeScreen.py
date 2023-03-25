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

Builder.load_file('Screens/PHomeScreen.kv')

Window.size = (310, 500)

class PHomeScreen(MDScreen):

    def on_enter(self, *args):
        """Event fired when the screen is displayed: the entering animation is
        complete."""
        print(self.manager.get_screen("_ParentLogin_").ids.p_user.text)

        def on_enter12(interval):
            con2 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            cur = con2.cursor()
            q1 = "SELECT * FROM `student` where p_user = '" + self.manager.get_screen("_ParentLogin_").ids.p_user.text +"'"
            cur.execute(q1)
            ls = cur.fetchall()
            icons = list(md_icons.keys())
            for i in ls:
                self.ids.list_t.add_widget(
                    ListItemWithCheckbox6(text="Roll No : " + i[0], secondary_text="Student Name: " + i[1],
                                         tertiary_text="Date : " + i[5]))
            con2.commit()
            con2.close()

        Clock.schedule_once(on_enter12)
        self.ids.list_t.clear_widgets()

    def p_profile(self):
        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `parent` where p_user = '" + self.manager.get_screen("_ParentLogin_").ids.p_user.text +"'"
        cur = self.con.cursor()
        cur.execute(q1)
        ls = cur.fetchall()

        for val in ls:
            self.ids.box5.add_widget(
                MDLabel(
                    text="Name:  " + str(val[0]),
                    halign="center"
                ))
            self.ids.box6.add_widget(
                MDLabel(
                    text="Password:  " + str(val[1]),
                    halign="center"
                ))

        self.manager.get_screen("_ParentLogin_").ids.p_user.text=''
        self.manager.get_screen("_ParentLogin_").ids.p_pass.text = ''
class ListItemWithCheckbox6(ThreeLineAvatarIconListItem):
    """Custom right container."""
