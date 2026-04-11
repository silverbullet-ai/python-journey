# Day 66 Notes — Itertools & Lazy Computation

## Eager vs Lazy Computation

### Eager (Immediate)
- Computes all values at once
- Stores results in memory

Example:
```python
squares = [x * x for x in range(1_000_000)]
```

### Lazy (On Demand)
- Produces values one at a time
- Uses minimal memory

Example:
```python
squares = (x * x for x in range(1_000_000))
```

---

## Why itertools Exists

`itertools` provides:
- Fast, memory-efficient building blocks
- Lazy iteration primitives
- Expressive alternatives to manual loops

It lets you **compose behavior**, not manage state.

---

## Common itertools Tools (Practical)

- `count()` → infinite counters
- `islice()` → slice iterators
- `chain()` → combine iterables
- `takewhile()` / `dropwhile()` → conditional flow
- `product()` / `permutations()` → combinatorics

All are **lazy**.

---

## Avoiding Intermediate Lists

Bad:
```python
filtered = [x for x in data if x % 2 == 0]
mapped = [x * 2 for x in filtered]
```

Better:
```python
mapped = (x * 2 for x in data if x % 2 == 0)
```

Best (explicit intent):
```python
from itertools import islice
mapped = islice((x * 2 for x in data if x % 2 == 0), 10)
```

---

## Mental Rule

> If you don’t need all the data at once,
> don’t create it all at once.
