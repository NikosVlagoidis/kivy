from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from play import Play
from play import movies

#add check for empty entries

class AddAPlay(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'

    def do_add(self, nameOfPlay, shortDescription):
        app = App.get_running_app()
        app.nameOfPlay = nameOfPlay
        app.shortDescription = shortDescription
        new_play = Play()
        new_play.set_name(app.nameOfPlay)
        new_play.set_description(app.shortDescription)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'
        movies.append(new_play)
        print(new_play.name)

    def reset_form(self):
        self.ids['nameOfPlay'].text = ""
        self.ids['shortDescription'].text = ""
