import random

score = 0
number_of_questions = 5

while number_of_questions > 0:
    num1, num2 = random.randint(-10, 20), random.randint(-10, 50)

    # Given question
    print(f"What is {num1} + {num2} ?")

    # If characters and decimals and symbols - print out enter a valid number
    while True:
        try:
            answer = int(input("Enter your answer: "))
            break
        except ValueError:
            print("Please enter a valid number")

    # Check whether the user answer is it correct?
    if answer == num1 + num2:
        print("You got correct")
        score += 1
    else:
        print(f"You got wrong, correct answer is {num1 + num2}")

    # Deduct one from the given question
    number_of_questions -= 1

# Display the results
print(f"Your score is {score} out of 5!")
