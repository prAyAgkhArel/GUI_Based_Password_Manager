import json
import random
from tkinter import *
from tkinter import messagebox               # this is not tkinter's class it is also a module
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)                   #copies password to clip board automatically
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():   #this is called when user clicks add button

    email = username_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    new_dict = {
        website: {
            "email":email,
        "password":password,
        }
    }

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="!!" , message="You left some fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)
        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_dict, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent= 4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)  #creating Canvas object
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo)
canvas.grid(row=0, column=1)

#website label and entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="W")  # label sticks to left side of the grid
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()  # cursor preappears on the entry

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="E")
username_entry = Entry(width=42)
username_entry.grid(row=2, column=1, columnspan=2, sticky="W")
username_entry.insert(0, "e.g. prayagkharel@gmail.com")  #starting string in entry

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky= "W")
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, sticky= "W")

button_add = Button(text="Add", width=35, command=save, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2, sticky="W")

generate_password_button = Button(text= "Generate Password", command = generate_password, highlightthickness=0)
generate_password_button.grid(row=3, column=1, columnspan=2,  sticky="E")



window.mainloop()