# 📘 Day 28 Notes — Constructors & `self`

## What Is a Constructor?

- A constructor is a special method  
- It runs automatically when an object is created  
- In Python, the constructor is named `__init__`  

```python
class Student:
    def __init__(self):
        pass
```

---

## Why `self` Exists

- `self` represents the current object  
- It allows each instance to store its own data  
- Python passes `self` automatically  

```python
student = Student()
# Internally becomes:
Student.__init__(student)
```

---

## Creating Instance Attributes

- Instance attributes belong to a specific object  

```python
class Student:
    def __init__(self, name):
        self.name = name
```

```python
s1 = Student("Aahish")
s2 = Student("Rahul")
```

- `s1.name` and `s2.name` are independent  

---

## How Objects Store Data

- Each instance has its own attribute dictionary  

```python
print(s1.__dict__)
print(s2.__dict__)
```

---

## Common Beginner Mistake

Forgetting `self`:

```python
# ❌ Wrong
name = name

# ✅ Correct
self.name = name
```

---

## Mental Rule

> `self` is not a keyword.  
> It is the object itself.
