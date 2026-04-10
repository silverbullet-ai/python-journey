# Day 20 - Revision & Mini Practice Set

print("MINI PRACTICE SET\n")

# Problem 1: Even numbers from a list
numbers = [1, 4, 7, 10, 15, 20]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
print()

# Problem 2: Count word frequency using dictionary
sentence = "python is easy and python is powerful"
words = sentence.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)
print()

# Problem 3: Function to check palindrome
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print("Is 'Never Odd Or Even' palindrome?",
      is_palindrome("Never Odd Or Even"))
print()

# Problem 4: Remove duplicates using set
values = [1, 2, 2, 3, 4, 4, 5]
unique_values = list(set(values))
print("Unique values:", unique_values)
print()

# Problem 5: Dictionary with list values
students = {
    "Aahish": [80, 85, 90],
    "Aayan": [70, 75, 72]
}

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name}'s average marks:", avg)

print("\nDay 20 completed successfully!")
