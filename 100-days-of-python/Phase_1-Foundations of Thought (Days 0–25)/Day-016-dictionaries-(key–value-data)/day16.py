# Day 16 - Dictionaries (Key–Value Data)

# Creating a dictionary
student = {
    "name": "Aahish",
    "age": 22,
    "course": "Python"
}

print("Student dictionary:", student)

print()

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

print()

# Adding a new key-value pair
student["city"] = "Gaya"
print("After adding city:", student)

print()

# Updating an existing value
student["age"] = 23
print("After updating age:", student)

print()

# Removing a key-value pair
removed_course = student.pop("course")
print("Removed course:", removed_course)
print("After removal:", student)

print()

# Iterating over dictionary
print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

print("\nDay 16 completed successfully!")
