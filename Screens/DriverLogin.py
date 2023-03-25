from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
Builder.load_file('Screens/DriverLogin.kv')

Window.size = (310, 500)

class DriverLogin(MDScreen):

    dialog = None

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()
    def dlogin(self):

        if self.ids.d_user.text=='' and self.ids.d_pass.text=='':
            print("not ok")
            self.dialog = MDDialog(
                title="Log In Failed",
                text=f"Please Enter username & password...!",
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        on_release=self.close
                    ),
                ],
            )
            # open and display dialog
            self.dialog.open()
            self.ids.d_user.text = ''
            self.ids.d_pass.text = ''


        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `s_driver`"
        cur = self.con.cursor()
        cur.execute(q1)
        ls = cur.fetchall()

        for val in ls:
            if val[2] == self.ids.d_user.text and val[3]==self.ids.d_pass.text:
                self.manager.current = "_DHomeScreen_"


















