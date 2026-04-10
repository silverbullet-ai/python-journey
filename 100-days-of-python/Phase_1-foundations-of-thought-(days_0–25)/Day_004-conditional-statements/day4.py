# Day 4 - Conditional Statements

# Simple if
age = 20

if age >= 18:
    print("You are eligible to vote")

print()

# if-else
number = 7

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print()

# if-elif-else
marks = 78

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

print()

# Nested if
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")



print("\nDay 4 completed successfully!")
