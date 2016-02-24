from hall import Hall
from theaterHall import TheaterHall
from cinemaHall import CinemaHall

hall = Hall("paok", 300)
hall.add_line_of_seats([1, 2, 3])
hall.add_line_of_seats([1, 2, 3])
for i in range(1,2):
    hall.add_line_of_seats([1, 3, 4, 5])

hall.add_line_of_seats(hall.create_line_of_seats(10))

print(hall.get_number_of_seats())

