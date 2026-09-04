import turtle as t
import pandas as pd
screen= t.Screen()

screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)

answer_state = screen.textinput(title = f"{}/50 states Correct" , prompt = "Guess the State of the US State Guessing Game ")

t.shape(image)

screen.exitonclick()
