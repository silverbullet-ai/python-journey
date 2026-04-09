# Day 43 — Decorators (Functions)

print("DECORATORS PRACTICE\n")

def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello, Aahish!")

greet()

print("\n------------------\n")

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function starting...")
        result = func(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper

@timing_decorator
def add(a, b):
    return a + b

print("Result:", add(3, 4))

print("\nDay 43 completed successfully!")