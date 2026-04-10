# Day 21 - Error Handling (try / except)

print("ERROR HANDLING DEMO\n")

# Example 1: Handling division error
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid integers.")
else:
    print("Result:", result)
finally:
    print("Division attempt completed.\n")

# Example 2: List index error
numbers = [10, 20, 30]

try:
    index = int(input("Enter index to access: "))
    print("Value:", numbers[index])
except IndexError:
    print("Index out of range.")
except ValueError:
    print("Index must be an integer.")
finally:
    print("List access attempt completed.\n")

# Example 3: Dictionary key error
student = {"name": "Aahish", "age": 22}

try:
    key = input("Enter key to access (name/age): ")
    print("Value:", student[key])
except KeyError:
    print("Key not found in dictionary.")
finally:
    print("Dictionary access completed.")

print("\nDay 21 completed successfully!")
