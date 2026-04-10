# Day 14 - Tuples (Immutable Sequences)

# Creating tuples
numbers = (10, 20, 30, 40)
single_value = (5,)

print("Numbers tuple:", numbers)
print("Single value tuple:", single_value)

print()

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

print()

# Slicing
print("Slice [1:3]:", numbers[1:3])
print("Reverse tuple:", numbers[::-1])

print()

# Iterating over tuple
print("Iterating over tuple:")
for num in numbers:
    print(num)

print()

# Immutability demonstration
# numbers[1] = 25  # Uncommenting this will cause an error

print("Tuples cannot be modified after creation.")

print("\nDay 14 completed successfully!")
