from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # random numbers of letters, numbers abd symbols
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # creation of the password
    random_password = random.choices(letters, k=nr_letters) + random.choices(numbers, k=nr_numbers)+ random.choices(symbols, k=nr_symbols)
    random.shuffle(random_password)
    random_password = ''.join(random_password)

    # clearing whatever is there in password entry box and writing out generated password there
    password_entry.delete(0, 'end')
    password_entry.insert(0, random_password)
    # copying our generated password to the clipboard
    pyperclip.copy(random_password)

# ---------------------------- SEARCH DATA ------------------------------- #
def search_data():
    try:
        with open('data.json', 'r') as read_file:
        # reading the old data
            data = json.load(read_file)
        cred = data[website_entry.get()]
        messagebox.showinfo(title="credentials", message=f"Website: {website_entry.get()}\nEmail: {cred['Email']}\nPassword: {cred['Password']}")
    except FileNotFoundError:
        messagebox.showerror(message="File not found")
    except KeyError:
        messagebox.showerror(message="Data not found")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # getting the entried variables
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            'Email': email,
            'Password': password
        }
    }

    # if the user left any box empty, there will be a popup and it won't save the data
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty boxes")
        return
    
    try: # if the data.json file already exists, this will work
        with open('data.json', 'r') as read_file:
            # reading the old data
            data = json.load(read_file)
            # updating the old data with the new data
            data.update(new_data)
    
    except FileNotFoundError:
        data = new_data

    # writing to the data.json with the updated data
    with open("data.json", 'w') as file:
        json.dump(data, file, indent=4)

    # clears the website and password entry
    website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady=50)

# creating a canvas to load the image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
# 100, 100 to put it in the middle i.e., the half of height and width
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row=0, column=1)

# adding the website label and entry box
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=17)
# focus takes the curser and puts it in the entry box
website_entry.focus()
# columnspan stretches the box into 2 columns
website_entry.grid(row=1, column= 1)

# adding enail label and entry box
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=36)
# starts with my email id as default. 0 means at the beginning of the entry
email_entry.insert(0, 'binduhegdee@gmail.com')
email_entry.grid(row=2, column= 1, columnspan=2)

# creating password label and entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# adding the 2 buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=15)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', width=15, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()