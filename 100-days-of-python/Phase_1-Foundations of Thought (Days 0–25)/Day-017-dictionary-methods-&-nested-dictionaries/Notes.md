# Day 17 Notes — Dictionary Methods & Nested Dictionaries

## Safe Access: `get()`

Using `[]` raises `KeyError` if the key is missing.

Safer approach:

```python
student = {"name": "Aahish", "age": 23}

print(student.get("name"))
print(student.get("grade", "Not Available"))
```

This avoids crashes by returning `None` or a default value.

---

## Common Dictionary Methods

```python
student.keys()     # Returns keys
student.values()   # Returns values
student.items()    # Returns key-value pairs
student.update({"city": "Gaya"})  # Merge / add entries
student.clear()    # Remove all entries
```

---

## Nested Dictionaries

A dictionary inside another dictionary.

### Example

```python
students = {
    "Aahish": {"age": 23, "course": "Python"},
    "Swati": {"age": 22, "course": "C++"}
}
```

Used for:

- User profiles  
- API responses  
- Configuration files  

---

## Accessing Nested Data

```python
print(students["Aahish"]["course"])
```

---

## Iterating Nested Dictionaries

```python
for name, details in students.items():
    print("Name:", name)
    for key, value in details.items():
        print(f"  {key}: {value}")
```

---

## Key Idea

Dictionaries model **meaningful relationships**, not positions.
