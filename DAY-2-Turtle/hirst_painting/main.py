#import colorgram

#rgb = []
#colors = colorgram.extract('image.jpg', 30)

#for color in colors:
 #   r = color.rgb.r
 #   g = color.rgb.g
 #   b = color.rgb.b

#    new_colors = (r, g, b)
 #   rgb.append(new_colors)

#print(rgb)

# We have to do all this shit just to get this colors list mentioned below, !!
# Once we get this, we can comment out or just delete the code.!

import turtle as t
t.colormode(255)
import random
colors = [(204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]
numberOfDots = 101


t.speed("fastest")

t.penup()
t.setheading(225)
t.forward(200)
t.setheading(0)

for Dots in range(1, numberOfDots):
    t.pendown()
    t.dot(10, random.choice(colors))
    t.penup()
    t.pencolor(random.choice(colors))
    t.forward(20)

    if Dots % 10 == 0:
        t.setheading(90)
        t.forward(20)
        t.setheading(180)
        t.forward(200)
        t.setheading(0)

t.hideturtle()

from turtle import Screen
screen = Screen()
screen.exitonclick()