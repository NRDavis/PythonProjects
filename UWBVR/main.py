'''
Author:         Nathan Davis
Date:           10.9.2019
Intent:
                This is an experimental venture into the use of Kivy and other Python3 frameworks towards the
                development of a cross-platform application capable of running on Windows/MacOS/Linux/Android
'''

from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout                      # temporary used to transition over
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen        # used for screen management

from kivy.uix.slider import Slider
from kivy.uix.button import Button

from kivy.uix.camera import Camera
from kivy.core.window import Window


class ControlPage(FloatLayout):
    def __init__(self, **kwargs):
        super(ControlPage, self).__init__(**kwargs)

        padding = 20        # we add 20 pixels of padding to our items

    # Sliders for each of the servos - each one entitled servo_x
        self.servo_1 = Slider(min = -135, max=135, value = 0, pos_hint={'x': 0.75, 'y': 0.30})
        self.servo_1.size_hint = (0.225, 0.05)
        self.servo_1.bind(on_press=self.slide_one)
        self.add_widget(self.servo_1)

        self.servo_2 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.25})
        self.servo_2.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_2)

        self.servo_3 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.20})
        self.servo_3.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_3)

        self.servo_4 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.15})
        self.servo_4.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_4)

        self.servo_5 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.10})
        self.servo_5.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_5)

        self.servo_6 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.05})
        self.servo_6.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_6)

        self.servo_7 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.35})
        self.servo_7.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_7)

        self.servo_8 = Slider(min=-135, max=135, value=0, pos_hint={'x': 0.75, 'y': 0.40})
        self.servo_8.size_hint = (0.225, 0.05)
        self.add_widget(self.servo_8)

    # Labels for each one of the servo sliders - each one entitled slabel_x
        self.slabel_1 = Label(text='s1: Base', pos_hint={'x': 0.60, 'y': 0.40})
        self.slabel_1.size_hint = (0.225, 0.05)
        self.slabel_1.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_1)

        self.slabel_1 = Label(text='s2: Art 1', pos_hint={'x': 0.60, 'y': 0.35})
        self.slabel_1.size_hint = (0.225, 0.05)
        self.slabel_1.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_1)

        self.slabel_1 = Label(text='s3: Art 1', pos_hint={'x': 0.60, 'y': 0.30})
        self.slabel_1.size_hint = (0.225, 0.05)
        self.slabel_1.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_1)

        self.slabel_2 = Label(text='s4: Art 2', pos_hint={'x': 0.60, 'y': 0.25})
        self.slabel_2.size_hint = (0.225, 0.05)
        self.slabel_2.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_2)

        self.slabel_3 = Label(text='s5: Art 2', pos_hint={'x': 0.60, 'y': 0.20})
        self.slabel_3.size_hint = (0.225, 0.05)
        self.slabel_3.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_3)

        self.slabel_4 = Label(text='s6: Art 2', pos_hint={'x': 0.60, 'y': 0.15})
        self.slabel_4.size_hint = (0.225, 0.05)
        self.slabel_4.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_4)

        self.slabel_5 = Label(text='s7: Art 3', pos_hint={'x': 0.60, 'y': 0.10})
        self.slabel_5.size_hint = (0.225, 0.05)
        self.slabel_5.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_5)

        self.slabel_6 = Label(text='s8: Art 3', pos_hint={'x': 0.60, 'y': 0.05})
        self.slabel_6.size_hint = (0.225, 0.05)
        self.slabel_6.color = (1, 1, 1, 1)
        self.add_widget(self.slabel_6)

        self.sgauge_zero = Label(text='-135', pos_hint={'x': 0.65, 'y': 0.45})
        self.sgauge_zero.size_hint = (0.225, 0.05)
        self.sgauge_zero.color = (1, 1, 1, 1)
        self.add_widget(self.sgauge_zero)

        self.sgauge_onehundred = Label(text='135', pos_hint={'x': 0.84, 'y': 0.45})
        self.sgauge_onehundred.size_hint = (0.225, 0.05)
        self.sgauge_onehundred.color = (1, 1, 1, 1)
        self.add_widget(self.sgauge_onehundred)

        self.slabel_servo = Label(text='Servos', pos_hint={'x': 0.75, 'y': 0.50})
        self.slabel_servo.size_hint = (0.225, 0.05)
        self.slabel_servo.color = (1, 0, 0, 1)
        self.add_widget(self.slabel_servo)

    # Adding a Camera Pane to the frame
        self.cam = Camera()
        self.cam = Camera(resolution=(1024, 1024), size=(.1, .1))
        self.cam.size_hint = (0.5, 0.5)
        self.cam.pos_hint = {'x': 0.25, 'y': 0.5}
        self.cam.play = True
        self.add_widget(self.cam)

    # Adding a button to cut Camera Feed
        self.cam_button = Button(text='Cut', pos_hint={'x': 0.4, 'y': 0.425})
        self.cam_button.size_hint = (0.2, 0.075)
        self.cam_button.bind(on_press=self.change_feed)
        self.add_widget(self.cam_button)

    # Adding labels for the Ultrasonic Proximity Sensors

        self.sensor_forward = Label(text='Ultrasonic Sensors', pos_hint={'x': 0.075, 'y': 0.30})
        self.sensor_forward.size_hint = (0.075, 0.05)
        self.sensor_forward.color = (1, 0, 0, 1)
        self.add_widget(self.sensor_forward)

        self.sensor_forward = Label(text='Forward Sensor:', pos_hint={'x': 0.05, 'y': 0.25})
        self.sensor_forward.size_hint = (0.075, 0.05)
        self.sensor_forward.color = (1, 1, 1, 1)
        self.add_widget(self.sensor_forward)

        self.sensor_left = Label(text='  Left Sensor:', pos_hint={'x': 0.05, 'y': 0.2})
        self.sensor_left.size_hint = (0.075, 0.05)
        self.sensor_left.color = (1, 1, 1, 1)
        self.add_widget(self.sensor_left)

        self.sensor_right = Label(text='Right Sensor:', pos_hint={'x': 0.05, 'y': 0.15})
        self.sensor_right.size_hint = (0.075, 0.05)
        self.sensor_right.color = (1, 1, 1, 1)
        self.add_widget(self.sensor_right)

        self.sensor_top = Label(text='   Top Sensor:', pos_hint={'x': 0.05, 'y': 0.10})
        self.sensor_top.size_hint = (0.075, 0.05)
        self.sensor_top.color = (1, 1, 1, 1)
        self.add_widget(self.sensor_top)

        self.sensor_bottom = Label(text='Bottom Sensor:', pos_hint={'x': 0.05, 'y': 0.05})
        self.sensor_bottom.size_hint = (0.075, 0.05)
        self.sensor_bottom.color = (1, 1, 1, 1)
        self.add_widget(self.sensor_bottom)

    # Data for Ultrasonic Proximity Sensors
        self.data_forward = Label(text='--', pos_hint={'x':0.15, 'y': 0.25})
        self.data_forward.size_hint = (0.075, 0.05)
        self.data_forward.color = (1, 1, 1, 1)
        self.add_widget(self.data_forward)

        self.data_left = Label(text = '--', pos_hint={'x': 0.15, 'y': 0.2})
        self.data_left.size_hint = (0.075, 0.05)
        self.data_left.color = (1, 1, 1, 1)
        self.add_widget(self.data_left)

        self.data_right = Label(text='--', pos_hint={'x': 0.15, 'y': 0.15})
        self.data_right.size_hint = (0.075, 0.05)
        self.data_right.color = (1, 1, 1, 1)
        self.add_widget(self.data_right)

        self.data_top = Label(text='--', pos_hint={'x': 0.15, 'y': 0.10})
        self.data_top.size_hint = (0.075, 0.05)
        self.data_top.color = (1, 1, 1, 1)
        self.add_widget(self.data_top)

        self.data_bottom = Label(text='--', pos_hint={'x': 0.15, 'y': 0.05})
        self.data_bottom.size_hint = (0.075, 0.05)
        self.data_bottom.color = (1, 1, 1, 1)
        self.add_widget(self.data_bottom)

    def change_feed(self, instance):
        if self.cam_button.text == 'Cut':
            self.cam_button.text = 'Go Live'
            self.cam.play = False
        else:
            self.cam_button.text = 'Cut'
            self.cam.play = True

    def slide_one(self, instance):
        if self.servo_1.value > 80:
            self.slabel_1.color = (0, .5, .5, 1)
        else:
            self.slabel_1.color = (1, 1, 1, 1)




class UWBVRApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)         # sets page to Black
        self.title = 'UWBVR'            # name appearing on top banner
        self.screen_manager = ScreenManager()           # we instantiate screen manager - generate root framework

        # instantiate login page
        self.control_page = ControlPage()
        screen = Screen(name='')
        screen.add_widget(self.control_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__=="__main__":
    uwbvr_app = UWBVRApp()
    uwbvr_app.run()


# all is good
