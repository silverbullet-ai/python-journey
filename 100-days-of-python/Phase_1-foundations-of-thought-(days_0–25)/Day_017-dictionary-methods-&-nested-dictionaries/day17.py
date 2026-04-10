# Day 17 - Dictionary Methods & Nested Dictionaries

# Dictionary methods
student = {
    "name": "Aahish",
    "age": 23,
    "course": "Python"
}

print("Name:", student.get("name"))
print("Grade:", student.get("grade", "Not Assigned"))

print()

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print()

# Updating dictionary
extra_info = {"city": "Jaipur", "year": 2026}
student.update(extra_info)
print("After update:", student)

print()

# Nested dictionary
students = {
    "Aahish": {"age": 23, "course": "Python"},
    "Swati": {"age": 22, "course": "C++"},
    "Manav": {"age": 22, "course": "Java"}
}

print("\nSTUDENT DATA")
for name, info in students.items():
    print("\nName:", name)
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nDay 17 completed successfully!")
