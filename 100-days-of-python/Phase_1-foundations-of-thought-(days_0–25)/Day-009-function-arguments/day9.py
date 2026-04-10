# Day 9 - Function Arguments

# Positional arguments
def multiply(a, b):
    return a * b

print("Multiply:", multiply(3, 4))

print()

# Default arguments
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Aahish")

print()

# Keyword arguments
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(name="Aahish", age=21, course="Python")

print()

# Mixing positional and keyword arguments
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(5))
print("Power:", power(5, exponent=3))



print("\nDay 9 completed successfully!")
