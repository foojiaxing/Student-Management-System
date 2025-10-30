# Allows the program to save and load students data in a JSON file name and format
import json

# An empty dictionary to store student records
students = {}

# Add student details (ID, name, age, course, GPA)
# Ensure GPA & age within reasonable ranges
# Prevent incorrect inputs (e.g., non-numeric values for age & GPA)

# 2.1 Add Student Function
def add_student():
    while True:
        # Input student ID
        while True:  # Loop until a valid student id is entered
            student_id = (input("Enter student ID (or type '*' to return to main menu): ")
                          .replace(" ", ""))
            if student_id == "*":  # Escape condition
                print("Returning to the main menu...")
                return
            if not student_id.isdigit():
                print("Invalid student ID. Please enter only numbers.")
            elif student_id in students:
                print("Student ID already exists. Please enter a unique ID.")
            else:
                break  # Exit the loop once it is valid

        # Input student name
        while True:  # Loop until a valid name is entered
            student_name = (input("Enter student name: ").title().replace(" ", ""))
            if not student_name.isalpha():
                print("Invalid student name. Please enter only alphabets.")
            else:
                break  # Exit the loop once it is valid

        # Input student age
        while True:  # Loop until a valid age is entered
            student_age = (input("Enter student age: ").replace(" ", ""))
            if not student_age.isdigit():
                print("Invalid student age. Please enter only numbers.")
            elif not (1 <= int(student_age) <= 100):
                print("Invalid student age. Student age must be between 1 and 100.")
            else:
                break  # Exit the loop once it is valid

        # Input student course
        while True:  # Loop until a valid course is entered
            student_course = (input("Enter student course: ").title().replace(" ", ""))
            if not student_course.isalpha():
                print("Invalid student course. Please enter only alphabets.")
            else:
                break  # Exit the loop once it is valid

        # Input student GPA
        while True:  # Loop until a valid GPA is entered
            student_gpa = (input("Enter student GPA (0.00 - 4.00): ").replace(" ", ""))
            try:
                student_gpa = float(student_gpa)
                if not (0.00 <= student_gpa <= 4.00):
                    print("Invalid student GPA. Student GPA must be between 0.00 and 4.00.")
                else:
                    break  # Exit the loop once it is valid
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
        print("Returning to the main menu...")
        break


# Update student details based on their ID (except ID)
# Check if the student ID exists before updating
# Provide options to update only 1 field at a time instead of all details at once

# 2.2 Update Student Function
def update_student():
    if not students:
        print("Invalid. No student records found.")  # Check if the students' dictionary is empty
        return  # Exit the function

    while True:  # Loop until a valid student id is entered
        student_id = (input("Enter student ID to update (or type '*' to return to main menu): ")
                      .replace(" ", ""))
        if student_id == "*":  # Escape condition
            print("Returning to the main menu...")
            return
        if student_id in students:
            break    # Exit loop if the ID is valid
        print("Invalid. Student ID not found. Please try again.")

    print("Select from number 1 to 4 to update:")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Course")
    print("4. Update GPA")

    while True:  # Loop until a valid choice is entered
        option = input("Choose an option to update: ").replace(" ", "")
        if option in ["1", "2", "3", "4"]:
            print(f"Your choice is {option}.")
            break  # Exit the loop once it is valid
        else:
            print("Invalid. Please enter a number between 1 to 4.")

    # Update name
    if option == "1":
        while True:  # Loop until a valid name is entered
            new_name = input("Enter new name: ").title().replace(" ", "")
            if not new_name.isalpha():
                print("Invalid student name. Please enter only alphabets.")
            else:
                students[student_id]["Name"] = new_name
                print("Student record updated successfully!")
                print("Returning to the main menu...")
                break  # Exit the loop once it is valid

    # Update age
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
                print("Returning to the main menu...")
                break  # Exit the loop once it is valid

    # Update course
    elif option == "3":
        while True:  # Loop until a valid course is entered
            new_course = input("Enter new course: ").title().replace(" ", "")
            if not new_course.isalpha():
                print("Invalid student course. Please enter only alphabets.")
            else:
                students[student_id]["Course"] = new_course
                print("Student record updated successfully!")
                print("Returning to the main menu...")
                break  # Exit the loop once it is valid

    # Update gpa
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
                    print("Returning to the main menu...")
                    break  # Exit the loop once it is valid
            except ValueError:
                print("Invalid student GPA. Please enter only numbers.")


# 2.3 Delete Student Function
def delete_student():
    if not students:
        print("Invalid. No student records found.")  # Check if the students' dictionary is empty
        return  # Exit the function

    # Asks user to enter the Student ID they want to delete
    while True:
        student_id = (input("Enter student ID to delete (or type '*' to return to main menu): ")
                      .replace(" ", ""))
        if student_id == "*":  # Escape condition
            print("Returning to the main menu...")
            return
        if student_id in students:
            break    # Exit loop if the ID is valid
        else:
            print("Invalid. Student ID not found.")

    # Confirmation Prompt (asking yes/no to confirm deletion)
    while True:
        confirmation = input(f"Delete {students[student_id]['Name']}? (yes/no): ").replace(" ", "")
        if confirmation.lower() == "yes":
            del students[student_id]  # Remove student record from the dictionary
            print("Student record deleted successfully!")
            print("Returning to the main menu...")
            break
        elif confirmation.lower() == "no":
            print("Deletion cancelled.")
            print("Returning to the main menu...")
            break
        else:
            print("Invalid input. Please enter yes/no.")   # If invalid, continue asking the user to input until valid


