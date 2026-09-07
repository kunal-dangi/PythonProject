import turtle as t
import pandas as pd
screen= t.Screen()

screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)

guesses = []

while len(guesses) < 50:
    answer_state = screen.textinput(title = f"{len(guesses)}/50 states Correct" , prompt = "Guess the State of the US State Guessing Game ").title()

    t.shape(image)

    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state == "Exit":
        states = [item for item in all_states if item not in guesses]
        pd.DataFrame(states).to_csv("remaining.csv")
        break

    if answer_state in all_states:
        guesses.append(answer_state)
        n = t.Turtle()
        n.hideturtle()
        n.penup()
        state = data[data.state == answer_state]
        x = int(state.x.values[0])         # we can also use another attribute here named item(), it also grabs 1st element
        # only.
        y = int(state.y.values[0])
        n.goto(x, y)
        n.write(answer_state, align = "center", font = ("Arial", 10, "bold"))




