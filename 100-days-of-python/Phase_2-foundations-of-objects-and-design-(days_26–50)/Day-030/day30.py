# Day 30 — Methods & Behavior Modeling

print("METHODS & BEHAVIOR PRACTICE\n")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def is_passed(self):
        return self.marks >= 40

# Create instances
s1 = Student("Aahish", 85)
s2 = Student("Rahul", 32)

s1.display()
print("Passed?", s1.is_passed())

print("\n------------------\n")

s2.display()
print("Passed?", s2.is_passed())

print("\nDay 30 completed successfully!")