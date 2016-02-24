from hall import Hall


class TheaterHall(Hall):

    NumOfBalcony = 0
    NumOfDressingRoom = 0

    def add_balcony(self, num):
        self.NumOfBalcony += num

    def add_dressing_room(self, num):
        self.NumOfDressingRoom += num
