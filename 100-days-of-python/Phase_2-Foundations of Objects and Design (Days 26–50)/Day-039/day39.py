# Day 39 — Dataclasses

print("DATACLASSES PRACTICE\n")

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

    def is_passed(self):
        return self.marks >= 40

s1 = Student("Aahish", 85)
s2 = Student("Rahul", 35)

print(s1)
print("Passed?", s1.is_passed())

print(s2)
print("Passed?", s2.is_passed())

print("\nEquality check:")
print(s1 == s2)

print("\nDay 39 completed successfully!")
