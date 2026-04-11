# Day 57 Notes — Test Design & Edge Cases

## What Should Be Tested?

Test:
- Core business logic
- Boundary conditions
- Failure scenarios
- Behavior that must never change

Do NOT test:
- Trivial getters/setters
- Python built-ins
- Logging output
- Implementation details

---

## Normal Case vs Edge Case

### Normal Case
Expected, common input.

Example:
```python
divide(10, 2)
```

### Edge Case
Boundary or unusual input that can break logic.

Examples:
```python
divide(0, 5)
divide(1, 1)
divide(10, 0)
```

Edge cases reveal weaknesses.

---

## Negative Testing (Very Important)

Negative tests verify that:
- Invalid input is rejected
- Errors are raised correctly
- System fails safely

A test that never fails is suspicious.

---

## Avoid Fragile Tests

Fragile tests:
- Depend on exact output formatting
- Break on refactoring
- Test *how* instead of *what*

Good tests:
- Focus on behavior
- Survive refactoring
- Read like documentation

---

## Running the Tests

From inside Day-57:
```bash
python -m unittest test_calculator.py
```
---

## Mental Rule

> If a test breaks when behavior didn’t change,
> the test is wrong.
