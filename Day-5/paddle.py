from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=6, stretch_len=2)
        self.color("white")
        self.goto(x, y)

    def go_up(self):
        self.speed("fastest")
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        self.speed("fastest")
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

