# Day 77 Notes — Unit Testing with unittest

## Why Python Has unittest

unittest exists because:
- Testing must work without extra dependencies
- Teams need standardized tools
- Tests should behave consistently across environments

unittest is:
- Part of Python’s standard library
- Explicit and structured
- Less opinionated than modern tools like pytest

---

## What Is a Unit Test?

A unit test:
- Tests one function or method
- Uses controlled inputs
- Asserts expected behavior
- Fails clearly when behavior changes

A unit test answers one question:
“Did this unit behave exactly as expected?”

---

## Structure of a unittest Test Case

A typical unit test includes:
- A class inheriting from `unittest.TestCase`
- Methods starting with `test_`
- Assertions that verify behavior

Common pattern:
Arrange → Act → Assert

---

## How unittest Test Discovery Works

When running:

```bash
python -m unittest discover
```

This command explicitly tells `unittest` where the test files live,
ensuring consistent and predictable test discovery.

---

## About `__init__.py`

Both the `code/` and `tests/` directories contain an empty `__init__.py` file.

These files are added to:
- Mark both directories as Python packages
- Make imports explicit and unambiguous
- Improve compatibility with test discovery and future tooling

While tests may run without these files in some cases,
including them ensures the project structure behaves
consistently as it grows.