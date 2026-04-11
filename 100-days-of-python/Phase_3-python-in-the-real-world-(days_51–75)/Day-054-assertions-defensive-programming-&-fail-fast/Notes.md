# Day 54 Notes — Assertions, Defensive Programming & Fail Fast

## What Is Defensive Programming?

Defensive programming is the practice of:
- Anticipating misuse
- Rejecting invalid input early
- Preventing silent failures

You do not trust callers blindly.

---

## What Are Assertions?

Assertions are **sanity checks**.
They verify assumptions that *must* be true.

Example:
```python
assert x > 0
```

Meaning:
"If this is false, something is fundamentally wrong."

---

## Assertions vs Exceptions (Critical Difference)

### Assertions
- Used for **developer mistakes**
- Catch bugs during development
- Can be disabled in optimized mode
- Not for user input validation

### Exceptions
- Used for **runtime errors**
- Handle invalid user input
- Expected failure scenarios
- Always active

---

## When to Use Assertions

Use assertions when:
- You want to enforce internal invariants
- A condition should *never* be false
- A failure indicates a bug, not bad input

Do NOT use assertions for:
- User input validation
- Network failures
- File I/O errors

---

## Fail Fast Principle

Failing early:
- Exposes bugs immediately
- Prevents corrupted state
- Makes debugging easier

Failing late:
- Spreads damage
- Hides root causes
- Creates unpredictable behavior

---

## Mental Rule

> If something must be true for your code to work,
> assert it.
