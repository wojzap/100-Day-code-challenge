from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_random_password():

    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 4
    nr_symbols = 4
    nr_numbers = 4

    password_letters = [random.choice(letters) for letter in range(0, nr_letters)]
    password_numbers = [random.choice(numbers) for number in range(0, nr_numbers)]
    password_symbols = [random.choice(symbols) for symbol in range(0, nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    randomised_password = "".join(password_list)

    password_entry.insert(0, randomised_password)
    pyperclip.copy(randomised_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    name = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {name}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            data = f"{website} | {name} | {password}\n"
            file = open("password_data.txt", mode="a")
            file.write(data)
            file.close()

            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="ew")
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="ew")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="ew")

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()
email_username_entry = Entry()
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")

generate_pass_button = Button(text="Generate Password", command=generate_random_password)
generate_pass_button.grid(row=3, column=2, sticky="ew")
add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")


window.mainloop()
