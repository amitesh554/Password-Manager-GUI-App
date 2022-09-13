from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letter + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_e.insert(0, password)


def save():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()
    new_data = {
        website: {
            "Email": email,
            'Password': password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="OOPS", message="Please Fill all the details")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read an old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file)
        else:
            # Update old data to new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Write new data into json file
                json.dump(data, data_file)

        finally:
            website_e.delete(0, END)
            email_e.delete(0, END)
            password_e.delete(0, END)


def find_password():
    website=website_e.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="Data File not found")
    else:
        if website in data:
            Email=data[website]["Email"]
            Password=data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email:{Email}\nPassword:{Password}")
        else:
            messagebox.showinfo(title="Error",message=f"No datails of {website} exists")



window = Tk()
window.minsize(width=400, height=400)
window.title("Password Manager")
window.config(padx=25, pady=25)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_l = Label(text="Website")
website_l.grid(row=1, column=0)
email_l = Label(text="Email")
email_l.grid(row=2, column=0)
password_l = Label(text="Password")
password_l.grid(row=3, column=0)

# Entry

website_e = Entry(width=35)
website_e.grid(row=1, column=1)
website_e.focus()
email_e = Entry(width=35)
email_e.grid(row=2, column=1)
password_e = Entry(width=35)
password_e.grid(row=3, column=1)

# Button

generate_pass_b = Button(text="Generate Password", command=generate_pass)
generate_pass_b.grid(row=3, column=2)
add_b = Button(text="Add", width=20, command=save)
add_b.grid(row=4, column=1)
add_search_b=Button(text="Search",width=10,command=find_password)
add_search_b.grid(row=1,column=2)
window.mainloop()
