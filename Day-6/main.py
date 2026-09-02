from idlelib.configdialog import tracers
from turtle import Turtle, Screen, tracer
import time
from player import Player

from car_manager import CarManager

from sb import SB


screen = Screen()

screen.setup(width=600, height=600)

screen,tracer(0)

player = Player()
car_manager = CarManager()
sb = SB()

screen.listen()
screen.onkey(player.move_up , "w")
screen.onkey(player.move_left , "a")
screen.onkey(player.move_right , "d")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.Cars()
    car_manager.Cars_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            sb.KO()


        if player.Is_At_Finish():
            player.Is_At_START()
            car_manager.Lvl_up()





screen.exitonclick()