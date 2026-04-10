# Day 21 Notes — Error Handling

## What is an Error?

An error occurs when Python encounters something it cannot execute.

Common runtime errors:

- `ValueError`
- `ZeroDivisionError`
- `TypeError`
- `IndexError`
- `KeyError`

---

## `try / except`

Used to handle errors without crashing the program.

### Syntax

```python
try:
    risky_code
except ErrorType:
    handling_code
```

### Example

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## Handling Multiple Exceptions

You can catch different errors separately.

```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("Conversion failed.")
```

---

## `else` Block

Runs if no exception occurs.

```python
try:
    x = 5 / 1
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
```

---

## `finally` Block

Runs no matter what (error or no error).  
Used for cleanup.

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
```

---

## Why Error Handling Matters

- Prevents crashes  
- Improves user experience  
- Makes programs reliable  
- Encourages defensive programming
