# Function to get student details
def get_student_details():
    name = input("Enter student name: ")
    marks = float(input("Enter marks (0–100): "))
    return name, marks

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Function to check pass/fail
def check_pass_fail(marks):
    if marks >= 35:
        return "PASS"
    else:
        return "FAIL"

# Function to display a single student's result
def display_result(name, marks, grade, status):
    print("\n--- Student Result ---")
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Status:", status)

# Function to add multiple students
def add_students(students):
    n = int(input("How many students do you want to add? "))
    for i in range(n):
        print(f"\nEntering details for student {i+1}:")
        name, marks = get_student_details()
        grade = calculate_grade(marks)
        status = check_pass_fail(marks)
        students.append({"name": name, "marks": marks, "grade": grade, "status": status})
    print(f"\n{n} student(s) added successfully!")

# Function to show all students
def show_students_results(students):
    if not students:
        print("No students added yet!")
    else:
        print("\n====== All Students Results ======")
        for student in students:
            display_result(student["name"], student["marks"], student["grade"], student["status"])

# ----- Main Program -----
students_list = []

while True:
    print("\n--- Menu ---")
    print("1. Add Students")
    print("2. Show Student Results")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_students(students_list)
    elif choice == "2":
        show_students_results(students_list)
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")

