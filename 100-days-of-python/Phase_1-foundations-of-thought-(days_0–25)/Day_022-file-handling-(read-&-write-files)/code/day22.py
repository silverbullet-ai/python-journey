# Day 22 - File Handling (Read & Write Files)

print("FILE HANDLING DEMO\n")

# Reading a file
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("File not found.")

print("\n------------------\n")

# Writing to a file
with open("output.txt", "w") as file:
    file.write("This file was created using Python.\n")
    file.write("Day 22 of 100 Days of Python.\n")

print("Data written to output.txt")

print("\n------------------\n")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("Appending new line.\n")

print("Data appended to output.txt")

print("\nDay 22 completed successfully!")
