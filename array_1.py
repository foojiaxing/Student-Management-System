import numpy as np
arr = np.array([1,2,3])
print(arr)


while True:  #if invalid, asks the input again
    power_consumption = int(input("Enter your house power consumption:"))
    if power_consumption < 1:
        print("Invalid input")
        continue #skips rest of the loop and asks the input again
    else:
        break #break when it is valid-go to next step

# BREAK and CONTINUE only can be used when in a loop (while, for)
# RETURN-(invalid) only can be used in def function

if 1 <= power_consumption <= 200:
    charge = 0.218 * power_consumption
    print(charge)
elif 201 <= power_consumption <= 500:
    charge = 0.334 * power_consumption
    print(charge)
elif 301 <= power_consumption <= 600:
    charge = 0.516 * power_consumption
    print(charge)
elif 601 <= power_consumption <= 900:
    charge = 0.546 * power_consumption
    print(charge)
elif power_consumption >= 900:
    charge = 0.571 * power_consumption
    print(charge)

if charge < 100:
    print("Invalid, there is no discount")
elif 100 <= charge <= 200:
    charge_after_discount = charge * 0.95
    print(charge_after_discount)
elif 201 <= charge <= 500:
    charge_after_discount = charge * 0.90
    print(charge_after_discount)
elif charge >= 501:
    charge_after_discount = charge * 0.85
    print(charge_after_discount)


# if invalid, will not ask input again (absence of while loop)
power_consumption = int(input("Enter your house power consumption:"))
if power_consumption < 1:
    print("Invalid input")

if 1 <= power_consumption <= 200:
    charge = 0.218 * power_consumption
    print(charge)
elif 201 <= power_consumption <= 500:
    charge = 0.334 * power_consumption
    print(charge)
elif 301 <= power_consumption <= 600:
    charge = 0.516 * power_consumption
    print(charge)
elif 601 <= power_consumption <= 900:
    charge = 0.546 * power_consumption
    print(charge)
elif power_consumption >= 900:
    charge = 0.571 * power_consumption
    print(charge)

if charge < 100:
    print("Invalid, there is no discount")
elif 100 <= charge <= 200:
    charge_after_discount = charge * 0.95
    print(charge_after_discount)
elif 201 <= charge <= 500:
    charge_after_discount = charge * 0.90
    print(charge_after_discount)
elif charge >= 501:
    charge_after_discount = charge * 0.85
    print(charge_after_discount)



charge = 0
# if invalid, will not ask input again (absence of while loop)
power_consumption = int(input("Enter your house power consumption:"))
if power_consumption < 1:
    print("Invalid input")

if 1 <= power_consumption <= 200:
    charge = 0.218 * power_consumption
elif 201 <= power_consumption <= 500:
    charge = 0.334 * power_consumption
elif 301 <= power_consumption <= 600:
    charge = 0.516 * power_consumption
elif 601 <= power_consumption <= 900:
    charge = 0.546 * power_consumption
elif power_consumption >= 900:
    charge = 0.571 * power_consumption

print(charge)

charge_after_discount = 0
if charge < 100:
    print("Invalid, there is no discount")
elif 100 <= charge <= 200:
    charge_after_discount = charge * 0.95
elif 201 <= charge <= 500:
    charge_after_discount = charge * 0.90
elif charge >= 501:
    charge_after_discount = charge * 0.85

print(charge_after_discount)


charge = 0
def electricity_bill():
    global charge
    power_consumption = int(input("Enter your house power consumption:"))
    if power_consumption < 1:
        print("Invalid input")
        return  # Invalid(return)

    if 1 <= power_consumption <= 200:
        charge = 0.218 * power_consumption
    elif 201 <= power_consumption <= 500:
        charge = 0.334 * power_consumption
    elif 301 <= power_consumption <= 600:
        charge = 0.516 * power_consumption
    elif 601 <= power_consumption <= 900:
        charge = 0.546 * power_consumption
    elif power_consumption >= 900:
        charge = 0.571 * power_consumption

    print(f"The total charge before discount: RM{charge:.2f}")


def rebate():
    charge_after_discount = 0
    if charge < 100:
        print("Invalid, there is no discount")
        return  # Invalid(return)

    # local charge_after_discount
    elif 100 <= charge <= 200:
        charge_after_discount = charge * 0.95
    elif 201 <= charge <= 500:
        charge_after_discount = charge * 0.90
    elif charge >= 501:
        charge_after_discount = charge * 0.85

    print(f"The total charge after discount: RM{charge_after_discount:.2f}")


# call back the function
electricity_bill()
rebate()