# 2.4 View All Student Records
def view_students():
    if not students:
        print("Invalid. No student records found.")  # Check if the students' dictionary is empty
        return  # Exit the function

    # Column headers (id,name,course,gpa) aligned with specific spacing
    print(f"\n{'ID':<15} {'Name':<20} {'Age':<5} {'Course':<40} {'GPA':<5}")
    print("-" * 90)    # Print a horizontal line of dashes as a separator under the header
    # Go through each student in the students' dictionary
    for student_id, student in students.items():
        # Student id is the key, so student will represent the student's details
        print(f"{student['id']:<15} {student['Name']:<20} {student['Age']:<5} "
              f"{student['Course']:<40} {student['GPA']:<5}")
    print()
    print("Returning to the main menu...")


# 2.5 Save and Load Data
# Save student records
def save_records():  # Save the students' records into student.json file
    # Open file(students.json) in write mode("w")- create the file if it doesn't exit or overwriting if it does
    with open("students.json", "w") as file:
        # json.dump() function will take the student list and save it into students.json file
        json.dump(students, file)
    print("Records saved successfully.")
    print("Returning to the main menu...")

# Load student records
def load_records():  # Retrieve and show the latest data as it was last saved
    global students  # Tell Python to use global "students" list
    try:  # Try to open the file and read its data
        with open("students.json", "r") as file:  # Open the "students.json" file in read mode ("r")
            students = json.load(file)  # Load the content of the file in JSON format into global "students" list
        print("Records loaded successfully.")
        print("Returning to the main menu...")
    except FileNotFoundError:  # "Try" block will jump to "except" block if the file is not found
        print("Invalid. No saved records found.")


# 2.6 Search Functionality (Optional)
# Search for students by student id, name or course
def search_student():
    if not students:
        print("Invalid. No student records found.")  # Check if the students' dictionary is empty
        return  # Exit the function

    # Ask user to choose a field
    print("Search by:")
    print("1. ID")
    print("2. Name")
    print("3. Course")

    while True:  # Loop until a valid choice is entered
        option = (input("Choose an option to search (or type '*' to return to main menu): ")
                  .replace(" ", ""))
        if option == "*":  # Escape condition
            print("Returning to the main menu...")
            return
        if option in ["1", "2", "3"]:
            print(f"Your choice is {option}.")
            break  # Exit the loop once it is valid
        else:
            print("Invalid. Please enter a number between 1 to 3.")

    # Search by ID
    if option == "1":
        while True:  # Loop until a valid name is entered
            result = [] # Reset the result list for each new search
            search_id = input("Enter ID: ").replace(" ", "")
            if not search_id.isdigit():
                print("Invalid student ID. Please enter only numbers.")
            else:
                # Search for matching records
                for student_id, info in students.items():
                    # Check matching records
                    if search_id in student_id.replace(" ", ""): # Allow partial matching for student ID
                        result.append((student_id, info))  # Add matching records to the result list

                # Check whether the results are in the student records or not
                if result:
                    print("\nMatching Student Records:")
                    print("{:<15} {:<20} {:<5} {:<40} {:<5}".format("ID", "Name", "Age", "Course", "GPA"))
                    print("-" * 90)  # Print a horizontal line of dashes as a separator under the header
                    for student_id, info in result:
                        print("{:<15} {:<20} {:<5} {:<40} {:<5}".format(
                            student_id, info["Name"], info["Age"], info["Course"], info["GPA"]))
                    print()
                    print("Returning to the main menu...")
                    return

                else:
                    print("No matching records found. Please try again.")

    # Search by name
    if option == "2":
        while True:  # Loop until a valid name is entered
            result = []  # Reset the result list for each new search
            search_name = input("Enter name: ").replace(" ", "").lower()
            if not search_name.isalpha():
                print("Invalid student name. Please enter only alphabets.")
            else:
                # Search for matching records
                for student_id, info in students.items():
                    # Check matching records
                    if search_name in info["Name"].replace(" ", "").lower(): # Allow partial matching for name
                        result.append((student_id, info))  # Add matching records to the result list

                # Check whether the results are in the student records or not
                if result:
                    print("\nMatching Student Records:")
                    print("{:<15} {:<20} {:<5} {:<40} {:<5}".format("ID", "Name", "Age", "Course", "GPA"))
                    print("-" * 90)  # Print a horizontal line of dashes as a separator under the header
                    for student_id, info in result:
                        print("{:<15} {:<20} {:<5} {:<40} {:<5}".format(
                            student_id, info["Name"], info["Age"], info["Course"], info["GPA"]))
                    print()
                    print("Returning to the main menu...")
                    return

                else:
                    print("No matching records found. Please try again.")

    # Search by course
    if option == "3":
        while True:  # Loop until a valid name is entered
            result = []  # Reset the result list for each new search
            search_course = input("Enter course: ").replace(" ", "").lower()
            if not search_course.isalpha():
                print("Invalid student course. Please enter only alphabets.")
            else:
                # Search for matching records
                for student_id, info in students.items():
                    # Check matching records
                    if search_course in info["Course"].replace(" ", "").lower(): # Allow partial matching for course
                        result.append((student_id, info))  # Add matching records to the result list

                # Check whether the results are in the student records or not
                if result:
                    print("\nMatching Student Records:")
                    print("{:<15} {:<20} {:<5} {:<40} {:<5}".format("ID", "Name", "Age", "Course", "GPA"))
                    print("-" * 90)  # Print a horizontal line of dashes as a separator under the header
                    for student_id, info in result:
                        print("{:<15} {:<20} {:<5} {:<40} {:<5}".format(
                            student_id, info["Name"], info["Age"], info["Course"], info["GPA"]))
                    print()
                    print("Returning to the main menu...")
                    return

                else:
                    print("No matching records found. Please try again.")


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
            view_students()
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
