# Day 27 — Classes & Instances

print("CLASSES & INSTANCES PRACTICE\n")

# Define a class (blueprint)
class Student:
    pass

# Create instances (real objects)
student1 = Student()
student2 = Student()

print("Student 1:", student1)
print("Student 2:", student2)

print("Same object?", student1 is student2)

print("\n------------------\n")

# Another example
class Laptop:
    pass

lap1 = Laptop()
lap2 = Laptop()

print("Laptop 1 ID:", id(lap1))
print("Laptop 2 ID:", id(lap2))

print("\nDay 27 practice completed successfully!")