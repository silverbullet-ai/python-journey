# Day 33 — Inheritance & super()

print("INHERITANCE & SUPER PRACTICE\n")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(self.name, "barks")

dog = Dog("Buddy", "Labrador")

print("Name:", dog.name)
print("Breed:", dog.breed)
dog.speak()

print("\nDay 33 completed successfully!")
