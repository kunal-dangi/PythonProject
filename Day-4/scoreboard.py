from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))

#    def increase_score(self):
#        self.score += 1
 #       self.clear()
 #       self.write(f"Score: {self.score}, High Score: {self.highscore}", align="center", font=("Courier", 24, "bold"))


#    def game_over(self):
#        self.goto(0, 0)
#        self.write("GAME OVER...", align="center", font=("Courier", 24, "bold"))


    def Update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align="center", font=("Courier", 24, "bold"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.Update()

    def increase_score(self):
        self.score += 1
        self.Update()