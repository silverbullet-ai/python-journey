# Day 56 Notes — Unit Testing with unittest

## What Is unittest?

unittest is Python’s built-in testing framework.
It provides:
- Test discovery
- Assertions
- Structured test cases
- Clear pass/fail reporting

---

## Test File Naming Rules

- Test files should start with `test_`
- Test cases should inherit from `unittest.TestCase`
- Test methods should start with `test_`

These are conventions, not decoration.

---

## Anatomy of a Unit Test

Every test has:
1. Setup (input)
2. Action (call the function)
3. Assertion (expected result)

---

## Assertions (Core Ones)

- `assertEqual(a, b)`
- `assertTrue(condition)`
- `assertFalse(condition)`
- `assertRaises(ErrorType)`

Assertions express **expectations**.

---

## To run the test 

From inside Day-56 directory (in bash):

```bash

python -m unittest test_calculator.py

```
---

## Mental Rule

> A failing test is information, not failure.
