# Day 13 Notes — List Slicing & Copying

## List Slicing

Slicing allows you to extract a portion of a list.

### Syntax

```python
list[start:end:step]
```

- `start` → inclusive  
- `end` → exclusive  
- `step` → jump size (optional)  

---

## Examples

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]
print(numbers[::2])   # [0, 2, 4]
print(numbers[::-1])  # Reversed list
```

---

## Negative Indexing

Negative indices count from the end.

```python
print(numbers[-1])      # Last element
print(numbers[-3:-1])   # Elements near the end
```

---

## Copying Lists (IMPORTANT)

### ❌ Wrong Way

```python
a = b
```

This does **NOT** create a copy.  
Both variables point to the same list.

---

### ✅ Correct Ways

```python
a = b.copy()
a = b[:]
```

These create a **new list**.

---

## Key Rule

- Assignment copies the **reference**.  
- Slicing or `copy()` creates a **new list**.
