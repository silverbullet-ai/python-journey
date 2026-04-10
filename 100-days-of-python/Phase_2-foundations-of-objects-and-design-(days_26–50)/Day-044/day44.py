# Day 44 — Decorators (Classes)

print("CLASS DECORATORS PRACTICE\n")

# Simple class-based decorator
class SimpleDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function execution")
        self.func()
        print("After function execution")

@SimpleDecorator
def greet():
    print("Hello, Aahish!")

greet()

print("\n------------------\n")

# Class decorator with arguments
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@Repeat(3)
def say_hi():
    print("Hi!")

say_hi()

print("\nDay 44 completed successfully!")