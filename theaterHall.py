from hall import Hall


class TheaterHall(Hall):

    NumOfBalcony = 0
    NumOfDressingRoom = 0

    def add_balcony(self, num):
        """
        Adds Balcony to a TheaterHall
        :param num: Number of Balcony to be added. Can be a negative number
        """
        self.NumOfBalcony += num

    def add_dressing_room(self, num):
        """
        Adds Dressing Rooms to a TheaterHall
        :param num: Number of Dressing Rooms to be added. Can be negative number
        """
        self.NumOfDressingRoom += num
