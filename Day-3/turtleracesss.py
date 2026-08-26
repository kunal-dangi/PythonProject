import random
import turtle
from turtle import Turtle, Screen

is_bet_ON = False
screen = Screen()

screen.setup(width= 500, height= 400)

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?, Choose one color: ")
print(user_bet)

all_turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(-230, -50 + i * 30)
    t.color(colors[i])
    all_turtles.append(t)

if user_bet:
    is_bet_ON = True

while is_bet_ON:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_bet_ON = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win Rascal!!, {winning_color} Turtle Has finished first!!")
            else:
                print(f"HAHA It's not that easy!!, {winning_color} Turtle Has finished first!!. YOU LOSE LOSER")


        dist = random.randint(1, 5)
        turtle.forward(dist)


screen.exitonclick()
