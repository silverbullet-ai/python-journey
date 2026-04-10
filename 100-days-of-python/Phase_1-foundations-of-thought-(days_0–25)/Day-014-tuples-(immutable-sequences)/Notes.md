# Day 14 Notes — Tuples

## What is a Tuple?

A tuple is an **ordered collection of items** like a list,  
but it is **immutable** (cannot be changed).

---

## Creating a Tuple

### Syntax

```python
t = (1, 2, 3)
```

### Single-element Tuple

```python
t = (5,)   # Comma is mandatory
```

Without the comma, it is NOT a tuple:

```python
t = (5)    # This is just an integer
```

---

## Tuple Characteristics

- Ordered  
- Indexed  
- Allows duplicate values  
- Immutable  

---

## Accessing Tuple Elements

### Indexing

```python
t = (10, 20, 30)
print(t[0])  # 10
```

### Slicing

```python
print(t[1:3])  # (20, 30)
```

---

## Immutability (Core Concept)

Once created, a tuple:

- Cannot add elements  
- Cannot remove elements  
- Cannot modify elements  

Example:

```python
t = (1, 2, 3)
# t[0] = 10   ❌ TypeError
```

This prevents accidental data changes.

---

## Tuple vs List

### List

- Mutable  
- Uses `[]`  

```python
lst = [1, 2, 3]
```

### Tuple

- Immutable  
- Uses `()`  

```python
tpl = (1, 2, 3)
```

---

## When to Use Tuples

- Fixed data (coordinates, RGB values)  
- Data that should not change  
- As dictionary keys (later)  
- Returning multiple values from functions
