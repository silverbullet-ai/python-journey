# Day 8 - Functions (Introduction)

# Simple function
def greet():
    print("Hello, welcome to Day 8!")

greet()

print()

# Function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("Aahish")
greet_user("Python Learner")

print()

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(10, 20)
print("Sum:", sum_result)

print()

# Function with logic
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = 7
print("Is", num, "even?", check_even(num))



print("\nDay 8 completed successfully!")
