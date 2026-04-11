# Day 99 Notes — CLI Layer

## Purpose of CLI Layer

The CLI:
- Parses arguments
- Instantiates dependencies
- Calls service methods
- Prints results

It does NOT:
- Contain business logic
- Handle persistence directly
- Make validation decisions

---

## Storage Path Strategy

- Default: tasks.json
- Optional: --storage custom_path.json

CLI decides path.
Repository receives it.

---

## Error Handling

CLI should:
- Catch ValueError
- Print friendly message
- Exit gracefully

Service should:
- Raise meaningful errors

Separation is critical.

---

## How To Run

From inside Day-99:

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
3. Run these commands
```bash
python -m task_manager.cli add "Learn Architecture"
python -m task_manager.cli list
python -m task_manager.cli complete 1
python -m task_manager.cli list
```
---

## What To Observe
- Business logic is untouched.
- Repository is untouched.
- CLI just wires.
- Storage path is configurable:

Example:
```bash
python -m task_manager.cli --storage mytasks.json add "Test"
```
