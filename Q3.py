# Import libraries
import random
from tkinter import *
from tkinter import messagebox

# Create the main window, set the size and title
root = Tk()
root.geometry("500x300")
root.title("GXBank Berhad")

# List of usernames and passwords
username_list = ["howjieying", "foojiaxing", "ngkaylyn",
                 "chanyuanlin", "cherlywongexing", "siowqifeng",
                 "chongyuanwei", "gohsiying", "lavaniaachandramohan",
                 "nurulhumaidahsherin"]
password_list = ["1002371013", "1002371198", "1002372193", "1002371497",
                 "1002371070", "1002371213", "1002372877", "1002371454",
                 "1002372380", "1002370878"]

# Need to map the username_list to password_list
user_credentials = {username_list[i]: password_list[i] for i in range(len(username_list))}

# Initialize attempts
attempts = 0

# Variable to store the generated TAC
generated_tac = None


# Function to generate TAC
def generate_tac():
    return random.randint(100, 999)


# Function to validate TAC
def validate_tac():
    global generated_tac
    tac_input = tac_value.get()
    if tac_input == str(generated_tac):
        messagebox.showinfo("Success", "Customer validated successfully")
        tac_entry.config(state=DISABLED)  # Disables entries upon successful validation
        display_options()
    elif tac_input == str():
        messagebox.showinfo("Invalid", "Please enter TAC")
    else:
        messagebox.showerror("Error", "Invalid TAC. Exiting...")
        root.quit()


# Function to display the banking options
def display_options():
    options_label.grid(row=6, column=0, columnspan=100, padx=120, pady=10)


# Function to handle the login
def login():
    global attempts, generated_tac
    user = username_value.get()
    pwd = password_value.get()

    if not user or not pwd:
        messagebox.showerror("Invalid", "Please enter username or password")
        return ()

    if user in user_credentials and user_credentials[user] == pwd:
        generated_tac = generate_tac()
        messagebox.showinfo("TAC", f"TAC generated: {generated_tac}")
        username_entry.config(state=DISABLED)
        password_entry.config(state=DISABLED)
        tac.grid(row=4, column=2)
        tac_entry.grid(row=4, column=3)
        validate_tac_button.grid(row=5, column=3)
    else:
        attempts += 1
        if attempts < 3:
            messagebox.showerror("Error", f"Invalid username or password. Attempt {attempts}")
        else:
            messagebox.showerror("Error", "Too many failed attempts. Exiting...")
            root.quit()


# Heading of the window
Label(root, text="Welcome to Our Banking App!", font="Helvetica 12 underline").grid(row=0, column=2, padx=5, pady=5)

# Variable for storing data
username_value = StringVar()
password_value = StringVar()
tac_value = StringVar()

# Username label and entry
username = Label(root, text="Username :", font="Times 12 bold")
username.grid(row=1, column=2)
username_entry = Entry(root, textvariable=username_value)
username_entry.grid(row=1, column=3)

# Password label and entry
password = Label(root, text="Password :", font="Times 12 bold")
password.grid(row=2, column=2)
password_entry = Entry(root, textvariable=password_value)
password_entry.grid(row=2, column=3)

# Login button
login_button = Button(root, text="Login", command=login, font="Arial 11 bold", fg="blue")
login_button.grid(row=3, column=3)

# TAC label and entry
tac = Label(root, text="Enter TAC :", font="Times 12 bold")
tac.grid(row=4, column=2)
tac_entry = Entry(root, textvariable=tac_value)
tac_entry.grid(row=4, column=3)

# Validate TAC button
validate_tac_button = Button(root, text="Validate TAC", command=validate_tac, font="Arial 11 bold", fg="blue")
validate_tac_button.grid(row=5, column=3)

# Banking options label
options_label = Label(root, text="Banking options available:\n- Transfer\n- Top-up\n- Make payments\n- Receive money",
                      font="Times 12", justify=LEFT)

# Run the code
root.mainloop()
