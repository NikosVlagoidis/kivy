from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from play import Play
from play import movies


# add check for empty entries


class AddAPlay(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

    def do_add(self, name_of_play, short_description, director,list_of_actors):
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
        print(new_play.name, new_play.director, new_play.description)

    def reset_form(self):
        self.ids['nameOfPlay'].text = ""
        self.ids['shortDescription'].text = ""

    def do_go_back(self,):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
