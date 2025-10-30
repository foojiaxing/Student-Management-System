# Allows the program to save and load students data in a JSON file name and format
import json

# An empty dictionary to store student records
students = {}


# Add student details (ID, name, age, course, GPA)
# Ensure GPA & age within reasonable ranges
# Prevent incorrect inputs (e.g., non-numeric values for age & GPA)

# 2.1 Add Student Function
def add_student():
    while True:  # Loop until a valid student id is entered
        # Input student ID
        while True:
            student_id = input("Enter student ID: ").replace(" ", "")
            if not student_id.isdigit():
                print("Invalid student ID. Please enter only numbers.")
            elif student_id in students:
                print("Student ID already exists. Please enter a unique ID.")
            else:
                break  # Exit the loop once is valid

        # Input student name
        while True:  # Loop until a valid name is entered
            student_name = input("Enter student name: ").replace(" ", "")
            if not student_name.isalpha():
                print("Invalid student name. Please enter only alphabets.")
            else:
                break  # Exit the loop once is valid

        # Input student age
        while True:  # Loop until a valid age is entered
            student_age = input("Enter student age: ").replace(" ", "")
            if not student_age.isdigit():
                print("Invalid student age. Please enter only numbers.")
            elif not (1 <= int(student_age) <= 100):
                print(f"Invalid student age. Student age must be between 1 and 100.")
            else:
                break  # Exit the loop once is valid

        # Input student course
        while True:  # Loop until a valid age is entered
            student_course = input("Enter student course: ").replace(" ", "")
            if not student_course.isalpha():
                print("Invalid student course. Please enter only alphabets.")
            else:
                break  # Exit the loop once is valid

        # Input student GPA
        while True:  # Loop until a valid GPA is entered
            student_gpa = input("Enter student GPA (0.00 - 4.00): ").replace(" ", "")
            try:
                student_gpa = float(student_gpa)
                if not (0.00 <= student_gpa <= 4.00):
                    print("Invalid student GPA. Student GPA must be between 0.00 and 4.00.")
                else:
                    break  # Exit the loop once is valid
            except ValueError:
                print("Invalid student GPA. Please enter only numbers.")

        # Store the student's details in the dictionary
        students[student_id] = {
            "id": student_id,
            "Name": student_name,
            "Age": int(student_age),
            "Course": student_course,
            "GPA": student_gpa
        }
        print("Student added successfully!")
        break


# Update student details based on their ID (except ID)
# Check if the student ID exists before updating
# Provide options to update only 1 field at a time instead of all details at once

# 2.2 Update Student Function
def update_student():
    while True:  # Loop until a valid student id is entered
        student_id = input("Enter student ID to update: ").replace(" ", "")
        if student_id in students:
            break    # Exit loop if the ID is valid
        print("Invalid. Student ID not found. Please try again.")

    print("Select field from number 1 to 4 to update:")
    print("\n1. Update Name")
    print("2. Update Age")
    print("3. Update Course")
    print("4. Update GPA")

    while True:  # Loop until a valid choice is entered
        option = input("Choose an option to update: ").replace(" ", "")
        if option in ["1", "2", "3", "4"]:
            print(f"Your choice is {option}.")
            break  # Exit the loop once is valid
        else:
            print("Invalid. Please enter a number between 1 to 4.")

    if option == "1":
        while True:  # Loop until a valid name is entered
            new_name = input("Enter new name: ").replace(" ", "")
            if not new_name.isalpha():
                print("Invalid student name. Please enter only alphabets.")
            else:
                students[student_id]["Name"] = new_name
                print("Student record updated successfully!")
                break  # Exit the loop once is valid

    elif option == "2":
        while True:  # Loop until a valid age is entered
            new_age = input("Enter new age: ").replace(" ", "")
            if not new_age.isdigit():
                print("Invalid student age. Please enter only numbers.")
            elif not (1 <= int(new_age) <= 100):
                print("Invalid student age. Student age must be between 1 and 100.")
            else:
                students[student_id]["Age"] = int(new_age)
                print("Student record updated successfully!")
                break  # Exit the loop once is valid

    elif option == "3":
        while True:  # Loop until a valid course is entered
            new_course = input("Enter new course: ").replace(" ", "")
            if not new_course.isalpha():
                print("Invalid student course. Please enter only alphabets.")
            else:
                students[student_id]["Course"] = new_course
                print("Student record updated successfully!")
                break  # Exit the loop once is valid

    elif option == "4":
        while True:  # Loop until a valid gpa is entered
            new_gpa = input("Enter new GPA (0.00 - 4.00): ").replace(" ", "")
            try:
                new_gpa = float(new_gpa)
                if not (0.00 <= new_gpa <= 4.00):
                    print("Invalid student GPA. Student GPA must be between 0.00 and 4.00.")
                else:
                    students[student_id]["GPA"] = new_gpa
                    print("Student record updated successfully!")
                    break  # Exit the loop once is valid
            except ValueError:
                print("Invalid student GPA. Please enter only numbers.")


