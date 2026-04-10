# Day 25 - Phase 1 Final Mini Project
# Student Record Manager (CLI)

students = {}

def add_student():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        marks_input = input("Enter marks separated by space: ")
        marks = [int(m) for m in marks_input.split()]

        students[name] = marks
        print("Student added successfully.\n")
    except ValueError:
        print("Invalid marks. Please enter integers only.\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return

    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {avg:.2f}\n")

def menu():
    print("STUDENT RECORD MANAGER")
    print("1. Add student")
    print("2. Display students")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
