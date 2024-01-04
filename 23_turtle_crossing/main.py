import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road")
screen.bgcolor('black')
screen.tracer(0)

# creating objects from the classes
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# only up key is valid
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # to check collision with a car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # to see if the player crossed the road safely
    if player.is_at_finish_line():
        cars.next_level()
        scoreboard.increase_level()
        player.go_to_start()


screen.exitonclick()