# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

def save_password():
    web = input1.get()
    email = input2.get()
    password = input3.get()
    with open("data.txt", "w") as f:
        f.write(web + "  |  " + email + "  |  " + password + "\n")


# UI SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=50)

canvas = Canvas(window, width=400, height=500, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(200, 250, image=photo)
canvas.grid(column=1, row=0, columnspan=2)

WebEntry = Label(window, text="Website: ", fg="white", font=("Arial", 25))
WebEntry.grid(column=0, row=1, sticky = "e")

Email = Label(window, text="Email/Username: ", fg="white", font=("Arial", 25))
Email.grid(column=0, row=2, sticky = "e")

Password = Label(window, text="Password: ", fg="white", font=("Arial", 25))
Password.grid(column=0, row=3, sticky = "e")

input1 = Entry(window , width=45, bd=3)
input1.grid(column=1, row=1, columnspan=2, sticky = "w")
input1.focus()

input2 = Entry(window , width=45, bd=3)
input2.grid(column=1, row=2, columnspan=2, sticky = "w")
input2.insert(0, "kunal432344@gmail.com")

input3 = Entry(window , width= 20, bd=3)
input3.grid(column=1, row=3, sticky = "w")
# sticky keeps it sticky to a direction in a column,,, columnspan increases the reach of widget to more than 1 column

button = Button(window, text = "Generate Password", fg="black", font=("Arial", 25))
button.grid(column = 2, row=3, sticky = "w")

button2 = Button(window, text = "Add", fg="black", font=("Arial", 25), width=40, command=save_password)
button2.grid(column = 1, row = 4, columnspan=2)

window.mainloop()
