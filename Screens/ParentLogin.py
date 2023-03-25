from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import mysql.connector as mq
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
Builder.load_file('Screens/ParentLogin.kv')

Window.size = (310, 500)

class ParentLogin(MDScreen):
    dialog = None

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()
    def plogin(self):
        if self.ids.p_user.text == '' and self.ids.p_pass.text == '':
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
            self.ids.p_user.text = ''
            self.ids.p_pass.text = ''

        self.con = mq.connect(host='localhost', user='root', password='', database='travel_management_&_tracking')
        q1 = "SELECT * FROM `parent`"
        cur = self.con.cursor()
        cur.execute(q1)
        ls = cur.fetchall()

        for val in ls:
            # print(i[p])
            if val[0] == self.ids.p_user.text and val[1] == self.ids.p_pass.text:
                # for val in ls2:
                # print(m[p])
                # if val[0]==d_pass:
                self.manager.current = "_PHomeScreen_"





