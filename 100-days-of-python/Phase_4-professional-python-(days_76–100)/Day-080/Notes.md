# Day 80 Notes — Integration Testing Basics

## What Integration Tests Are

Integration tests verify:
- Multiple components working together
- Real interactions between modules
- Behavior across boundaries

They answer the question:
“Do these pieces work together correctly?”

---

## Unit Tests vs Integration Tests

Unit tests:
- Isolate one unit
- Mock external dependencies
- Fail fast and precisely

Integration tests:
- Use real implementations
- Mock less or not at all
- Validate wiring and collaboration

Both are necessary.
They solve different problems.

---

## Why Integration Tests Matter

Even if unit tests pass:
- Modules may be wired incorrectly
- Data may flow incorrectly
- Assumptions between components may break

Integration tests catch these gaps.

---

## What NOT to Mock in Integration Tests

Avoid mocking:
- Your own modules
- Internal data flow
- Business logic

Mock only:
- Truly external systems (APIs, databases)
- Non-deterministic services

Integration tests are about **trusting your code**.

---

## Speed vs Confidence Trade-off

Integration tests are:
- Slower than unit tests
- Fewer in number
- Higher in confidence

A healthy test suite:
- Many unit tests
- Some integration tests
- Very few end-to-end tests

---

## Mental Rule

> If unit tests ask “does this work?”
> integration tests ask “does this fit together?”

---

## How to Run the Tests

From inside Day-80:
```bash
python -m unittest discover
