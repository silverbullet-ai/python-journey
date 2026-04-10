# Day 11 - Lists (Introduction)

# Creating lists
numbers = [10, 20, 30, 40]
names = ["Aahish", "Python", "Learner"]

print("Numbers list:", numbers)
print("Names list:", names)

print()

# Indexing
print("First number:", numbers[0])
print("Last number:", numbers[-1])

print()

# Modifying list elements
numbers[1] = 25
print("Modified numbers list:", numbers)

print()

# Iterating over a list
print("Iterating over numbers:")
for num in numbers:
    print(num)

print()

# Mixed data types
mixed_list = [1, "Hello", 3.5, True]
print("Mixed list:", mixed_list)

print("\nDay 11 completed successfully!")
