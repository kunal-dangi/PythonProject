from tkinter import *
window = Tk()

window.minsize(400, 300)
window.title("Converter")

inputs = Entry(width = 5)
inputs.grid(column = 1, row = 0)
inputs.get()

label = Label(text = "Miles")
label.grid(column = 3, row = 0)

IsEqualTo = Label(text = "is equal to")
IsEqualTo.grid(column = 0, row = 1)

zero = Label(text = "0")
zero.grid(column = 1, row = 1)

km = Label(text = "kilometers")
km.grid(column = 2, row = 1)

def Button_called():
    nextint = float(float(inputs.get()) * 1.60934)
    zero.config(text = nextint)


button = Button(text = "Convert", command = Button_called)
button.grid(column = 1, row = 2)

window.mainloop()