from hall import Hall


class CinemaHall(Hall):
    threeD = False
    soundSystem = ""

    def add_threed(self):
        self.threeD = True

    def add_sound_system(self, ss):
        self.soundSystem = ss.upper()


