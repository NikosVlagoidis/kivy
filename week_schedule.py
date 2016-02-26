from play import Play
from cinemaPlays import CinemaPlay
from hall import Hall
from theaterHall import TheaterHall
from cinemaHall import CinemaHall


class Week_Schedule:

    def __init__(self):
        self.Monday = {}
        self.Tuesday = {}
        self.Wednesday = {}
        self.Thursday = {}
        self.Friday = {}
        self.Saturday = {}
        self.Sunday = {}

    def set_play_date(self, play, day, hall, time):

        if day.upper() == "MONDAY":
            self.Monday[hall.name] = [play.name, time]
        if day.upper() == "TUESDAY":
            self.Tuesday[hall.name] = [play.name, time]
        if day.upper() == "WEDNESDAY":
            self.Wednesday[hall.name] = [play.name, time]
        if day.upper() == "THURSDAY":
            self.Thursday[hall.name] = [play.name, time]
        if day.upper() == "FRIDAY":
            self.Friday[hall.name] = [play.name, time]
        if day.upper() == "SATURDAY":
            self.Saturday[hall.name] = [play.name, time]
        if day.upper() == "SUNDAY":
            self.Sunday[hall.name] = [play.name, time]

    def find_day_for_play(self, play):
        print("Day \t Play \t Time \t  \tHall \t for " + play)
        out = ""
        try:
            for halls in self.Monday.values():
                for i in halls:
                    if i == play:
                        out += ("Monday " + str(halls))
                        for key in self.Monday.keys():
                            if self.Monday[key] == halls:
                                out += " " + key + "\n"



        except:
            pass
        try:
            for halls in self.Tuesday.values():
                for i in halls:
                    if i == play:
                        out += ("Tuesday " + str(halls))
                        for key in self.Tuesday.keys():
                            if self.Tuesday[key] == halls:
                                out += " " + key + "\n"

        except:
            pass
        try:
            for halls in self.Wednesday.values():
                for i in halls:
                    if i == play:
                        out += ("Wednesday " + str(halls))
                        for key in self.Wednesday.keys():
                            if self.Wednesday[key] == halls:
                                out += " " + key + "\n"
        except:
            pass
        try:
            for halls in self.Thursday.values():
                for i in halls:
                    if i == play:
                        out += ("Thursday " + str(halls))
                        for key in self.Thursday.keys():
                            if self.Thursday[key] == halls:
                                out += " " + key + "\n"
        except:
            pass
        try:
            for halls in self.Friday.values():
                for i in halls:
                    if i == play:
                        out += ("Friday " + str(halls))
                        for key in self.Friday.keys():
                            if self.Friday[key] == halls:
                                out += " " + key + "\n"
        except:
            pass
        try:
            for halls in self.Saturday.values():
                for i in halls:
                    if i == play:
                        out += ("Saturday " + str(halls))
                        for key in self.Saturday.keys():
                            if self.Saturday[key] == halls:
                                out += " " + key + "\n"
        except:
            pass
        try:
            for halls in self.Sunday.values():
                for i in halls:
                    if i == play:
                        out += ("Sunday " + str(halls))
                        for key in self.Sunday.keys():
                            if self.Sunday[key] == halls:
                                out += " " + key + "\n"
        except:
            pass
        print(out)



