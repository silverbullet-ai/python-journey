# Day 5 - Loops in Python

print("WHILE LOOP EXAMPLE")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("\nFOR LOOP EXAMPLE")

for i in range(1, 6):
    print("i:", i)

print("\nBREAK EXAMPLE")

for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at", num)
        break
    print("num:", num)

print("\nCONTINUE EXAMPLE")

for num in range(1, 6):
    if num == 3:
        continue
    print("num:", num)

print("\nINFINITE LOOP WARNING DEMO")

x = 1
while x <= 3:
    print("x:", x)
    x += 1  # removing this line causes infinite loop



print("\nDay 5 completed successfully!")
