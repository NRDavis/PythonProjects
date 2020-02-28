'''
Author:     Nathan Davis
Date:       2.14.2020 - Happy Valentine's Day
Intent:     To create a GUI for serial Communication with Python for use on a Raspberry Pi


'''

# Items imported for GUI
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

# Items imported for Serial Communication
    # will utilize pySerial to perform communication tasks
#import serial



'''
serial comm for raspberry pi


'''





class mainPage(FloatLayout):
    def __init__(self, **kwargs):
        super(mainPage, self).__init__(**kwargs)

        padding = 20    # we add 20 pixels of padding to our items

        # adding labels for serial Communications
        self.input_label = Label(text='Serial Input', pos_hint = {'x':0.0, 'y':0.85})
        self.input_label.size_hint = (0.225, 0.05)
        self.input_label.color = (1,1,1,1)
        self.add_widget(self.input_label)

        self.text_bar = TextInput(text='Enter', multiline = False, pos_hint = {'x':0.2, 'y':0.85})
        self.text_bar.size_hint = (0.225, 0.05)
        self.text_bar.color = (1,1,1,1)
        def on_enter(instance, value):
            print('User pressed enter', instance)
        self.text_bar.bind(on_text_validate= on_enter)
        self.add_widget(self.text_bar)



        self.output_label = Label(text='Serial Output', pos_hint={'x': 0.0, 'y': 0.75})
        self.output_label.size_hint = (0.225, 0.05)
        self.output_label.color = (1, 1, 1, 1)
        self.add_widget(self.output_label)

        self.text_bar = TextInput(text='Receive', pos_hint={'x': 0.2, 'y': 0.75})
        self.text_bar.size_hint = (0.225, 0.05)
        self.text_bar.color = (1, 1, 1, 1)
        self.add_widget(self.text_bar)



        self.send_button = Button(text='Send', pos_hint={'x': 0.1, 'y':0.65})
        self.send_button.size_hint = (0.225, 0.05)
        self.send_button.bind(on_press=self.send)
        self.add_widget(self.send_button)

    def send(self, instance):
        if self.send_button.text == 'Click 1':
            self.send_button.text = 'Click 2'
        else:
            self.send_button.text = 'Click 1'

    '''
    def on_enter(self, instance):
        print('User pressed enter', instance)
    '''



class PldProtoApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)   # sets page to Black
        self.title = 'PLD Proto'
        self.screen_manager = ScreenManager()

        # instantiate Mainpage
        self.main_page = mainPage()
        screen = Screen(name='')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)
        return self.screen_manager


if __name__ =="__main__":
    pld_proto_app = PldProtoApp()
    pld_proto_app.run()
