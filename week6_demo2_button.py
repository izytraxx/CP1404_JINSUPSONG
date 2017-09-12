from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

class SecondApp(App):
    message = StringProperty()

    def build(self):
        self.root = Builder.load_file("kivy_size_hint.kv")
        return self.root

    def pressed(self, button):
        if button.text == "x":
            button.text = "o"
        else:
            button.text = "x"
        #print(button.text)


    #When user presses button, textinput is displayed on label

    def button_pressed(self):
        print(self.root.ids.label_display.text)
        message = self.root.ids.user_input.text
        self.root.ids.label_display.text = message
        #self.root.ids.label_display.text = self.root.ids.user_input.text
        #self.root.ids.submit_button.text = "yes"
        print("working")

    def checking(self):
        print(self.root.ids.user_input.text)

SecondApp().run()

"""
Try to create a tic tac toe game with 9 buttons.
"""

#kivy_grid.kv
#GridLayout:
#    cols: 2
#
#    BoxLayout:
#        orientation: "vertical"
#        Button:
#            text: "11"
#        Button:
#            text: "22"
#        Button:
#            text: "33"
#
#    Button:
#        text: "1"
#    Button:
#        text: "2"
#    Button:
#        text: "3"
#    Button:
#        text: "4"
#    Button:
#        text: "5"
