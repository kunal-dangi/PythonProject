from tkinter import *
# if you are gonna use whole lot of classes from tkinter then import this
# otherwise just import tkinter and use tkinter.functionName()
window= Tk()



window.title("GUI")
window.minsize(500,200)

Label = Label(text = "I am alone!!!")
Label.pack()

#button

def button_clicked():
    new_input = input.get()
    Label.config(text=new_input)    # config used to change label


button = Button(text = "Click me" , command = button_clicked)
button.pack()

# Input

input = Entry()
input.pack()
input.get()
Label.config(text = input.get())

# as you may have noticed that we have to pack() everything whatever we want to show on the screen...
# there are 3 ways to do this as well(not only pack):
# 1> .pack() -> can select sides,,, default to top
# 2> .place() -> have to give exact coordinates on screen
# 3> .grid -> we can change whole screen in grids and decide a fix no. of rows and coloumns to divide screen in...
### keep in mind that we can't use 2 of them in our code,,, if write pack then continue pack and if we write pack
# and grid in same file... error!!


window.mainloop()
# something like screen.exitonclick() in turtle... used for keeping the window alive basically