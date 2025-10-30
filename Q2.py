from tkinter import *

items = ["Apples", "Oranges", "Flour", "Milk", "Maggie Noodles", "Cooking oil", "Sugar"]

# Total no. of items purchased
total_items = len(items)

# Cost of each item purchased
Apples_cost = (1000 / 150) * 3
Oranges_cost = (800 / 100) * 2
Flour_cost = (2000 / 1000) * 40
Milk_cost = 12 * 6
Maggie_Noodles_cost = 10 * 2
Cooking_oil_cost = (2000 / 250) * 13
Sugar_cost = (3000 / 250) * 2

# Discount applied
Total_amount = Apples_cost + Oranges_cost + Flour_cost + Milk_cost + Maggie_Noodles_cost + Cooking_oil_cost + Sugar_cost
Discount = Total_amount * 5 / 100
Discountformember = f"{Discount:.2f}"

# The final amount to be paid
Final_amount = Total_amount - Discount

# Decoration
seperateline = "------------------------------------------"
B_1 = "{0:<20s}{1:>30s}".format("Item", "Amt(RM)")
B_2 = "{0:<20s}{1:>30s}".format("Apples", f"{Apples_cost:.2f}")
B_3 = "{0:<20s}{1:>28s}".format("Oranges", f"{Oranges_cost:.2f}")
B_4 = "{0:<20s}{1:>32s}".format("Flour", f"{Flour_cost:.2f}")
B_5 = "{0:<20s}{1:>32s}".format("Milk", f"{Milk_cost:.2f}")
B_6 = "{0:<20s}{1:>21s}".format("Maggie Noodles", f"{Maggie_Noodles_cost:.2f}")
B_7 = "{0:<20s}{1:>26s}".format("Cooking oil", f"{Cooking_oil_cost:.2f}")
B_8 = "{0:<20s}{1:>31s}".format("Sugar", f"{Sugar_cost:.2f}")
B_9 = "Total items: " + str(total_items)
B_10 = "{0:<20s}{1:>28s}".format("Sub Total", f"{Total_amount:.2f}")
B_11 = "{0:<20s}{1:>25s}".format("Discount(5%)", Discountformember)
B_12 = "{0:<20s}{1:>32s}".format("Total", f"{Final_amount:.2f}")

window = Tk()
window.title("Mr.XYZ payment")
titleforreceipt = "SPLATOON GROCER @ UCSI MALL"
Label(window, text=titleforreceipt).grid(row=0, column=0, padx=0, pady=0)
statesList = [seperateline, B_1, seperateline, B_2, B_3, B_4, B_5, B_6, B_7, B_8, seperateline, B_9, B_10, B_11, B_12]
lstNE = Listbox(window, width=34, height=16)
lstNE.grid(padx=60, pady=3)

# Insert the items into listbox
for item in statesList:
    lstNE.insert(END, item)

window.mainloop()
