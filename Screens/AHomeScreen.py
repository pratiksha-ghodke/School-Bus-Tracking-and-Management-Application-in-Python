from kivy import args
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix import widget
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList,OneLineListItem,ThreeLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.clock import Clock
import mysql.connector as mq
from kivymd.icon_definitions import md_icons
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.toast import toast
import datetime

Builder.load_file('Screens/AHomeScreen.kv')

Window.size = (310, 500)
class AHomeScreen(MDScreen):

    def on_enter(self, *args):
        """Event fired when the screen is displayed: the entering animation is
        complete."""

        def on_enter1(interval):
            con2 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            cur = con2.cursor()
            q1 = "SELECT * FROM `s_driver`"
            cur.execute(q1)
            ls = cur.fetchall()
            icons = list(md_icons.keys())
            for i in ls:
                self.ids.list_one.add_widget(
                    ListItemWithCheckbox1(text="Driver ID: " + i[4], secondary_text="Bus No: " + i[1],
                                          tertiary_text="Driver Name : " + i[0], icon=icons[1]))
            con2.commit()
            con2.close()

        def on_enter2(interval):
            con2 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            cur = con2.cursor()
            q1 = "SELECT * FROM `student` "
            cur.execute(q1)
            ls = cur.fetchall()
            icons = list(md_icons.keys())
            for i in ls:
                self.ids.list_two.add_widget(
                    ListItemWithCheckbox2(text="Roll No : " + i[0], secondary_text="Student Name: " + i[1],
                                         tertiary_text="Class: " + i[6], icon=icons[1]))
            con2.commit()
            con2.close()

        def on_enter(interval):
            con2 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            cur = con2.cursor()
            q1 = "SELECT * FROM `bus`"
            cur.execute(q1)
            ls = cur.fetchall()
            icons = list(md_icons.keys())
            for i in ls:
                self.ids.list_three.add_widget(
                    ListItemWithCheckbox3(text="bus_no : " + i[0], secondary_text="driver : " + i[1],
                                          tertiary_text="Rute :" + i[2], icon=icons[1]))

            con2.commit()
            con2.close()

        Clock.schedule_once(on_enter1)
        self.ids.list_one.clear_widgets()
        Clock.schedule_once(on_enter2)
        self.ids.list_two.clear_widgets()
        Clock.schedule_once(on_enter)
        self.ids.list_three.clear_widgets()

    def create_list(self, *args):
        con3 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `s_driver`"
        cur = con3.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons = list(md_icons.keys())
        for i in ls:
            self.ids.list_one.add_widget(
                ListItemWithCheckbox1(text="Driver ID: " + i[4], secondary_text="Bus No: " + i[1],
                                      tertiary_text="Driver Name : " + i[0], icon=icons[1]))
        con3.commit()
        con3.close()
    # This function works when called from a button
    def button_push(self,):
        con4 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `s_driver`"
        cur = con4.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons= list(md_icons.keys())
        for i in ls:
            self.ids.list_one.add_widget(ListItemWithCheckbox1(text="Driver ID: "+i[4],secondary_text="Bus No: "+i[1],tertiary_text="Driver Name : "+i[0],icon=icons[1]))
        con4.commit()
        con4.close()
    def create_list2(self, *args):
        con3 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `student`"
        cur = con3.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons = list(md_icons.keys())
        for i in ls:
            self.ids.list_two.add_widget(ListItemWithCheckbox2(text="Roll No : "+i[0],secondary_text="Student Name: "+i[1],tertiary_text="Class: "+i[6],icon=icons[1]))
        con3.commit()
        con3.close()

        # This function works when called from a button
    def button_push2(self, ):
        con4 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `student` "
        cur = con4.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons = list(md_icons.keys())
        for i in ls:
            self.ids.list_two.add_widget(ListItemWithCheckbox2(text="Roll No : "+i[0],secondary_text="Student Name: "+i[1],tertiary_text="Class: "+i[6],icon=icons[1]))
        con4.commit()
        con4.close()
    def create_list1(self, *args):
        con3 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `bus`"
        cur = con3.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons1 = list(md_icons.keys())
        for i in ls:
            self.ids.list_three.add_widget(
                ListItemWithCheckbox3(text="bus_no : " + i[0], secondary_text="driver : " + i[1],
                                      tertiary_text="Rute :" + i[2], icon=icons1[1]))

        con3.commit()
        con3.close()

        # This function works when called from a button

    def button_push1(self, ):
        con4 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `bus`"
        cur = con4.cursor()
        cur.execute(q1)
        ls = cur.fetchone()
        icons1 = list(md_icons.keys())
        for i in ls:
            self.ids.list_three.add_widget(
                ListItemWithCheckbox3(text="bus_no : " + i[0], secondary_text="driver : " + i[1],tertiary_text="Rute :"+i[2],icon=icons1[1]))

        con4.commit()
        con4.close()


    def change_color(self, instance):
        if instance in self.ids.values():
            current_id = list(self.ids.keys())[list(self.ids.values()).index(instance)]
            for i in range(5):
                if f"nav_icon{i + 1}" == current_id:
                    self.ids[f"nav_icon{i + 1}"].text_color = 1, 0, 0, 1
                else:
                    self.ids[f"nav_icon{i + 1}"].text_color = 0, 0, 0, 1



