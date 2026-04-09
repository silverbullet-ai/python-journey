# Day 42 — Generators

print("GENERATORS PRACTICE\n")

def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up(5)

for num in gen:
    print(num)

print("\nTrying to iterate again:")
for num in gen:
    print(num)  # Will not run

print("\nCreating new generator:")
for num in count_up(3):
    print(num)

print("\nDay 42 completed successfully!")