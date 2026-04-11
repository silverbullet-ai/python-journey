# Day 79 Notes — Mocking & Isolation

## Why Mocking Exists

Unit tests should test:
- Your logic
- Your decisions
- Your behavior

They should not depend on:
- Network calls
- File systems
- Databases
- Time
- Randomness

Mocking exists to replace real dependencies
with controlled, predictable behavior.

---

## What a Mock Really Is

A mock is a fake object that:
- Pretends to be a real dependency
- Returns values you define
- Records how it was used

Mocks allow tests to:
- Be fast
- Be deterministic
- Fail only when your code is wrong

---

## Unit Tests vs External Systems

If a unit test:
- Needs internet
- Needs a database
- Depends on system time

It is no longer a unit test.

Mocks keep tests focused and isolated.

---

## When to Mock (and When Not To)

Mock when:
- The dependency is slow
- The dependency is external
- The dependency is non-deterministic

Do NOT mock:
- The function under test
- Simple, pure logic
- Data structures

Mocking is a tool, not a default.

---

## unittest.mock Basics

Common tools:
- `patch` — temporarily replaces objects
- `Mock` — generic fake objects

Key idea:
You mock **where the dependency is used**,
not where it is defined.

---

## Mental Rule

> If a test fails because of something
> outside your control,
> the test is poorly isolated.

---

## How to Run the Tests

From inside Day-79:
```bash
python -m unittest discover