class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class AddStudent(MDScreen):
    def add_student(self, stud_name, enroll_no, p_user, s_add, user_d, class1):
        date = str(datetime.date.today())
        if self.ids.stud_name.text == '' or self.ids.enroll_no.text == '' or self.ids.p_user.text == '' or self.ids.s_add.text == '' or self.ids.user_d.text == '' or self.ids.class1.text=='':
            toast(text="Please enter required information")

        else:
            con5 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q = "insert into student values('" + enroll_no + "','" + stud_name + "','" + s_add + "','" + user_d +"','"+ p_user + "','" + date + "','" + class1 + "')"
            cur = con5.cursor()
            cur.execute(q)
            con5.commit()
            con5.close()
            con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q1 = "SELECT * FROM `student`"
            cur = con.cursor()
            cur.execute(q1)
            ls = cur.fetchall()
            for i in ls:
                print(i)
            toast(text="data saved..!")
            self.manager.current = "_AHomeScreen_"
            self.ids.stud_name.text=''
            self.ids.enroll_no.text = ''
            self.ids.p_user.text = ''
            self.ids.s_add.text= ''
            self.ids.user_d.text=''
            con.commit()
            con.close()


class Remove_student(MDScreen):
    enroll_no1 = StringProperty()
    def remove_s(self,enroll_no1):
        if self.ids.enroll_no1.text=='':
            toast(text="Please enter roll no.")
        else:
            con1 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            #print("Enter enrollment No : ")
            #enroll_no1 = input()
            q1 = "DELETE FROM `student` WHERE enroll_no = " + enroll_no1
            cur = con1.cursor()
            cur.execute(q1)
            con1.commit()
            con1.close()
            self.ids.enroll_no1.text=''
            self.ids.stud_name.text = ''
            self.ids.enroll_no1.text = ''
            self.ids.bus_no.text = ''
            self.ids.class1.text= ''
            toast(text="Data deleted....!")

class AddDriver(MDScreen):
    def add_driver(self, d_name, user_d, bus_no, pass_d,driver_id):
        ls = []
        if self.ids.d_name.text=='' or self.ids.user_d.text=='' or self.ids.bus_no.text=='' or self.ids.pass_d.text=='' or self.ids.driver_id.text=='':
            toast(text="Please enter required information")
        else:
            con5 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q = "insert into s_driver values('" + d_name + "','" + bus_no + "','" + user_d + "','"+ pass_d + "','" + driver_id + "')"
            cur = con5.cursor()
            cur.execute(q)
            con5.commit()
            con5.close()
            con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            q1 = "SELECT * FROM `s_driver`"
            cur = con.cursor()
            cur.execute(q1)
            ls = cur.fetchall()
            self.manager.current = "_AHomeScreen_"
            toast(text="Data saved....!")
            self.ids.d_name.text=''
            self.ids.user_d.text=''
            self.ids.bus_no.text=''
            self.ids.pass_d.text=''
            self.ids.driver_id.text=''
            con.commit()
            con.close()

class ListItemWithCheckbox1(ThreeLineAvatarIconListItem):
    icon = StringProperty("android")

class ListItemWithCheckbox2(ThreeLineAvatarIconListItem):
    icon = StringProperty("android")

class ListItemWithCheckbox3(ThreeLineAvatarIconListItem):
    icon = StringProperty("android")

class Remove(MDScreen):
    driver_id_1 = StringProperty()
    def remove(self,driver_id_1):
        if self.ids.driver_id_1.text =='':
            toast(text="Please enter driver id")
        else:
            con1 = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
            #print("Enter driver id: ")
            #driver_id = input()
            q1 = "delete from s_driver where driver_id = " + driver_id_1
            cur = con1.cursor()
            cur.execute(q1)
            con1.commit()
            con1.close()
            self.ids.driver_id_1.text = ''
            self.ids.driver_name.text = ''
            self.ids.driver_pass.text = ''
            self.ids.bus_no.text = ''
            toast(text="Data deleted....!")
