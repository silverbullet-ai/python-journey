# Day 32 — Composition vs Inheritance

print("COMPOSITION vs INHERITANCE PRACTICE\n")

# Inheritance example
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

print("\n------------------\n")

# Composition example
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is driving")

car = Car()
car.drive()

print("\nDay 32 completed successfully!")
