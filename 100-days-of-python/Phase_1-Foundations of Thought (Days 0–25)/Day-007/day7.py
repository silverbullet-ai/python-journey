# Day 7 - Loop Control & Logic Practice

print("BREAK EXAMPLE")
for i in range(1, 10):
    if i == 6:
        print("Breaking at", i)
        break
    print(i)

print("\nCONTINUE EXAMPLE")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

print("\nPASS EXAMPLE")
for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)

print("\nLOGIC PRACTICE")

# Print numbers from 1 to 10 except multiples of 3
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)



print("\nDay 7 completed successfully!")
