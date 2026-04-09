# Day 11 Notes — Lists

## Why Lists?

Lists allow us to store **multiple values in a single variable**.

Instead of:

```python
a = 10
b = 20
c = 30
```

We use:

```python
numbers = [10, 20, 30]
```

---

## Creating a List

### Syntax

```python
list_name = [value1, value2, value3]
```

Lists can store:

- Integers  
- Floats  
- Strings  
- Mixed data types  

### Example

```python
data = [1, 2.5, "Python", True]
```

---

## Indexing

Lists are **zero-indexed**.

### Example

```python
numbers = [10, 20, 30]

print(numbers[0])  # 10
print(numbers[1])  # 20
```

### Negative Indexing

```python
print(numbers[-1])  # Last element
```

---

## Modifying Lists

Lists are **mutable**, meaning they can be changed.

### Example

```python
numbers = [10, 20, 30]
numbers[1] = 50
print(numbers)  # [10, 50, 30]
```

---

## Iterating Over a List

Use a `for` loop to access each element.

### Example

```python
numbers = [10, 20, 30]

for item in numbers:
    print(item)
```

---

## Key Concept

Lists store **references to objects**, not copies.
