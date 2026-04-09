# Day 76 — Introduction to Professional Python & Testing Mindset

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    print("Calculator module loaded successfully.")

