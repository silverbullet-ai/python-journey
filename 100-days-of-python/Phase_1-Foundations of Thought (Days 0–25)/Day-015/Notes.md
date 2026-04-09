# Day 15 Notes — Sets

## What is a Set?

A set is an **unordered collection of unique elements**.

- No duplicates allowed  
- No indexing  
- Mutable (can be changed)  

---

## Creating a Set

### Syntax

```python
s = {1, 2, 3}
```

### Empty Set

```python
s = set()   # Correct way
```

⚠ `{}` creates an empty dictionary, NOT a set.

---

## Set Characteristics

- Unordered  
- Unique elements  
- Mutable  
- No indexing or slicing  

---

## Adding & Removing Elements

```python
s = {1, 2, 3}

s.add(4)          # Add element
s.remove(2)       # Error if value not present
s.discard(10)     # No error if value missing
s.pop()           # Removes a random element
```

---

## Set Operations

### Union

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
print(A.union(B))
```

### Intersection

```python
print(A & B)
print(A.intersection(B))
```

### Difference

```python
print(A - B)
print(A.difference(B))
```

---

## When to Use Sets

- Remove duplicates  
- Membership testing  
- Mathematical set operations  
- When order doesn’t matter  
