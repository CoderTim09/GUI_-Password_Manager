from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Constants
FONT = ("Arial", 12)

# ---------------------------- starify ------------------------------- #

def starify():
    current_show_atribute = password_input.cget("show")
    if current_show_atribute == "*":
        password_input.configure(show="")
    else:
        password_input.configure(show="*")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SEARCH ------------------------------- #

def search():
    with open("data.json", "r") as data_file:
        website = website_input.get().title()
        
        # Read file
        data = json.load(data_file)

        try:
            messagebox.showinfo(title=website.title(), message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        except KeyError: 
            pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website.title(): {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:           
                # Reading old data
                data = json.load(data_file)     
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:            
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.minsize(600, 350)
window.config(padx=50, pady=50)

# Canvas logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#  ------ Labels ------  #

# Website
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

# Email/email
usernam_label = Label(text="Email/email:", font=FONT)
usernam_label.grid(column=0, row=2)

# Password
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

#  ------ inputs/entries ------  #

# website input
website_input = Entry(width=51)
website_input.grid(column=1, row=1)
website_input.focus()

# Email/email input
email_input = Entry(width=70)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "tim@staberg.com")

# Password input
password_input = Entry(width=51)
password_input.grid(column=1, row=3)

#  ------ Buttons ------  #

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=60, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Search Button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

# Starify Button
star_button = Button(text="*", width=5, command=starify)
star_button.grid(column=3, row=3)


window.mainloop()