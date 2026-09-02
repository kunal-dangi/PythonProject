from turtle import Turtle

STARTING_POSITION = (0,-280)
FINISHING_POSITION = 280
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.Is_At_START()
        self.setheading(90)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.left(90)

    def move_right(self):
        self.right(90)


    def Is_At_START(self):
        self.goto(STARTING_POSITION)


    def Is_At_Finish(self):
        if self.ycor() > FINISHING_POSITION:
            return True
        else:
            return False
