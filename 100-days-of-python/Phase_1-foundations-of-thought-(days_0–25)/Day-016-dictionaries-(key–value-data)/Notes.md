# Day 16 Notes — Dictionaries

## What is a Dictionary?

A dictionary stores data as **key–value pairs**.

### Example

```python
student = {
    "name": "Aahish",
    "age": 22,
    "course": "Python"
}
```

---

## Dictionary Characteristics

- Unordered (conceptually)  
- Keys must be unique  
- Keys must be immutable (string, number, tuple)  
- Values can be anything  
- Mutable (can be changed)  

---

## Accessing Values

Use keys, not indices.

### Example

```python
print(student["name"])
```

⚠ Accessing a non-existing key causes `KeyError`.

Safer alternative:

```python
print(student.get("city"))  # Returns None if key doesn't exist
```

---

## Adding & Updating Values

### Add New Key

```python
student["city"] = "Gaya"
```

### Update Existing Key

```python
student["age"] = 23
```

---

## Removing Entries

```python
del student["course"]
student.pop("age")
```

---

## Iterating Over Dictionaries

```python
# Iterate over keys
for key in student:
    print(key)

# Iterate over values
for value in student.values():
    print(value)

# Iterate over key-value pairs
for key, value in student.items():
    print(key, value)
```

---

## When to Use Dictionaries

- Structured data  
- Lookup tables  
- Configurations  
- API / JSON data  
