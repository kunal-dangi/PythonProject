from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER...", align="center", font=("Courier", 24, "bold"))