# Day 15 - Sets (Unique Collections)

# Creating sets
numbers = {1, 2, 3, 4, 4, 5}
print("Numbers set:", numbers)

print()

# Adding elements
numbers.add(6)
print("After add:", numbers)

print()

# Removing elements
numbers.remove(3)
print("After remove 3:", numbers)

numbers.discard(10)  # no error
print("After discard 10:", numbers)

print()

# Membership testing
print("Is 2 in set?", 2 in numbers)
print("Is 10 in set?", 10 in numbers)

print()

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A - B:", A - B)
print("Difference B - A:", B - A)

print("\nDay 15 completed successfully!")
