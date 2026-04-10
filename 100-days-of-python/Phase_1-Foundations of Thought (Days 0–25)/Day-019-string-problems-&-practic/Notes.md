# Day 19 Notes — String Practice Patterns

## Common String Problem Patterns

### Cleaning Input

```python
text = "  Hello Python  "

cleaned = text.strip().lower().replace("python", "world")
print(cleaned)
```

Used methods:
- `strip()`  
- `lower()`  
- `replace()`  

---

### Reversing Strings

```python
text = "Python"
reversed_text = text[::-1]
print(reversed_text)
```

---

### Counting

#### Using a Loop

```python
text = "banana"
count = 0

for ch in text:
    if ch == "a":
        count += 1

print(count)
```

#### Using `count()`

```python
text = "banana"
print(text.count("a"))
```

---

### Comparing Strings

Case-insensitive comparison:

```python
a = "Python"
b = "python"

if a.lower() == b.lower():
    print("Same text")
```

Always clean before comparing when needed.

---

### Breaking into Words

```python
sentence = "Learn Python step by step"

words = sentence.split()
print(words)
print(len(words))
```

---

## Important Habit

Always decide:

- Do I need to clean the string?  
- Do I care about case?  
- Do I care about spaces or punctuation?  

Strong string handling begins with clarity of intent.

