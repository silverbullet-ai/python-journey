# Day 4 Notes — Conditional Statements

## What is a Conditional Statement?

A conditional statement allows a program to **execute code based on a condition**.

The condition must evaluate to:
- `True`
- `False`

---

## The `if` Statement

### Syntax

```python
if condition:
    statement
```

If the condition is `True`, the block runs.  
If `False`, it is skipped.

### Example

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
```

---

## `if-else` Statement

### Syntax

```python
if condition:
    statement
else:
    statement
```

Only one block will execute.

### Example

```python
number = 5

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## `if-elif-else` Ladder

Used when multiple conditions are involved.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Python checks conditions from **top to bottom**.

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

---

## Nested `if`

An `if` statement inside another `if`.

Used for more complex decision logic.

### Example

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

---

## Indentation (VERY IMPORTANT)

Python uses indentation instead of braces `{}`.

- Indentation defines blocks
- Wrong indentation = error
- Standard indentation = **4 spaces**

---

## Key Rule

Conditions must result in `True` or `False`.
