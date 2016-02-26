from hall import Hall
from theaterHall import TheaterHall
from cinemaHall import CinemaHall
from week_schedule import Week_Schedule
from play import Play

hall = Hall("Hall 1", 300)
hall2 = Hall("Hall 2", 500)

jamesbond = Play()
jamesbond.set_name("James Bond")
schedule = Week_Schedule()
lotr = Play()
lotr.set_name("Lord of the Rings")

schedule.set_play_date(jamesbond, "Monday", hall, ["12,30", "14,40", "16.30"])
schedule.set_play_date(jamesbond, "Monday", hall2, "17.00")
schedule.set_play_date(jamesbond, "Tuesday", hall2, "17.00")
schedule.set_play_date(lotr, "Sunday", hall2, "13.00")



schedule.find_day_for_play(lotr.name)
schedule.find_day_for_play(jamesbond.name)
