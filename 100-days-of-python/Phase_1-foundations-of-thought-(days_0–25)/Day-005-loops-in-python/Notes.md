# Day 5 Notes — Loops

## Why Loops?

Loops allow us to **repeat a block of code** without writing it multiple times.

Instead of:

```python
print("Hello")
print("Hello")
print("Hello")
```

We use a loop.

---

## `while` Loop

The `while` loop runs **as long as a condition is True**.

### Syntax

```python
while condition:
    statement
```

### Example

```python
count = 1

while count <= 3:
    print("Hello")
    count += 1
```

Important:

- Condition must eventually become `False`
- Otherwise, it becomes an **infinite loop**

---

## `for` Loop

The `for` loop is used to **iterate over a sequence**.

Commonly used with `range()`.

### Syntax

```python
for variable in range(start, stop):
    statement
```

`range(start, stop):`

- `start` → inclusive  
- `stop` → exclusive  

### Example

```python
for i in range(1, 4):
    print(i)
```

---

## `break` Statement

Used to **exit the loop immediately**, even if the condition is True.

### Example

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## `continue` Statement

Used to **skip the current iteration** and move to the next one.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Key Difference

- `while` → condition-based loop  
- `for` → sequence-based loop
