# Day 24 Notes — Modules & Imports

## What is a Module?

A module is a file containing Python code (functions, variables, classes)  
that can be reused in other programs.

Examples:
- `math`
- `random`
- `datetime`

---

## Importing Modules

###  `import module`

Use `module.function()`.

```python
import math

print(math.sqrt(16))
```

---

###  `from module import name`

Use the imported name directly.

```python
from math import sqrt

print(sqrt(16))
```

---

### `Aliasing`

Rename modules for convenience.

```python
import math as m

print(m.pi)
```

---

## Built-in Modules (Common)

- `math` → mathematical operations  
- `random` → randomness  
- `datetime` → dates and time  
- `os` → interacting with OS (advanced)  
- `sys` → system-level details (advanced)  

---

## Why Modules Matter

- Avoid rewriting code  
- Organize large programs  
- Improve readability  
- Encourage reuse  
- Promote modular design  
