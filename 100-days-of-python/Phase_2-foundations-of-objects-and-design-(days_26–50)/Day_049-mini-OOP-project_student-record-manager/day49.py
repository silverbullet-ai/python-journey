# Day 49 — Mini OOP Project: Student Record Manager

print("STUDENT RECORD MANAGER (OOP)\n")

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student.student_id] = student

    def get_student(self, student_id):
        if student_id not in self.students:
            raise KeyError("Student not found")
        return self.students[student_id]

    def display_all(self):
        if not self.students:
            print("No students available")
        for student in self.students.values():
            student.display()

# Demo usage
manager = StudentManager()

try:
    manager.add_student(Student(1, "Aahish", 88))
    manager.add_student(Student(2, "Rahul", 76))
except ValueError as e:
    print("Error:", e)

print("\nAll Students:")
manager.display_all()

print("\nSearching student with ID 1:")
try:
    student = manager.get_student(1)
    student.display()
except KeyError as e:
    print("Error:", e)

print("\nDay 49 completed successfully!")