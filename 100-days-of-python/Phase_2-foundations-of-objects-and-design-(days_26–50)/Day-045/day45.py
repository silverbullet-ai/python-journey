# Day 45 — Context Managers

print("CONTEXT MANAGERS PRACTICE\n")

# Using built-in context manager
with open("sample.txt", "w") as file:
    file.write("Hello, context managers!")

print("File written safely.")

print("\n------------------\n")

# Custom class-based context manager
class SimpleContext:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")

with SimpleContext():
    print("Inside the context")

print("\n------------------\n")

# Context manager using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Resource acquired")
    yield
    print("Resource released")

with managed_resource():
    print("Using the resource")

print("\nDay 45 completed successfully!")