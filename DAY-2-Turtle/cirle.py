import turtle as t
from turtle import Screen
import random

t.colormode(255)

def random_color():
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    return (r, g, b)

t.speed("fastest")
def spirograph(size):
    for _ in range(int(360 / size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size)

# We can jus do it by writing t.left(10) and boom our spiral is ready but to make it stop exactly after it moves 360
# degree, we have to use heading() and we have to use setheading() to make sure its working fine!!!

# still if you just don't care about things like that than you could just use left or right but keep one thing in mind
# to provide sufficient number of repeatations in the range of loop , if not then the circles just stop mid-way and the
# spirograph will never complete !!!!!!!!!




spirograph(10)

screen = Screen()
screen.exitonclick()