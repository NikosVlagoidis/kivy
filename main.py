from hall import Hall
from theaterHall import TheaterHall
from cinemaHall import CinemaHall
from week_schedule import Week_Schedule
from play import Play
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from play import movies


class Login(Screen):
    def do_login(self, login_text, password_text):
        app = App.get_running_app()
        app.username = login_text
        app.password = password_text
        if app.username.upper() == "ADMIN" and app.password.upper() == "ADMIN":
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

    def reset_form(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""


class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').reset_form()

    def add_a_play(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'add_a_play_screen'
        self.manager.get_screen('add_a_play_screen').reset_form()

    def delete_a_play(self):
        self.manager.transition = SlideTransition(directtion="left")
        self.manager.current = 'delete_a_play_screen'
        self.manager.get_screen('delete_a_play_screen').show_list()


class AddAPlay(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

    def do_add(self, name_of_play, short_description, director, list_of_actors):
        app = App.get_running_app()
        app.nameOfPlay = name_of_play
        app.shortDescription = short_description
        app.director = director
        app.list_of_actors = list_of_actors
        new_play = Play()
        new_play.set_name(app.nameOfPlay)
        new_play.set_description(app.shortDescription)
        new_play.director = director
        new_play.actor_list = list_of_actors
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        movies.append(new_play)

    def reset_form(self):
        self.ids['nameOfPlay'].text = ""
        self.ids['shortDescription'].text = ""
        self.ids['Director'].text = ""
        self.ids['List_of_Actors'].text = ""
        self.ids['duration'].text = ""

    def do_go_back(self,):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'


class DeleteAPlay(Screen):

    def do_go_back(self,):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

    def show_list(self):
        self.ids.listes.clear_widgets()
        for k in movies:
            label = Label(text=k.name, id=k.name+"label")
            button = Button(text='Delete', id=k.name)
            box = BoxLayout(orientation='horizontal')
            box.add_widget(label)
            box.add_widget(button)
            self.ids.listes.add_widget(box)
            button.fbind('on_press', self.delete_movie)

    def delete_movie(self, obj):

        for k in movies:
            if k.name == obj.id:
                movies.remove(k)
        self.manager.get_screen('delete_a_play_screen').show_list()


class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(AddAPlay(name='add_a_play_screen'))
        manager.add_widget(DeleteAPlay(name='delete_a_play_screen'))
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
