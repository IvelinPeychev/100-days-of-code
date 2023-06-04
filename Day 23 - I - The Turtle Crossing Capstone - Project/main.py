from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle crossing')
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detection of collisions with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful level completion
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.leve_up()
        scoreboard.increase_level()



screen.exitonclick()
