from tkinter import *
# if you are gonna use whole lot of classes from tkinter then import this
# otherwise just import tkinter and use tkinter.functionName()
window= Tk()



window.title("GUI")
window.minsize(500,200)

Label = Label(text = "I am alone!!!")
Label.pack()




window.mainloop()
# something like screen.exitonclick() in turtle... used for keeping the window alive basically