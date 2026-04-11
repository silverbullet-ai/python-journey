# Day 97 Notes — Models & Repository

## Why Start With Repository

The repository:
- Defines persistence behavior
- Forces clean boundaries
- Enables testing without CLI

If storage is unstable,
everything above it becomes unstable.

---

## Repository Responsibilities

- Accept storage path in constructor
- Create file if missing
- Load tasks from JSON
- Save tasks to JSON
- Convert between dict and Task objects

No business logic allowed here.

---

## Deterministic Testing

Repository tests must:
- Use temporary file paths
- Never rely on existing files
- Clean up after themselves
- Be repeatable

Flaky storage tests destroy trust.

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
