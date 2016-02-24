from play import Play


class CinemaPlay(Play):
    duration = 0

    def set_duration(self, dur):
        """
        Set the duration of a Cinema Play
        :param dur: Insert the duration
        """
        self.duration = dur
