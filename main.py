from tkinter import *
from tkinter import messagebox
import random
import json


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
spec_chars = ['!', '@', "#", '$', '%', '^', '&', '*', "(", ")"]


# --------- SEARCHING THROUGH DATABASE -----------#
def search():
    website = web_text.get()
    try:
        with open('passwords.json', mode='r') as data_file:
            # Reading the old data
            data = json.load(data_file)
            if website in data:
                email = data[website]['email']
                pw = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password: {pw}\n')
    except KeyError:
        messagebox.showinfo(title='Error', message='No data file found.')
    except UnboundLocalError:
        messagebox.showinfo(title='Error', message='No data file found.')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data file found.')


# ------------ PASSWORD GENERATOR ----------------#
def password_generator():
    pw_text.delete(0, END)
    gen_pw = ''
    ran_cap = random.choice(alphabet).upper()
    gen_pw += ran_cap
    for _ in range(0, 7):
        _ = random.choice(alphabet)
        gen_pw += str(_)
    for _ in range(0, 4):
        _ = random.randint(0, 9)
        gen_pw += str(_)
    for _ in range(0, 2):
        _ = random.choice(spec_chars)
        gen_pw += str(_)
    pw_text.insert(0, gen_pw)


# -------------- SAVE PASSWORD -------------------#

def saving_password():
    website = web_text.get()
    email = account_text.get()
    password = pw_text.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty fields detected', message='You left some fields empty, please rectify this '
                                                                   'situation in order to continue.')
    else:
        try:
            with open('passwords.json', mode='r') as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('passwords.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('passwords.json', mode='w') as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_text.delete(0, END)
            account_text.delete(0, END)
            pw_text.delete(0, END)



# ----------------- UI SETUP ----------------------#
window = Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

background = Canvas(width=200, height=200)
pass_logo = PhotoImage(file='logo.png')
background.create_image(100, 100, image=pass_logo)
background.grid(column=1, row=0)

# website
web_label = Label(text='Website: ', font=('Arial', 12))
web_label.grid(column=0, row=1)

web_text = Entry()
web_text.grid(column=1, row=1)
web_text.focus()

search_button = Button(text='Search', width=13, command=search)
search_button.grid(column=2, row=1)

# email or username
account = Label(text='Email/Username: ', font=('Arial', 12))
account.grid(column=0, row=2)

account_text = Entry(width=35)
account_text.grid(column=1, row=2, columnspan=2)
account_text.insert(0, 'your@email.com')

# Password
pw = Label(text='Password: ', font=('Arial', 12))
pw.grid(column=0, row=3)

pw_text = Entry(width=21)
pw_text.grid(column=1, row=3)

# add button
add_button = Button(text='Add', width=36, command=saving_password)
add_button.grid(column=1, row=4, columnspan=2)

# Generate Password Button
pw_button = Button(text='Generate Password', command=password_generator)
pw_button.grid(column=2, row=3)

window.mainloop()
