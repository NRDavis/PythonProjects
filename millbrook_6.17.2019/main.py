'''
Author:         Nathan Davis
Date:           6.17.2019
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
from kivy.uix.button import Button

from kivy.core.window import Window
import os                                                       # used for saving password information
import webbrowser                                               # used for opening browser


class LoginPage(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)

        padding = 20        # we add 20 pixels of padding to our items

        if os.path.isfile('prev_detail.txt'):
            with open('prev_detail.txt', 'r') as f:
                d = f.read().split(',')
                prev_username = d[0]
                prev_password = d[1]
        else:
            prev_username = ''
            prev_password = ''

        # we add a Label: Username
        username_label = Label(text='Username: ', pos_hint={'x': 0, 'y': .75})  # set text
        username_label.color = [1, 1, 1, 1]        # white label
        username_label.size_hint = (0.3, 0.15)     # label is 30% width and 15% height
        username_label.font_size = 20            # set font size to 20 pixels
        username_label.bold = True              # embolden the text
        self.add_widget(username_label)         # we add the username label to the framework window

        # we add a TextInput field
        self.username = TextInput(multiline=False, pos_hint={'x': 0.30, 'y': 0.775})
        self.username.size_hint = (0.6, 0.075)
        self.add_widget(self.username)

        # we add a password label: Password
        password_label = Label(text='Password: ', pos_hint={'x': 0.0, 'y': 0.65})
        password_label.color = [1, 1, 1, 1]         # white label
        password_label.size_hint = (0.3, 0.15)
        password_label.font_size = 20
        password_label.bold = True
        self.add_widget(password_label)

        # we add a TextInput field for our Password
        self.password = TextInput(multiline=False, pos_hint={'x': 0.30, 'y': 0.675}, password=True)
        self.password.size_hint = (0.6, 0.075)
        self.add_widget(self.password)

        # we add a checkbox for displaying our password

        # we add a Sign-In button
        self.join = Button(text='Sign-In', pos_hint={'x': 0.3, 'y': 0.575})
        self.join.size_hint = (0.6, 0.075)
        self.join.bind(on_press=self.join_button)
        self.add_widget(self.join)


        # we add a label for our signup button
        signup_label = Label(text="Not a Member? ", pos_hint={'x': 0.0, 'y': 0.45})
        signup_label.color = [1, 1, 1, 1]
        signup_label.size_hint = (0.3, 0.15)
        signup_label.font_size = 20
        signup_label.bold = True
        self.add_widget(signup_label)


        # we add a Sign-Up button
        self.up = Button(text='Sign-Up', pos_hint={'x': 0.3, 'y': 0.475})
        self.up.size_hint = (0.6, 0.075)
        self.up.bind(on_press=self.signup_button)
        self.add_widget(self.up)

    def join_button(self, instance):
        username = self.username.text
        password = self.password.text
        print('Recieved:\t{username}, {password}'.format(username=username, password=password))

        with open('prev_detail.txt', 'w') as f:
            f.write("{username},{password}".format(username=username, password=password))

        greeting = "Welcome, {username}".format(username=username)
        millbrook_app.home_page.update_greeting(greeting)
        millbrook_app.screen_manager.current = "Home"

    def signup_button(self, instance):
        print('Sign-Up Button')









class HomePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        # First Row
        # self.add_widget(Label())                                                    # blank label
        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.message = Label(halign='center', valign='middle', font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)  # Message Label

        # Second Row
        self.broadcast = Button(text='Broadcast')  # Broadcast button - needs function
        self.broadcast.bind(on_press=self.broadcast_button)
        self.add_widget(self.broadcast)

        self.podcast = Button(text='Podcast')
        self.podcast.bind(on_press=self.podcast_button)
        self.add_widget(self.podcast)
        # Third Row
        self.media_ctr = Button(text=' Media Ctr')
        self.media_ctr.bind(on_press=self.media_ctr_button)
        self.add_widget(self.media_ctr)

        self.lunch_menu = Button(text='Lunch Menu')
        self.lunch_menu.bind(on_press=self.lunch_menu_button)
        self.add_widget(self.lunch_menu)
        # Fourth Row
        self.king_cast = Button(text='Kingcast')
        self.king_cast.bind(on_press=self.king_cast_button)
        self.add_widget(self.king_cast)

        self.website = Button(text='Website')
        self.website.bind(on_press=self.website_button)
        self.add_widget(self.website)
        # links to:              https://www.wcpss.net/millbrookhs

        url = 'https://www.wcpss.net/millbrookhs'

    def update_greeting(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

    # Button functions
    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'

    def broadcast_button(self, instance):
        print('Broadcast-Button pressed')
        millbrook_app.screen_manager.current = 'Broadcast'

    def podcast_button(self, instance):
        print('Podcast-Button pressed')
        millbrook_app.screen_manager.current = 'Podcast'

    def media_ctr_button(self, instance):
        print('MediaCenter-Button pressed')
        millbrook_app.screen_manager.current = 'Media Center'

    def lunch_menu_button(self, instance):
        print('Lunch-Menu-Button pressed')
        millbrook_app.screen_manager.current = 'Lunch Menu'

    def king_cast_button(self, instance):
        print('Kingcast-Button pressed')
        url = 'https://www.wcpss.net/domain/12389'
        webbrowser.open_new(url)
        millbrook_app.screen_manager.current = 'Kingcast'

    def website_button(self, instance):
        print('website-Button pressed')
        url = 'https://www.wcpss.net/millbrookhs'
        webbrowser.open_new(url)


class Broadcast(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 3

        # First Row
        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text='Broadcast Page'))

        '''
        In future update, we'll add functionality like a link or window to view the video services offered by MHS.
        '''

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'


class Podcast(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text="Podcast"))

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'


class MediaCenter(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text='Media Center'))

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'


class LunchMenu(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text='Lunch Menu'))

        '''

        Functionality will be updated so MHS staff have access to a terminal program and can update the lunch menu
        each meal period.
        There could be a breakfast tab and a lunch tab.

        '''

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'


class KingCast(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text='Kingcast'))

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'


class Website(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.logout = Button(text='Sign Out')
        self.logout.bind(on_press=self.sign_out_button)
        self.add_widget(self.logout)

        self.home = Button(text='Home')
        self.home.bind(on_press=self.home_button)
        self.add_widget(self.home)

        self.add_widget(Label(text='Website'))

        '''
        As of right now, the website button will function simply as a link.
        In the future, it may be updated to function as a menu to a list of links
        '''

    def home_button(self, instance):
        print('return home')
        millbrook_app.screen_manager.current = "Home"

    def sign_out_button(self, instance):
        print('sign-out-button pressed')
        millbrook_app.screen_manager.current = 'Login'





class MillbrookApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.5, 0.95, 1)         # sets page to infantry blue
        self.title = 'Millbrook High School'            # name appearing on top banner

        self.screen_manager = ScreenManager()           # we instantiate screen manager - generate root framework

        # instantiate login page
        self.login_page = LoginPage()
        screen = Screen(name='Login')
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        # instantiate home page
        self.home_page = HomePage()
        screen = Screen(name='Home')
        screen.add_widget(self.home_page)
        self.screen_manager.add_widget(screen)

        # instantiate Broadcast page
        self.broadcast_page = Broadcast()
        screen = Screen(name='Broadcast')
        screen.add_widget(self.broadcast_page)
        self.screen_manager.add_widget(screen)

        # instantiate Podcast page
        self.podcast_page = Podcast()
        screen = Screen(name='Podcast')
        screen.add_widget(self.podcast_page)
        self.screen_manager.add_widget(screen)

        # instantiate Media_ctr page
        self.media_ctr_page = MediaCenter()
        screen = Screen(name='Media Center')
        screen.add_widget(self.media_ctr_page)
        self.screen_manager.add_widget(screen)

        # instantiate Lunch_menu page
        self.lunch_menu_page = LunchMenu()
        screen = Screen(name='Lunch Menu')
        screen.add_widget(self.lunch_menu_page)
        self.screen_manager.add_widget(screen)

        # instantiate Kingcast page
        self.kingcast_page = KingCast()
        screen = Screen(name='Kingcast')
        screen.add_widget(self.kingcast_page)
        self.screen_manager.add_widget(screen)

        # We don't instantiate any page for the website link - that launches a browser application.
        # Maybe, we'll have a common drop down menu.
        return self.screen_manager

if __name__=="__main__":
    millbrook_app = MillbrookApp()
    millbrook_app.run()


# all is good
