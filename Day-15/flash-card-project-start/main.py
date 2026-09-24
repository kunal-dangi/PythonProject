import random
from tkinter import *
import pandas as pd
import random

GREEN = "#B1DDC6"
dictionary = {}
try:
    data = pd.read_csv("data/remaining.csv")
except FileNotFoundError:
    original = pd.read_csv("data/french_words.csv")
    dictionary = original.to_dict("records")
else:
    dictionary = data.to_dict(orient="records")      # {orient="records"} is used to change the order of data
                                                 # we are getting in dictionary!!!
print(dictionary)
current = {}

def next_card():
    global current
    if not dictionary:
        canvas.itemconfig(card_title, text="No cards left", fill="Black")
        canvas.itemconfig(card_word, text="\u2728", fill="Black")
        return
    current = random.choice(dictionary)
    canvas.itemconfig(card_title, text ="French", fill = "Black")
    canvas.itemconfig(card_word, text = current["French"], fill = "Black")
    canvas.itemconfig(fg_image, image=photoFg)
    window.after(3000, func = flip_card)

def flip_card():
    global current
    # Flip the currently shown card; do not select a new one here
    if not current:
        return
    canvas.itemconfig(fg_image, image = photoBg)
    canvas.itemconfig(card_title, text ="English", fill = "White")
    canvas.itemconfig(card_word, text = current["English"], fill = "White")

def got_it():
    global current
    if not current:
        return
    try:
        dictionary.remove(current)
    except ValueError:
        pass
    pd.DataFrame(dictionary).to_csv("data/remaining.csv", index=False)
    current = {}
    next_card()



window = Tk()

window.title("Flashy Bi**h")

window.config(padx = 100, pady = 100, bg = GREEN)

canvas  = Canvas(window, width = 800, height = 600)
photoFg = PhotoImage(file = "images/card_front.png")
photoBg = PhotoImage(file="images/card_back.png")
fg_image = canvas.create_image(400, 300, image = photoFg)
card_title = canvas.create_text(370,150, text = "Title", font = ("Times New Roman", 24), fill = "Black")
card_word = canvas.create_text(370,350, text = "Word", font = ("Times New Roman", 18), fill = "Black")
canvas.grid(row = 0, column = 0, columnspan=2)

cross_button = PhotoImage(file = "images/wrong.png")
wrong = Button(image = cross_button , command = next_card)
wrong.grid(row = 1, column = 0)

tick_button = PhotoImage(file = "images/right.png")
gotcha = Button(image = tick_button, command = got_it)
gotcha.grid(row = 1, column = 1)

canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(row = 0, column = 0)

# Show the first card immediately
next_card()

window.mainloop()