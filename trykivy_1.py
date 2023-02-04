from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen

class Screen1(Screen):
   pass

class Screen2(Screen):
   pass

class Screen3(Screen):
   pass

class Screen4(Screen):
   pass

class Screen5(Screen):
   pass

class Screen6(Screen):
   pass

class MyApp(MDApp):
   def build(self):
      self.sm = MDScreenManager()
      self.sm.add_widget(Screen1(name='Screen1'))
      self.sm.add_widget(Screen2(name='Screen2'))
      self.sm.add_widget(Screen3(name='Screen3'))
      self.sm.add_widget(Screen4(name='Screen4'))
      self.sm.add_widget(Screen5(name='Screen5'))
      self.sm.add_widget(Screen6(name='Screen6'))
      return self.sm

MyApp().run()
