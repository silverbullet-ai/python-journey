# Day 58 Notes — Test Isolation, Setup & Teardown

## What Is Test Isolation?

Test isolation means:
- Each test runs independently
- No test depends on another
- Order of execution does not matter

A test should pass:
- Alone
- First
- Last
- In any order

---

## The Danger of Shared State

Shared state occurs when:
- Tests modify the same object
- Data persists across tests
- One test affects another’s outcome

This leads to:
- Flaky tests
- False confidence
- Random failures

---

## setUp() and tearDown()

### setUp()
- Runs **before each test**
- Used to create fresh state

### tearDown()
- Runs **after each test**
- Used to clean up resources

They guarantee isolation.

---

## What Belongs in setUp()

Good candidates:
- Fresh objects
- Temporary data
- Test fixtures

Bad candidates:
- Heavy logic
- Conditional behavior
- Assertions

---

## Running the Tests

From inside Day-58:
```bash
python -m unittest test_bank_account.py
```
---

## Mental Rule

> If a test only passes when run after another test,
> it is broken.
