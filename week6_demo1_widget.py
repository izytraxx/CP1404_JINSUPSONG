from kivy.app import App #App is a class for you to link up with kivy widget creation
from kivy.uix.button import Button

class TestApp(App): #TestApp is the new template name created, App is the superclass.
    def build(self): #self means this function (method) belongs to TestApp(class)
        return Button(text="Hello World!") #creating a button with test of Hello World

TestApp().run()