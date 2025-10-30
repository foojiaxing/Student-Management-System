# Math Quiz

import random

def ask_question(question, correct_answer):
    while True:
        try:
            answer = int(input(question))
            return answer == correct_answer
        except ValueError:
            print("Please enter a valid number.")
def quiz():
    score = 0

    print("Answer the following questions:")

    for _ in range(4):
        num1, num2 = random.randint(-10, 100), random.randint(-10, 100)

        # Randomly choose the operation
        operation = random.choice(['+', '*', '-', '//', '^2'])

        if operation == '+':
            question = f"What is {num1} + {num2}? "
            correct_answer = num1 + num2
        elif operation == '*':
            question = f"What is {num1} * {num2}? "
            correct_answer = num1 * num2
        elif operation == '-':
            question = f"What is {num2} - {num1}? "
            correct_answer = num2 - num1
        elif operation == '//':
            if num1 == 0:
                num1 += 1  # Avoid division by zero
            question = f"What is {num2} // {num1} ? "
            correct_answer = num2 // num1

        if ask_question(question, correct_answer):
            score += 1

    # Display the final score
    print(f"You got {score} out of 5 correct!")


# Run the quiz
quiz()

import random
score = 0
question_count = 0

while question_count < 5:
    num1, num2 = random.randint(-10, 100), random.randint(-10, 100)

    # Randomly choose the operation
    operation = random.choice(['+', '*', '-', '//', '^2'])

    if operation == '+':
        question = f"What is {num1} + {num2}? "
        correct_answer = num1 + num2
    elif operation == '*':
        question = f"What is {num1} * {num2}? "
        correct_answer = num1 * num2
    elif operation == '-':
        question = f"What is {num2} - {num1}? "
        correct_answer = num2 - num1
    elif operation == '//':
        if num1 == 0:
            num1 += 1  # Avoid division by zero
        question = f"What is {num2} // {num1} ? "
        correct_answer = num2 // num1

    # Display the final score
print(f"You got {score} out of 5 correct!")

