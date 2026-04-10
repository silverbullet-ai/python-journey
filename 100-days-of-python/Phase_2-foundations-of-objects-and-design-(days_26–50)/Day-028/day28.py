# Day 28 — Constructors & self

print("CONSTRUCTORS & SELF PRACTICE\n")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating instances
student1 = Student("Aahish", 21)
student2 = Student("Rahul", 20)

student1.show_details()
print("------------------")
student2.show_details()

print("\nStudent 1 dict:", student1.__dict__)
print("Student 2 dict:", student2.__dict__)

print("\nDay 28 completed successfully!")