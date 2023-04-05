from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    generated_pass = "".join(password_list)

    if password.get() != "":
        password.delete(0, END)

    password.insert(0, generated_pass)
    pyperclip.copy(generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def store_info():
    wb_name = website_name.get()
    u_name = user_name.get()
    pass_word = password.get()
    new_data = {
        wb_name: {
            "email": u_name,
            "password": pass_word,
        }
    }

    if wb_name == "" or pass_word == "":
        messagebox.showinfo(message="Please don't leave any fields empty")

    else:
        try:
            with open("my_file.json", 'r') as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("my_file.json", 'w') as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("my_file.json", 'w') as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_name.delete(0, END)
            password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_name.get()
    try:
        with open("my_file.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password_accessed = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password_accessed}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.move(mypass_img, 10, 10)
canvas.grid(row=0, column=1)

# Display Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entry Filling

website_name = Entry(width=22)
website_name.grid(row=1, column=1)
website_name.focus()

user_name = Entry(width=41)
user_name.grid(row=2, column=1, columnspan=2)
user_name.insert(0, "bhattvibhor123@gmail.com")

password = Entry(width=22)
password.grid(row=3, column=1)

# Execution Buttons

pass_gen_btn = Button(text="Generate Password", width=15, command=pass_gen)
pass_gen_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=38, command=store_info)
add_btn.grid(row=4, column=1, columnspan=2)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
