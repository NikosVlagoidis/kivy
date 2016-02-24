class Play:
    def __init__(self):
        """
        Constructor of a Play Class
        """
        self.name = ""
        self.description = ""
        self.director = ""
        self.actor_list = []

    def set_name(self, name):
        """
        Set a Name to the play
        :param name: Insert the name of the play
        """
        self.name = name

    def set_description(self, des):
        """
        Sets a description to the play
        :param des: Insert a short description of the Play
        """
        self.description = des

    def set_actor_list(self, actors):
        """
        Set the actor list
        :param actors: Insert a short list of actors
        """
        self.actor_list = actors
