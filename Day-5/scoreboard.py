from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto( -100, 210)
        self.write(f"SCORE: {self.score1}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 210)
        self.write(f"SCORE: {self.score2}", align="center", font=("Courier", 24, "normal"))
