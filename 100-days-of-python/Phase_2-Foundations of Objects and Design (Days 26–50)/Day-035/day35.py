# Day 35 — Polymorphism (Duck Typing)

print("DUCK TYPING PRACTICE\n")

class Dog:
    def speak(self):
        print("Dog barks")

class Human:
    def speak(self):
        print("Human speaks")

class Robot:
    def speak(self):
        print("Robot beeps")

def make_sound(entity):
    entity.speak()

entities = [Dog(), Human(), Robot()]

for e in entities:
    make_sound(e)

print("\nDay 35 completed successfully!")
