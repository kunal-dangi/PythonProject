# PASSWORD GENERATOR->

from tkinter import *
from tkinter import messagebox as mbox, messagebox
import random
import pyperclip
import json
from json import JSONDecodeError


def save_password():
    web = input1.get()
    email = input2.get()
    passwordEntry = input3.get()
    new_data = {web:{
        "email": email,
        "password": passwordEntry
    }}

    if len(web) == 0 or len(email) == 0 or len(passwordEntry) == 0:
        messagebox.showerror("Error", "Please enter all required information")
    else:
        is_ok = mbox.askokcancel(title="website",message = f"These are the details entered: \nEmail: {email} "
                                                f"\nPassword: {passwordEntry} \nIs it ok to save?")

        if is_ok:
            data = {}
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)                 # to read data from a json file!!
                data.update(new_data)               # to update the already present data
            except FileNotFoundError:
                data = new_data
            except JSONDecodeError:
                data = new_data
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)        # to write the updated data in json {indent = 4, for  better looks}
            input1.delete(0, END)
            input3.delete(0, END)

# Random Password Generator ->

def Generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    input3.insert(0, password)
    pyperclip.copy(password)



def Search():
    web = input1.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")
    except JSONDecodeError:
        messagebox.showerror("Error", "data.json is empty or invalid")
    else:
        if web in data:
            entry = data[web]
            messagebox.showinfo(
                title=web,
                message=f"Email: {entry['email']}\nPassword: {entry['password']}"
            )
        else:
            messagebox.showerror("Error", f"No details found for {web}")





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

button = Button(window, text = "Generate Password", fg="black", font=("Arial", 25), command=Generate_password)
button.grid(column = 2, row=3, sticky = "w")

button2 = Button(window, text = "Add", fg="black", font=("Arial", 25), width=40, command=save_password)
button2.grid(column = 1, row = 4, columnspan=2)

button3 = Button(window, text = "Search", fg="black", font=("Arial", 25), width=10, command=Search)
button3.grid(column = 2, row = 1, columnspan=1)

window.mainloop()
