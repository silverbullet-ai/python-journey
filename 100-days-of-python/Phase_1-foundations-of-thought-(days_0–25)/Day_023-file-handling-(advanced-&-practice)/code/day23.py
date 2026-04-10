# Day 23 - File Handling (Advanced & Practice)

print("ADVANCED FILE HANDLING PRACTICE\n")

# Problem 1: Read file line by line
print("Reading lines from input.txt:\n")

try:
    with open("input.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("input.txt not found.")

print("\n------------------\n")

# Problem 2: Count word frequency from file
word_count = {}

with open("input.txt", "r") as file:
    for line in file:
        words = line.lower().strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:")
for word, count in word_count.items():
    print(word, ":", count)

print("\n------------------\n")

# Problem 3: Write processed data to a new file
with open("output_summary.txt", "w") as file:
    file.write("Word Frequency Summary:\n")
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")

print("Processed data written to output_summary.txt")

print("\nDay 23 completed successfully!")
