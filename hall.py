halls = []


class Hall:
    def __init__(self, name, capacity):
        """
        A generic Hall class constructor having a name and capacity.
        :param name: The name of the Hall
        :param capacity: The Capacity of the Hall
        """
        self.name = name
        self.capacity = capacity
        self.lines = []
        self.luxury = False

    def add_line_of_seats(self, line):
        """
        Add a line of seats on the hall at the end
        :param line: Insert an Array of Integers(prefer sorted) to be appended on the end of lines Array
        :return: If the number of seats to be added is more than the capacity it returns an error message
        """
        if (self.get_number_of_seats() + len(line)) < self.capacity:
                self.lines.append(line)
        else:
            return "No more capacity to add Seats"

    def set_luxury_seats(self):
        """
        set a hall to have Luxury seats
        """
        self.luxury = True

    def get_number_of_seats(self):
        """
        Give the current Capacity of the Hall
        :return: An integer of the Capacity of the Hall
        """
        current_cap = 0
        for line in self.lines:
            current_cap += len(line)
        return current_cap

    def create_line_of_seats(self, num_of_seats):
        """
        Creates a Line of seats to be added as an Array of integers
        :param num_of_seats: Insert the number of seats you want to add in a line
        :return: return an array for a line e.g. if number of seats is 3 will return [1, 2, 3]
        """
        line = []
        for i in range(1,num_of_seats):
            line.append(i)
        return line
