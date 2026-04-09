# Day 46 — OOP Design Patterns (Mini Patterns)

print("OOP MINI PATTERNS PRACTICE\n")

# Factory pattern
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def animal_factory(kind):
    if kind == "dog":
        return Dog()
    elif kind == "cat":
        return Cat()

animal = animal_factory("dog")
animal.speak()

print("\n------------------\n")

# Strategy pattern
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy(a, b)

calc1 = Calculator(add)
calc2 = Calculator(multiply)

print("Add:", calc1.calculate(3, 4))
print("Multiply:", calc2.calculate(3, 4))

print("\n------------------\n")

# Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

car = Car(Engine())
car.drive()

print("\nDay 46 completed successfully!")
