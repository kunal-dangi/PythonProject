from turtle import Turtle, Screen

Wakanda = Turtle()
Wakanda.shape("classic")
Wakanda.color("purple")
for _ in range(20):
    Wakanda.pendown()
    Wakanda.forward(10)
    Wakanda.penup()
    Wakanda.forward(5)


screen = Screen()
screen.exitonclick()
