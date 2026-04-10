# Day 24 - Modules & Imports

print("MODULES & IMPORTS DEMO\n")

# Using math module
import math

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)

print()

# Using alias
import math as m
print("Cosine of 0:", m.cos(0))

print()

# Importing specific functions
from math import pow
print("2 raised to power 3:", pow(2, 3))

print()

# Using random module
import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice:", random.choice(["Python", "Java", "C++"]))

print()

# Using datetime module
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

print("\nDay 24 completed successfully!")
