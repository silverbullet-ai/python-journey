# Day 10 - Variable Scope

# Global variable
x = 10

def show_global():
    print("Inside function, x =", x)

show_global()
print("Outside function, x =", x)

print()

# Local variable
def local_example():
    y = 5
    print("Inside function, y =", y)

local_example()
# print(y)  # Uncommenting this will cause an error

print()

# Modifying global variable using global keyword
counter = 0

def increment_counter():
    global counter
    counter += 1
    print("Counter inside function:", counter)

increment_counter()
increment_counter()

print("Counter outside function:", counter)

print()

# Better approach: avoid global
def increment(value):
    return value + 1

counter = increment(counter)
print("Counter using return:", counter)

print("\nDay 10 completed successfully!")
