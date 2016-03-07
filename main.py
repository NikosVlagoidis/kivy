from hall import Hall
from theaterHall import TheaterHall
from cinemaHall import CinemaHall
from week_schedule import Week_Schedule
from play import Play
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from connected import Connected
from add_a_play_screen import AddAPlay
from play import movies


class Login(Screen):
    def do_login(self, login_text, password_text):
        app = App.get_running_app()
        app.username = login_text
        app.password = password_text
        if app.username.upper() =="ADMIN" and app.password.upper() =="ADMIN":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

    def reset_form(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(AddAPlay(name='add_a_play_screen'))

        return manager


if __name__ == '__main__':

    LoginApp().run()


hall = Hall("Hall 1", 300)
hall2 = Hall("Hall 2", 500)

jamesbond = Play()
jamesbond.set_name("James Bond")
schedule = Week_Schedule()
lotr = Play()
lotr.set_name("Lord of the Rings")

schedule.set_play_date(jamesbond, "Monday", hall, ["12,30", "14,40", "16.30"])
schedule.set_play_date(jamesbond, "Monday", hall2, "17.00")
schedule.set_play_date(jamesbond, "Tuesday", hall2, "17.00")
schedule.set_play_date(lotr, "Sunday", hall2, "13.00")


schedule.find_day_for_play(lotr.name)
schedule.find_day_for_play(jamesbond.name)



for movie in movies:
    print(movie.name)
    print(movie.description)
    print(movie.actor_list)
