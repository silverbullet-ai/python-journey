# Day 26 Notes — Python Object Model

## Everything Is an Object

- Python does not have primitive data types.
- Everything in Python is an object.

### Examples of Objects
- `int`
- `str`
- `list`
- `function`
- `class`

```python
x = 10
print(type(x))
```

---

## What Defines an Object?

Every object in Python has three properties:

- **Identity** — memory location  
- **Type** — what kind of object it is  
- **Value** — the data it holds  

```python
a = 100
print(id(a), type(a), a)
```

---

## Variables Are References

- Variables do **not** store values.
- Variables store **references to objects**.

```python
a = 10
b = a
print(id(a) == id(b))  # True
```

---

## Mutability vs Immutability

### Immutable Objects
Cannot be changed after creation.

**Examples:**
- `int`
- `float`
- `str`
- `tuple`

```python
x = 10
x += 1   # Creates a new object
```

---

### Mutable Objects
Can be modified in place.

**Examples:**
- `list`
- `dict`
- `set`

```python
nums = [1, 2]
nums.append(3)
```

---

## Why This Matters

Mutability affects:

- Shared references  
- Function behavior  
- Bugs and side effects  
- OOP design safety  

---

## Functions Are Objects Too

Functions are **first-class objects**.

They can be:
- Assigned to variables  
- Passed as arguments  
- Stored in data structures  

```python
def greet():
    return "Hello"

print(type(greet))
```

---

## Mental Rule

- Variables **point to objects**.  
- Objects have **identity, type, and value**.  
- **Mutability defines behavior**.
