# Day 52 Notes — PEP 8 & Clean Code Discipline

## What Is PEP (Python Enhancement Proposal) 8?

PEP 8 is Python’s official style guide.
It defines how Python code should look.

Its purpose is not control —  
its purpose is **clarity and consistency**.

---

## Why PEP 8 Matters

- Code is read far more than written
- Teams need shared conventions
- Consistent formatting reduces cognitive load
- Style disagreements waste time

PEP 8 removes ambiguity.

---

## The Most Important PEP 8 Rules (Focus Only on These)

### 1. Indentation
- Use **4 spaces**
- Never mix tabs and spaces

Bad:
```python
if x>5:
 print(x)
```

Good:
```python
if x > 5:
    print(x)
```

---

### 2. Line Length
- Limit lines to ~79 characters
- Break long expressions logically

Bad:
```python
result = very_long_function_name(arg1, arg2, arg3, arg4, arg5)
```

Good:
```python
result = very_long_function_name(
    arg1, arg2, arg3, arg4, arg5
)
```

---

### 3. Spacing Around Operators
Spaces improve readability.

Bad:
```python
x=10+5*3
```

Good:
```python
x = 10 + 5 * 3
```

---

### 4. Blank Lines Are Meaningful
- Use blank lines to separate ideas
- Two blank lines between top-level functions

---

### 5. Naming Conventions

- variables & functions → `snake_case`
- classes → `PascalCase`
- constants → `UPPER_CASE`

Bad:
```python
TotalValue = 100
```

Good:
```python
TOTAL_VALUE = 100
```

---

## Clean Code Discipline

Clean code:
- Looks calm
- Is predictable
- Feels easy to scan

Messy code creates mental resistance.

---

## Mental Rule

> If your code looks messy,
> your thinking probably is too.
