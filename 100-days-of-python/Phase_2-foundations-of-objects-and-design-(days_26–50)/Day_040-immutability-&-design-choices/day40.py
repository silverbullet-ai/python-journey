# Day 40 — Immutability & Design Choices

print("IMMUTABILITY PRACTICE\n")

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(2, 3)
print("Point:", p1)

# Uncommenting below will raise an error
# p1.x = 5

print("\nCreating a new modified point")
p2 = Point(p1.x + 1, p1.y + 1)
print("New Point:", p2)

print("\nDay 40 completed successfully!")
