# Day 19 - String Problems & Practice

# Problem 1: Reverse a string
text = "Python"
reversed_text = text[::-1]
print("Reversed:", reversed_text)

print()

# Problem 2: Palindrome check
word = "Madam"
clean_word = word.lower()
if clean_word == clean_word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

print()

# Problem 3: Count vowels in a string
sentence = "Python Programming is Powerful"
vowels = "aeiou"
count = 0

for char in sentence.lower():
    if char in vowels:
        count += 1

print("Vowel count:", count)

print()

# Problem 4: Word count
sentence = "Python makes programming enjoyable"
words = sentence.split()
print("Word count:", len(words))

print()

# Problem 5: Remove spaces from string
raw = "  Learn Python Step by Step  "
cleaned = raw.strip().replace(" ", "")
print("Cleaned string:", cleaned)

print("\nDay 19 completed successfully!")
