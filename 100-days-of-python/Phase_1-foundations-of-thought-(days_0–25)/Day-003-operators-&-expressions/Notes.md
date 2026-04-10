# Day 3 Notes — Operators & Expressions

## What is an Operator?

An operator is a symbol that performs an operation on values (operands).

### Example

```python
a + b
```

Here:
- `+` is the operator  
- `a` and `b` are operands  

---

## Arithmetic Operators

| Operator | Meaning |
|----------|----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulus |
| `**` | Exponentiation |

### Example

```python
print(10 // 3)  # 3
print(10 % 3)   # 1
```

---

## Assignment Operators

| Operator | Meaning |
|----------|----------|
| `=` | Assign |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |

### Example

```python
x = 5
x += 2
print(x)  # 7
```

---

## Comparison Operators

| Operator | Meaning |
|----------|----------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

Result is always Boolean (`True` or `False`).

### Example

```python
print(5 > 3)   # True
print(5 == 2)  # False
```

---

## Logical Operators

| Operator | Meaning |
|----------|----------|
| `and` | True if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Reverses the condition |

### Example

```python
age = 20
is_student = True

print(age > 18 and is_student == True)  # True
```

---

## Operator Precedence

Python follows this priority order:

1. `()`
2. `**`
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. Comparison operators
6. `not`
7. `and`
8. `or`

Parentheses `()` can be used to control order.

### Example

```python
result = 2 + 3 * 4
print(result)  # 14

result = (2 + 3) * 4
print(result)  # 20
```
