from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# TIMER MECHANISM

def Timer():
    global reps
    WORK_SECS = WORK_MIN * 60
    SHORT_BREAK = SHORT_BREAK_MIN
    LONG_BREAK = LONG_BREAK_MIN
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK)
    else:
        count_down(WORK_SECS)

# COUNTDOWN MECHANISM

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count >=  0 and count_sec <10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}" )
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        Timer()

# UI SETUP

window = Tk()
window.title("tomato timer")
window.config(padx = 100, pady = 100, bg = YELLOW)


heading = Label(text= "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40, "italic"))
heading.grid(column = 1, row = 0)

button = Button(
    text="start",
    fg=GREEN,
    bg=YELLOW,
    activebackground=YELLOW,
    highlightbackground=YELLOW,  # macOS border/focus color
    bd=0,
    relief="flat",
    command = Timer
)
button.grid(column=0, row=2)


button2 = Button(
    text="reset",
    fg=GREEN,
    bg=YELLOW,
    activebackground=YELLOW,
    highlightbackground=YELLOW,
    bd=0,
    relief="flat"
)
button2.grid(column=3, row=2)

ticks = Label(text = "✓", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 15, "italic"))
ticks.grid(column = 1, row = 3)

canvas = Canvas(width = 250, height = 244, bg = YELLOW, highlightthickness=0)
tomato = PhotoImage(file = "tomato.png") # a method to read image in canvas/tkinter {{file takes path to file as an input}}
canvas.create_image(125, 122, image =tomato) # you can't just write the file name in image section and play happy ending
text_timer = canvas.create_text(125, 135, text = "00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

window.mainloop()