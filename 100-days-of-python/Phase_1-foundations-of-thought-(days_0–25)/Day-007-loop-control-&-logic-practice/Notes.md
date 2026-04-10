# Day 7 Notes — Loop Control

## `break`

- Immediately exits the loop  
- Used when no further iteration is needed  

### Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## `continue`

- Skips the current iteration  
- Loop continues with the next iteration  

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## `pass`

- Does nothing  
- Used as a placeholder where a statement is required  

### Example

```python
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
```

---

## Why `pass` Exists

- To avoid syntax errors  
- To write code structure first  
- To fill logic later  

---

## Key Difference

- `break` → stops the loop  
- `continue` → skips an iteration  
- `pass` → does nothing, continues normally
