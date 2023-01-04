import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time
from pytz import timezone
from datetime import datetime, timedelta

format = "%Y-%m-%d %H:%M:%S"

class myclock1(Label):
    def update(self, *args):
    
        now_africa = datetime.now(timezone('US/Pacific'))
        self.text = "Pacific time: " + now_africa.strftime(format)
        
class myclock2(Label):
    def update(self, *args):

        now_utc = datetime.now(timezone('UTC'))
        self.text = "UTF time: " + now_utc.strftime(format)
        
class myclock3(Label):
    def update(self, *args):

        now_asia = datetime.now(timezone('Asia/Kolkata'))
        self.text = "Kolkata time: " + now_asia.strftime(format)

class Grid_LayoutApp(App):
    def build(self):

        clock1 = myclock1()
        clock2 = myclock2()
        clock3 = myclock3()
        
        Clock.schedule_interval(clock1.update, 1)
        Clock.schedule_interval(clock2.update, 1)
        Clock.schedule_interval(clock3.update, 1)
        
        layout = GridLayout(cols = 1)

        layout.add_widget(clock1)
        layout.add_widget(clock2)
        layout.add_widget(clock3) 
 
        return layout
    
    

root = Grid_LayoutApp()
root.run()
