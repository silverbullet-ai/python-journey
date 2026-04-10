# Day 12 - List Operations & Methods

numbers = [10, 20, 30]
print("Initial list:", numbers)

print()

# Adding elements
numbers.append(40)
print("After append:", numbers)

numbers.extend([50, 60])
print("After extend:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

print()

# Removing elements
numbers.remove(20)
print("After remove 20:", numbers)

removed = numbers.pop()
print("Popped element:", removed)
print("After pop:", numbers)

removed_index = numbers.pop(2)
print("Popped at index 2:", removed_index)
print("After pop index:", numbers)

print()

# Other operations
print("Length of list:", len(numbers))
print("Is 30 in list?", 30 in numbers)
print("Count of 10:", numbers.count(10))

print("\nDay 12 completed successfully!")
