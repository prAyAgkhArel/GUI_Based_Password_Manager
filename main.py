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

    email = email_entry.get()
    website = website_entry.get().lower()   # saved in small case to compare when user clicks search button
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


# .........................SEARCH FUNCTION..............................................#
def search():
    website = website_entry.get().lower()
    email_entry.delete(0, END)
    try:
        with open("data.json", mode ="r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            password_entry.insert(0, password)
            email_entry.insert(0,  email)
    except:
        messagebox.showerror(title="Error", message="Data not found")


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
website_entry = Entry(width=23)
website_entry.grid(row=1, column=1, sticky="W")
website_entry.focus()  # cursor preappears on the entry

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")
email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, string="prayagkharel006@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky= "W")
password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, sticky= "W")

button_add = Button(text="Add", width=35, command=save, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2, sticky="W")

generate_password_button = Button(text= "Generate Password", command = generate_password, highlightthickness=0)
generate_password_button.grid(row=3, column=1, columnspan=2,  sticky="E")

search_button = Button(text= "Search", width= 14, highlightthickness=0, command= search)
search_button.grid(row=1, column = 1, columnspan=2, sticky = "E")



window.mainloop()
