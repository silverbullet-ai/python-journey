# Day 13 - List Slicing & Copying

numbers = [0, 1, 2, 3, 4, 5]

print("Original list:", numbers)

print("\nSLICING EXAMPLES")
print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[3:]:", numbers[3:])
print("numbers[::2]:", numbers[::2])
print("numbers[::-1]:", numbers[::-1])

print()

# Referencing (dangerous)
a = numbers
a.append(6)

print("After modifying a:")
print("numbers:", numbers)
print("a:", a)

print()

# Proper copying
numbers = [0, 1, 2, 3, 4, 5]
b = numbers.copy()
b.append(6)

print("After copying and modifying b:")
print("numbers:", numbers)
print("b:", b)

print()

# Copy using slicing
c = numbers[:]
c.remove(2)

print("After slicing copy and modifying c:")
print("numbers:", numbers)
print("c:", c)

print("\nDay 13 completed successfully!")
