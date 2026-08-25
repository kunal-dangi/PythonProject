from turtle import Turtle, Screen
import random_walk

tim = Turtle()

colors = ["red", "green", "blue", "yellow", "cyan", "magenta" , "DarkOrchid","IndianRed", "wheat" , "CornflowerBlue"]


def draw_polygon(number_of_sides):
    angle = 360 / number_of_sides
    for i in range(number_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range (3, 11):
    tim.pencolor(random_walk.choice(colors))
    draw_polygon(i)


screen = Screen()
screen.exitonclick()