# 2.3 Delete Student Function
def delete_student():
    while True:
        # Asks user to enter the Student ID they want to delete
        student_id = input("Enter Student ID to delete: ").replace(" ", "")
        if student_id in students:
            break    # Exit loop if the ID is valid
        else:
            print("Invalid. Student ID not found.")

    # Confirmation Prompt (asking yes/no to confirm deletion)
    confirmation = input(f"Delete {students[student_id]['Name']}? (yes/no): ").replace(" ", "")
    if confirmation.lower() == "yes":
        del students[student_id]  # Remove student record from the dictionary
        print("Valid. Student record deleted successfully!")
    else:
        print("Invalid. Deletion cancelled.")
        return  # If invalid, continue asking the user for input until it is valid


# 2.4 View All Student Records
def view_student():
    if not students:  # If the students dictionary is empty
        print("Invalid. No student records found.")
        return  # If invalid, continue asking the user for input until it is valid

    # Column headers (id,name,course,gpa) aligned with specific spacing
    print(f"{'ID':<10} {'Name':<20} {'Age':<5} {'Course':<10} {'GPA':<5}")
    print("-" * 50)  # Print a line of dashes as a seperator under the header
    # Go through each student in the students' dictionary
    for student_id, student in students.items():  # Student id is the key, student will represent the student's details
        print(
            f"{student['id']:<10} {student['Name']:<20} {student['Age']:<5} {student['Course']:<10} {student['GPA']:<5}")


# 2.5 Save and Load Data
def save_records():  # Saves the students list into student.json file
    # Open file(students.json) in write mode("w")- create the file if it doesn't exit or overwriting if it does.
    with open("students.json", "w") as file:
        # json.dump() function will take the student list and save it into students.json file
        json.dump(students, file)
    print("Records saved successfully.")


def load_records():  # Retrieve and shows the latest data as it was last saved
    global students  # Tells Python to use global "students" list
    try:  # Tries to open the file and read its data
        with open("students.json", "r") as file:  # Open the "students.json" file in read mode ("r")
            students = json.load(file)  # Load the content of the file in JSON format into global "students" list
        print("Valid. Records loaded successfully.")
    except FileNotFoundError:  # Try block will jump to except block if the file is not found
        print("Invalid. No saved records found")


# 2.6 Search Functionality (Optional)
def search_student():
    print("Search by (ID/Name/Course).")
    # Asking user to choose a field
    search_field = input("Enter search field (ID/Name/Course): ").replace(" ", "").lower()

    # Checks if the user entered the valid options: id, name, course
    if search_field not in ['id', 'name', 'course']:
        print("Invalid search field. Please enter 'ID', 'Name', or 'Course'.")
        return  # If invalid, continue asking the user for input until it is valid

    # Ask the user to enter what value they want to search for
    query = input("Enter search query: ").replace(" ", "").lower()

    # Initialize the results
    result = []

    #
    for student_id, info in students.items():
        # Check matching records
        if (search_field == "id" and query == student_id) or \
                (search_field == "name" and query in info["Name"].replace(" ", "").lower()) or \
                (search_field == "course" and query in info["Course"].replace(" ", "").lower()):
            result.append((student_id, info))  # Add matching records to the result list

    # Check whether the results are in the student records or not
    if result:
        print("{:<10} {:<20} {:<10} {:<15} {:<5}".format("ID", "Name", "Age", "Course", "GPA"))
        for student_id, info in result:
            print("{:<10} {:<20} {:<10} {:<15} {:<5}".format(
                student_id, info["Name"], info["Age"], info["Course"], info["GPA"]))
    else:
        print("Invalid. No matching records found.")


# Main Menu
def main_menu():
    load_records()  # Load records on startup

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Save Records")
        print("6. Load Records")
        print("7. Search Student")
        print("8. Exit")
        option = input("Enter your choice: ").replace(" ", "")

        if option == "1":
            add_student()
        elif option == "2":
            update_student()
        elif option == "3":
            delete_student()
        elif option == "4":
            view_student()
        elif option == "5":
            save_records()
        elif option == "6":
            load_records()
        elif option == "7":
            search_student()
        elif option == "8":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# Run the main menu
main_menu()
