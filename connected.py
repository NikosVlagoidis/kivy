from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').reset_form()

    def add_a_play(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'add_a_play_screen'
        self.manager.get_screen('add_a_play_screen').reset_form()

