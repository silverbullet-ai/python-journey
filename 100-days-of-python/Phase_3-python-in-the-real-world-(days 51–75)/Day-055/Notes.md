# Day 55 Notes — Testing Mindset & Unit Testing Foundations

## Why Testing Exists

Testing exists because:
- Code changes
- Bugs reappear
- Humans forget
- Systems grow

Testing gives you **confidence to change code**.

---

## What Testing Is NOT

Testing is not:
- Proving code is perfect
- Testing Python itself
- Writing tests for everything

Testing is about **protecting behavior**.

---

## What Is a Unit Test?

A unit test:
- Tests one small piece of logic
- Runs fast
- Has no side effects
- Is deterministic (same input → same output)

---

## What Makes Code Testable?

Testable code:
- Has clear inputs and outputs
- Avoids global state
- Separates logic from I/O
- Does not depend on time, randomness, or environment

Hard-to-test code:
- Reads input directly
- Prints everywhere
- Depends on files or network
- Mixes logic and side effects

---

## Separation of Concerns (Critical)

Bad:
```python
def calculate_total():
    price = int(input())
    print(price * 1.18)
```

Good:
```python
def calculate_total(price: float) -> float:
    return price * 1.18
```

---

## Mental Rule

> If a function is easy to test,
> it is usually well designed.
