import turtle as t
from turtle import Screen
screen = Screen()

def moveForward():
    t.forward(10)

def moveBackward():
    t.backward(10)

def RotateClockwise():
    t.right(10)

def RotateAnticlockwise():
    t.left(10)

def ClearScreen():
    t.clear()

screen.listen()
screen.onkey(key="w", fun = moveForward)
screen.onkey(key="s", fun = moveBackward)
screen.onkey(key="a", fun = RotateClockwise)
screen.onkey(key="d", fun = RotateAnticlockwise)
screen.onkey(key = "c", fun = ClearScreen)

screen.exitonclick()