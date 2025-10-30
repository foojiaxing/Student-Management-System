from array_1 import charge_after_discount

list = [1,2,3,4,5,6]
print(list[1:3])

list = [1,2,3,4,5,6]
print(list.index(6))


list = [1,2,3,4,5,6]
list.insert(4,6)
print(list)

list = [1,2,3,4,5,6]
list.pop()
print(list)

list = [1,2,3,4,5,6]
list.reverse()
print(list)

list1 = [1,2,3,4,5,6]
list2 = [7,8,9]
list1.extend(list2)
print(list1)

string = "Hello"
print(string[1:3])

list = [1,2,3]
repeat = list * 3
print(repeat)

str = "python"
print(str[-8:5])


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

