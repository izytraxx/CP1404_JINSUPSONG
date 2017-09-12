"""
Construct an user interface with left and right panel. 
The left panel occupies 300 pixels wide, with the remaining space goes to the right panel.
The left panel displays a single line textInput and a submit button.
The right panel displays buttons using the names of animals according to the data below:
lion : 90
tiger : 80
deer : 70
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.config import Config

class AnimalApp(App):
    Config.set("graphics", "width", '500')
    Config.set("graphics", "height", '400')

    def __init__(self, **kwargs): # Initialise the starting values for a class
        super().__init__(**kwargs) # Connect current file to superclass App init()
        self.animals = {
            "lion": 90,
            "tiger": 80,
            "deer": 70
        }

    def build(self):
        self.root = Builder.load_file('animal_gui.kv')
        #print(self.animals) # Test statement
        self.create_buttons()
        return self.root

    def create_buttons(self):
        # Extract the keys in animals, then display on right panel as buttons
        for key, value in self.animals.items():
            temp_button = Button(text=key)
            temp_button.bind(on_release=self.pressed)
            self.root.ids.main_content.add_widget(temp_button)
            print(key)

    def pressed(self, button):
        print(button.text)

AnimalApp().run()
