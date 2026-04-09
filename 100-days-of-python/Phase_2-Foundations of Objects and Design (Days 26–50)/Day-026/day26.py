
# Day 26 — Python Object Model

print("PYTHON OBJECT MODEL PRACTICE\n")

# Identity, Type, Value
x = 42
print("Value:", x)
print("Type:", type(x))
print("ID:", id(x))

print("\n------------------\n")

# Reference behavior with mutable objects
a = [1, 2, 3]
b = a
b.append(4)

print("List a:", a)
print("List b:", b)
print("Same object?", id(a) == id(b))

print("\n------------------\n")

# Immutable object behavior
num = 10
print("Before:", num, id(num))
num += 5
print("After:", num, id(num))

print("\n------------------\n")

# Function as object
def square(n):
    return n * n

func_list = [square]
print("Function result from list:", func_list)

print("\nDay 26 completed successfully!")
