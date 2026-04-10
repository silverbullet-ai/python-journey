# Day 37 — __str__, __repr__ & Comparisons

print("STR, REPR & COMPARISONS PRACTICE\n")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Aahish", 85)
s2 = Student("Rahul", 92)
s3 = Student("Someone", 85)

print(s1)
print(repr(s2))

print("\nEquality check:")
print(s1 == s3)

print("\nSorting students:")
students = [s1, s2, s3]
students.sort()

for s in students:
    print(s)

print("\nDay 37 completed successfully!")
