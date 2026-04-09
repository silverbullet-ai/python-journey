# Day 100 Notes — Hardening & Logging

## Why Logging Matters

Print statements help users.
Logging helps developers.

Logging allows:
- Tracing behavior
- Diagnosing failures
- Observing system state

Logging should not:
- Replace error handling
- Expose sensitive data
- Create noise

---

## Logging Strategy

We will:
- Use Python's built-in logging module
- Log key service operations
- Log errors at appropriate levels
- Keep logs simple and structured

---

## What We Will NOT Do

- Add complex logging frameworks
- Overconfigure loggers
- Log excessively

Professional polish means restraint.

---

## Final Review Checklist

- Layers remain separated
- No circular dependencies
- Tests pass
- CLI thin
- Repository defensive
- Business rules enforced
- Logging helpful, not noisy

Professional software is predictable.

---

## Implementation

### `logging_config.py`

```python

import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
```
### Update `service.py` (Add Logging)
Add at top:

```python
import logging

logger = logging.getLogger(__name__)
```

Then modify methods:

```python
def add_task(self, title: str) -> Task:
    if not title or not title.strip():
        logger.warning("Attempted to add empty task")
        raise ValueError("Task title cannot be empty")

    tasks = self._repo.load_tasks()
    next_id = self._generate_next_id(tasks)

    new_task = Task(id=next_id, title=title.strip())
    tasks.append(new_task)
    self._repo.save_tasks(tasks)

    logger.info(f"Task added with ID {new_task.id}")
    return new_task
```
And:

```python
def mark_complete(self, task_id: int) -> Task:
    tasks = self._repo.load_tasks()

    for task in tasks:
        if task.id == task_id:
            task.completed = True
            self._repo.save_tasks(tasks)
            logger.info(f"Task {task_id} marked complete")
            return task

    logger.error(f"Task {task_id} not found")
    raise ValueError("Task not found")
```
### Update `cli.py`

At top:
```python
from task_manager.logging_config import configure_logging
```
Inside main() before parsing:
```python
configure_logging()
```
---

## Run

```bash
python -m task_manager.cli add "Final Review"
```

You should see:

```bash
2026-... | INFO | task_manager.service | Task added with ID 1
Added task [1] Final Review
```