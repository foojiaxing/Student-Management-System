import random

# Initialize variables
score = 0
number_of_questions = 5

# The loop will continue running as long as the number of questions greater than 0
while number_of_questions > 0:
    num1, num2 = random.randint(-10, 20), random.randint(-10, 20)

    # Given question
    print(f"What is {num1} + {num2} ?")

    # Test the value of the input, if there is a value error (characters and decimals and symbols)
    # then display a message to the user to enter a valid number
    while True:
        try:
            answer = int(input("Enter your answer: "))
            break
        except ValueError:
            print("Please enter a valid number")

    # Check whether the answer is it correct?
    if answer == num1 + num2:
        score += 1

    # Deduct one from the given question
    number_of_questions -= 1

# Results
print(f"Your score is {score} out of 5!")
