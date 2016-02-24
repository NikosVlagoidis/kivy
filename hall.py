class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.lines = []
        self.luxury = False

    def add_line_of_seats(self, line):
        if (self.get_number_of_seats() + len(line)) < self.capacity:
                self.lines.append(line)
        else:
            return "No more capacity to add Seats"

    def add_luxury_seats(self):
        self.luxury = True

    def get_number_of_seats(self):
        current_cap = 0
        for line in self.lines:
            current_cap += len(line)
        return current_cap

    def create_line_of_seats(self, num_of_seats):
        line = []
        for i in range(1,num_of_seats):
            line.append(i)
        return line
