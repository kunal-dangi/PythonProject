from turtle import Turtle

FONT = ("Courier", 20, "normal")

class SB(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def KO(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)