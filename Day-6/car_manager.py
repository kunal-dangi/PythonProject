import random
from turtle import Turtle


COLOURS = ['red','green','blue','yellow','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10





class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def Cars(self):
        random_no = random.randint(0,4)
        if random_no == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)


    def Cars_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def Lvl_up(self):
        self.car_speed += MOVE_INCREMENT
