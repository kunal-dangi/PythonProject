from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
cycle = 0
timer = None

# TIMER RESET

def Reset():
    global reps
    global cycle
    ticks.config(text = "_", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 15, "italic"))
    heading.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "italic"))
    canvas.itemconfig(text_timer, text="00:00")
    cycle = 0
    reps = 0
    window.after_cancel(timer)



def Tick_counter():
    global reps
    global cycle
    global text_timer
    global heading
    if reps % 8 == 0:
        cycle += 1
        NoOfTics = "✓" * cycle
        ticks.config(text = f"{NoOfTics}", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 15, "italic"))


# TIMER MECHANISM

def Timer():
    global reps
    WORK_SECS = WORK_MIN * 60
    SHORT_BREAK = SHORT_BREAK_MIN * 60
    LONG_BREAK = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        heading.config(text = "Long-Break", font = (FONT_NAME, 25, "italic"))
        count_down(LONG_BREAK)
    elif reps % 2 == 0:
        heading.config(text="Short-Break", font=(FONT_NAME, 25, "italic"))
        count_down(SHORT_BREAK)
    else:
        heading.config(text="Work", font=(FONT_NAME, 25, "italic"))
        count_down(WORK_SECS)

# COUNTDOWN MECHANISM

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count >=  0 and count_sec <10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}" )
    if count > 0:
        timer = window.after(1000, count_down, count-60)
    else:
        Timer()
        Tick_counter()

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
    relief="flat",
    command=Reset
)
button2.grid(column=3, row=2)

ticks = Label(text = "_", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 15, "italic"))
ticks.grid(column = 1, row = 3)

canvas = Canvas(width = 250, height = 244, bg = YELLOW, highlightthickness=0)
tomato = PhotoImage(file = "tomato.png") # a method to read image in canvas/tkinter {{file takes path to file as an input}}
canvas.create_image(125, 122, image =tomato) # you can't just write the file name in image section and play happy ending
text_timer = canvas.create_text(125, 135, text = "00:00", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

window.mainloop()