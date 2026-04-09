# Day 34 — Method Overriding & Polymorphism

print("METHOD OVERRIDING & POLYMORPHISM PRACTICE\n")

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()

print("\nDay 34 completed successfully!")
