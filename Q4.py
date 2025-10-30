import tkinter as tk
from tkinter import messagebox


class EnrollmentSystem:
    def __init__(self, window):
        self.view_button = None
        self.search_by_id_button = None
        self.student_listbox = None
        self.search_button = None
        self.delete_button = None
        self.id_entry = None
        self.add_button = None
        self.id_label = None
        self.validate_alpha = None
        self.course_entry = None
        self.name_label = None
        self.name_entry = None
        self.validate_course_alpha = None
        self.course_label = None
        self.root = window
        self.root.title("UCSI University Enrollment System")
        self.courses = {}
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for course and student information
        self.course_label = tk.Label(self.root, text="Course Name:")
        self.course_label.grid(row=0, column=0, padx=10, pady=10)
        self.validate_course_alpha = self.root.register(self.on_validate_course_alpha)
        self.course_entry = tk.Entry(self.root, validate="key", validatecommand=(self.validate_course_alpha, "%P"))
        self.course_entry.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        # Validate function that will take in only alphabets
        self.validate_alpha = self.root.register(self.on_validate_alpha)
        self.name_entry = tk.Entry(self.root, validate="key", validatecommand=(self.validate_alpha, "%P"))
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.id_label = tk.Label(self.root, text="Student ID:")
        self.id_label.grid(row=2, column=0, padx=10, pady=10)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=2, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Admission", command=self.add_admission)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search Student", command=self.search_student)
        self.search_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.root, text="View Students", command=self.view_students)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.search_by_id_button = tk.Button(self.root, text="Search by ID", command=self.search_by_id)
        self.search_by_id_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.student_listbox = tk.Listbox(self.root, width=50, height=10)
        self.student_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def on_validate_alpha(self, new_value):
        # Check if the new value is all alphabetic characters only
        if new_value.isalpha() or new_value == "":
            return True
        else:
            messagebox.showwarning("Invalid Input", "Please enter alphabetic characters only.")
            return False

    def on_validate_course_alpha(self, new_value):
        # Check if the new value is all alphabetic characters only
        if new_value.isalpha() or new_value == "":
            return True
        else:
            messagebox.showwarning("Invalid Input", "Please enter alphabetic characters only.")
            return False

    def add_admission(self):
        course = self.course_entry.get()
        name = self.name_entry.get()
        student_id = self.id_entry.get()

        if course and name and student_id:
            student = (name, student_id)
            if course in self.courses:
                self.courses[course].append(student)
            else:
                self.courses[course] = [student]
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showerror("Error", "Please fill all fields")

    def delete_student(self):
        course = self.course_entry.get()
        name = self.name_entry.get()

        if course and name:
            if course in self.courses:
                students = self.courses[course]
                for student in students:
                    if student[0] == name:
                        students.remove(student)
                        messagebox. showinfo("Success", "Student removed successfully!")
                        return
                messagebox.showerror("Error", "Student not found in the course.")
            else:
                messagebox.showerror("Error", "Course not found.")
        else:
            messagebox.showerror("Error", "Please fill both course and student name fields.")

    def search_student(self):
        name = self.name_entry.get()
        if name:
            result = []
            for course, students in self.courses.items():
                for student in students:
                    if student[0] == name:
                        result.append(f"Course: {course}, ID: {student[1]}")
            if result:
                messagebox.showinfo("Search Result", "\n".join(result))
            else:
                messagebox.showinfo("Search Result", "Student not found.")
        else:
            messagebox.showerror("Error", "Please enter a student name.")

    def view_students(self):
        course = self.course_entry.get()
        self.student_listbox.delete(0, tk.END)
        if course:
            if course in self.courses:
                students = self.courses[course]
                for student in students:
                    self.student_listbox.insert(tk.END, f"Name: {student[0]}, ID: {student[1]}")
            else:
                messagebox.showerror("Error", "Course not found.")
        else:
            # Show all students if course is not entered
            for course, students in self.courses.items():
                for student in students:
                    self.student_listbox.insert(tk.END, f"Course: {course}, Name: {student[0]}, ID: {student[1]}")

    def search_by_id(self):
        student_id = self.id_entry.get()
        if student_id:
            result = []
            for course, students in self.courses.items():
                for student in students:
                    if student[1] == student_id:
                        result.append(f"Course: {course}, Name: {student[0]}")
            if result:
                messagebox.showinfo("Search Result", "\n".join(result))
            else:
                messagebox.showinfo("Search Result", "Student not found.")
        else:
            messagebox.showerror("Error", "Please enter a student ID.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EnrollmentSystem(root)
    root.mainloop()
