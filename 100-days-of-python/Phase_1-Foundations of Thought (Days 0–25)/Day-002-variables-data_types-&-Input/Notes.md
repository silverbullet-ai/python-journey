# Day 2 Notes — Variables & Data Types

## What is a Variable?

A variable is a **name that refers to a value stored in memory**.

### Example

```python
x = 10
```

Here:
- `x` is the variable name  
- `10` is the value  

---

## Variable Naming Rules

- Must start with a letter or underscore  
- Cannot start with a number  
- Cannot use spaces  
- Case-sensitive (`age` and `Age` are different)  
- Should be meaningful  

### Good Examples

```python
total_marks = 95
user_name = "Aahish"
age = 20
```

### Bad Examples

```python
1value = 10        # ❌ Cannot start with number
my value = 5       # ❌ No spaces allowed
@data = 100        # ❌ Invalid character
```

---

## Common Data Types in Python

### 1️⃣ int
```python
x = 10
y = -5
z = 100
```

### 2️⃣ float
```python
pi = 3.14
value = 2.0
```

### 3️⃣ str
```python
name = "hello"
language = 'Python'
```

### 4️⃣ bool
```python
is_active = True
is_logged_in = False
```

Python automatically decides the type — this is called **dynamic typing**.

---

## Checking Data Type

Use:

```python
type(variable)
```

Example:

```python
x = 10
print(type(x))
```

---

## Taking Input from User

`input()` always returns a **string**.

```python
name = input("Enter your name: ")
```

If you need a number:

```python
age = int(input("Enter your age: "))
```

---

## Important Concept

Python does **NOT** need you to declare types explicitly.  
Types are decided at runtime.
