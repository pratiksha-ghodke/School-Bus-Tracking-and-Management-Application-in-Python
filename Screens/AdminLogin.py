from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import mysql.connector as mq

Builder.load_file('Screens/AdminLogin.kv')
Window.size = (310, 500)

class AdminLogin(MDScreen):
    dialog = None

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()

    def login(self):

        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        qr="select * from admin "
        cur = self.con.cursor()
        cur.execute(qr)
        for row in cur:
            if self.ids.user.text == row[0] and self.ids.password.text == row[2]:
                self.manager.current = "_AHomeScreen_"
                self.ids.user.text = ''
                self.ids.password.text = ''

            else:
                self.dialog = MDDialog(
                    title="Log In Failed",
                    text=f"Sorry..! {self.ids.user.text}!",
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            on_release=self.close
                        ),
                    ],
                )
                # open and display dialog
                self.dialog.open()
                self.ids.user.text = ''
                self.ids.password.text = ''






