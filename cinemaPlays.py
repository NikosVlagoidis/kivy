from play import Play


class CinemaPlay(Play):
    duration = 0

    def set_duration(self, dur):
        self.duration = dur
