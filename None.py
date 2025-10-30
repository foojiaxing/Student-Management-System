from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("GXBank Berhad")

# Heading
Label(root, text="Welcome to Our Banking App!", font="Helvetica 13 bold").grid(row=0, column=2)

# Variable for storing data
username_value = StringVar()
password_value = StringVar()
tac_value = StringVar()

# Username and Entry
username = Label(root, text="Username :")
username.grid(row=1, column=2)
username_entry = Entry(root, textvariable=username_value)
username_entry.grid(row=1, column=3)

# Password and Entry
password = Label(root, text="Password :")
password.grid(row=2, column=2)
password_entry = Entry(root, textvariable=password_value)
password_entry.grid(row=2, column=3)

# Login button
Button(text="Login", command=login).grid(row=3, column=3)

# TAC Label and Entry (Hidden initially)
tac = Label(root, text="Enter TAC :")
tac.grid(row=4, column=2)
tac_entry = Entry(root, textvariable=tac_value)
tac_entry.grid(row=4, column=3)

# Validate TAC Button (Hidden initially)
validate_tac_button = Button(root, text="Validate Tac", command=validate_tac).grid(row=5, column=3)

# Banking Options Label (Hidden initially)
password = Label(root, text="Banking options available:\nTransfer\nTop-up\nMake payments\nReceive money")

root.mainloop()
