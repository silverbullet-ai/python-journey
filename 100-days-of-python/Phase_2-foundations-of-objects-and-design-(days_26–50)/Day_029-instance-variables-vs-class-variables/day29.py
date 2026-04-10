# Day 29 — Instance vs Class Variables

print("INSTANCE vs CLASS VARIABLES PRACTICE\n")

class Student:
    college = "ABC University"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

# Create instances
s1 = Student("Aahish")
s2 = Student("Rahul")

print("Student 1:", s1.name, "-", s1.college)
print("Student 2:", s2.name, "-", s2.college)

print("\n------------------\n")

# Modify instance variable
s1.name = "Aahish Kumar"
print("Updated Student 1 name:", s1.name)

# Modify class variable via class
Student.college = "XYZ University"

print("\nAfter updating class variable:")
print("Student 1:", s1.college)
print("Student 2:", s2.college)

print("\n------------------\n")

# Shadowing class variable
s2.college = "Private College"

print("After shadowing:")
print("Student 2 college:", s2.college)
print("Student 1 college:", s1.college)
print("Class college:", Student.college)

print("\nDay 29 completed successfully!")