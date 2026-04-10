# Day 18 Notes — Strings (Advanced)

## Strings as Sequences

Strings behave like sequences:

- Indexed  
- Sliceable  
- Iterable  

But they are **immutable**.

---

## Common String Methods

```python
text = "  hello python  "

text.upper()        # Convert to uppercase
text.lower()        # Convert to lowercase
text.title()        # Title case
text.strip()        # Remove leading/trailing spaces
text.replace("python", "world")
text.split(" ")     # Split into list
"-".join(["a", "b", "c"])  # Join iterable into string
```

---

## String Slicing

Same rules as lists:

```python
text[start:end:step]
```

### Example

```python
text = "Python"

print(text[1:5])   # ytho
print(text[::-1])  # Reverse string
```

---

## String Formatting

### `f-strings` (Recommended)

```python
name = "Aahish"
age = 22

print(f"My name is {name} and I am {age} years old")
```

### `format()` Method

```python
print("My name is {} and I am {}".format(name, age))
```

---

## Important Note

Strings cannot be modified in place.  
Every operation creates a **new string**.
