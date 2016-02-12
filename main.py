#All the imports done
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import urllib
#Code for the program

#loading kv file
Builder.load_file('loginscreen.kv')

##Main app class
class MedicalApp(App):
    def build(self):
        return sm
    
##class for login
class Login(Screen):
    
    def feed(self):
        def bug_posted(req, results):
            print 'hello'
        dis = self.dis.text
        print dis
        params = urllib.urlencode({'dis': dis})
        print params
        req = UrlRequest('localhost:8000/saved',on_success= bug_posted,on_failure=bug_posted, req_body = params)
        
    
             
    
    
##Assigning screens to screenmanager(sm)
sm = ScreenManager()
sm.add_widget(Login(name='login'))



##Running the main app
if __name__ == '__main__':
    MedicalApp().run()