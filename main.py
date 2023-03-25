from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from Screens.Screen1 import Screen1
from Screens.FirstScreen import FirstScreen
from Screens.My import My
from Screens.AdminWelcome import AdminWelcome
from Screens.ParentWelcome import ParentWelcome
from Screens.DriverWelcome import DriverWelcome
from Screens.AdminSignUp import AdminSignUp
from Screens.AdminLogin import AdminLogin
from Screens.DriverLogin import DriverLogin
from Screens.ParentLogin import ParentLogin
from Screens.PHomeScreen import PHomeScreen
from Screens.DHomeScreen import DHomeScreen
from Screens.AHomeScreen import AHomeScreen
from Screens.AddBus import AddBus
from Screens.DriversMapView2 import DriversMapView2
from Screens.Add_parent import Add_parent
from Screens.AddExtDriver import AddExtDriver
from Screens.Logout import Logout
from Screens.DLogout import DLogout
from Screens.DriversMapView import DriversMapView
from Screens.try1 import try1
from Screens.RemoveBus import RemoveBus
from Screens.Remove_parent import Remove_parent
from Screens.A_remove import A_remove
from Screens.Profile import Profile
from Screens.ForgotPassword import ForgotPassword
from Screens.ResetPassword import ResetPassword
from kivymd.uix.list import MDList,ThreeLineListItem,OneLineListItem
import mysql.connector as mq

class RootScreenManager(ScreenManager):
    pass

class Travel_Management_2(MDApp):
    def build(self):
        return RootScreenManager()


if __name__ == "__main__":
    Travel_Management_2().run()
