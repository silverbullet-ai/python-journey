# Day 78 Notes — Assertions, Test Design & Edge Cases

## Why Assertions Matter More Than Test Count

A test is only as good as its assertion.

Bad tests:
- Pass easily
- Fail vaguely
- Miss real bugs

Good tests:
- Fail loudly
- Point directly to the problem
- Protect behavior, not implementation

---

## Assertions Are Contracts

An assertion states:
“This behavior must not change without intention.”

Assertions should be:
- Specific
- Clear
- Minimal

Avoid asserting more than necessary.

---

## Common Assertion Types in unittest

- assertEqual(a, b)
- assertNotEqual(a, b)
- assertTrue(condition)
- assertFalse(condition)
- assertIsNone(value)
- assertRaises(Exception)

Choose the assertion that best communicates intent.

---

## Weak Tests vs Strong Tests

Weak test:
- Only checks that code runs

Strong test:
- Checks exact output
- Validates edge behavior
- Fails for the right reason

Passing tests are useless
if they allow broken behavior.

---

## Edge Cases Are Where Bugs Hide

Edge cases include:
- Zero values
- Negative numbers
- Empty inputs
- Boundary conditions
- Invalid input types

Professional testing assumes:
“If it can break, it eventually will.”

---

## Test Behavior, Not Implementation

Tests should care about:
- What the function returns
- What errors it raises

Tests should not care about:
- How the function is implemented internally

This allows safe refactoring.

---

## Mental Rule for Test Design

> If a test would still pass after breaking the function,
> the test is not doing its job.

---

## How to Run the Tests

From inside Day-78:
```bash
python -m unittest discover
```
