from hall import Hall


class CinemaHall(Hall):
    threeD = False
    soundSystem = ""

    def set_threed(self):
        """
        Set a Cinema Hall to have 3d Screen
        """
        self.threeD = True

    def set_sound_system(self, ss):
        """
        Set a Specific SoundSystem to the Cinema Hall
        :param ss:
        """
        self.soundSystem = ss.upper()


