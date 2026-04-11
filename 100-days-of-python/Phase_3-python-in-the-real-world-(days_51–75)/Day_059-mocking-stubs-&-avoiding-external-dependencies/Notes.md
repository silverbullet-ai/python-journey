# Day 59 Notes — Mocking & External Dependencies

## Why External Dependencies Are Dangerous

External dependencies:
- Make tests slow
- Make tests flaky
- Require internet, files, or system state
- Can fail for reasons unrelated to your code

Unit tests must be:
- Fast
- Deterministic
- Independent

---

## What Is Mocking?

Mocking means:
- Replacing a real dependency
- With a fake, controlled version
- That returns predictable results

You are not testing the dependency.
You are testing **your logic**.

---

## Mock vs Stub (Simple Distinction)

### Stub
- Returns fixed data
- Has no logic

### Mock
- Can assert how it was used
- Tracks calls and arguments

---

## When to Mock

Mock:
- Network calls
- File I/O
- Time
- Randomness
- External APIs

Do NOT mock:
- Your own core logic
- Value objects
- Pure functions

---

## Running the Tests

From inside Day-59:
```bash
python -m unittest test_weather.py
```
---

## Mental Rule

> If a test requires internet, time, or files,
> it is not a unit test.
