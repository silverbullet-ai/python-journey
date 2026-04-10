# Day 6 - Nested Loops & Patterns

print("Pattern 1: Square of stars")
for row in range(4):
    for col in range(4):
        print("*", end=" ")
    print()

print("\nPattern 2: Right-angled triangle")
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()

print("\nPattern 3: Numbers pattern")
for row in range(1, 5):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

print("\nPattern 4: Reverse triangle")
for row in range(5, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()

print("\nDay 6 completed successfully!")
