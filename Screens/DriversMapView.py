from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

Window.size = (310, 500)

Builder.load_file('Screens/DriversMapView.kv')

class DriversMapView(MDScreen, MapView):
    getting_markets_timer = None

    def start_getting_markets_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.getting_markets_timer.cancel()
        except:
            pass

        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov, 1)

    def get_markets_in_fov(self, *args):
        # Get reference to main app and the database cursor
        pass

    def add_market(self, market):
        pass

