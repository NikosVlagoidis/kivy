class Play:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.director = ""
        self.actor_list = []

    def add_name(self, name):
        self.name = name

    def add_description(self, des):
        self.description = des

    def add_actor_list(self, actors):
        self.actor_list = actors
