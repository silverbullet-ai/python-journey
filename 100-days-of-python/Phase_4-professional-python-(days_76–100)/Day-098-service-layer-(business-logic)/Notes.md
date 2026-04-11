# Day 98 Notes — Service Layer

## What the Service Layer Does

The service layer:
- Defines allowed operations
- Enforces validation
- Coordinates repository calls

It does NOT:
- Read/write files directly
- Parse CLI arguments
- Print output

---

## Business Rules for This Project

- Task title cannot be empty
- Task IDs must be unique
- Marking a non-existent task raises error

Clear rules make systems predictable.

---

## ID Generation Strategy

Simple approach:
- Find max existing ID
- Increment by 1

No UUIDs.
No overengineering.

---

## Testing Strategy

Service tests must:
- Use temporary repository
- Validate correct behavior
- Validate failure cases
- Be deterministic

Tests define confidence.

---

## What To Do Today

0. Create venv
```bash
python -m venv venv
```
1. Activate Venv
```bash
source venv/Scripts/activate
```
2. Install package in editable mode
```bash
pip install -e .
```
3. Run:
```bash
python -m unittest discover -s tests
```

All tests must pass.
