# Day 18 - Strings (Advanced Operations)

text = "  Python Programming is Powerful  "

print("Original text:", repr(text))

print()

# Case conversion
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

print()

# Stripping spaces
clean_text = text.strip()
print("Stripped text:", repr(clean_text))

print()

# Replace
replaced_text = clean_text.replace("Powerful", "Awesome")
print("Replaced text:", replaced_text)

print()

# Splitting
words = replaced_text.split(" ")
print("Split words:", words)

print()

# Joining
joined_text = "-".join(words)
print("Joined text:", joined_text)

print()

# String slicing
print("First 6 chars:", joined_text[:6])
print("Reversed string:", joined_text[::-1])

print()

# String formatting
name = "Aahish"
day = 18
print(f"Day {day} completed by {name}!")

print("\nDay 18 completed successfully!")
