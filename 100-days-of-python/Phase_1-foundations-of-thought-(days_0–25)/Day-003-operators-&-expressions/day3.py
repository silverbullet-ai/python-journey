# Day 3 - Operators and Expressions

# Arithmetic operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print()

# Assignment operators
x = 5
x += 2
print("x after += 2:", x)

x *= 3
print("x after *= 3:", x)

print()

# Comparison operators
age = 20
print("Age > 18:", age > 18)
print("Age == 18:", age == 18)
print("Age != 18:", age != 18)

print()

# Logical operators
is_student = True
has_id = False

print("Eligible:",
      age > 18 and is_student)

print("Can enter:",
      has_id or is_student)

print("Not a student:",
      not is_student)

print()

# Operator precedence
result = 10 + 2 * 5
result_with_brackets = (10 + 2) * 5

print("Without brackets:", result)
print("With brackets:", result_with_brackets)


print("\nDay 3 completed successfully!")

