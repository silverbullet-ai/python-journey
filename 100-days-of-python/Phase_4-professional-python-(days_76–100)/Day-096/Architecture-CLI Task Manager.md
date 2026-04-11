# Layered Architecture — Task Manager Design

## Project Structure

```markdown

task_manager/
├── pyproject.toml
├── README.md
├── src/
│   └── task_manager/
│       ├── __init__.py
│       ├── models.py
│       ├── repository.py
│       ├── service.py
│       └── cli.py
└── tests/
    ├── __init__.py
    ├── test_repository.py
    └── test_service.py
```

## Layer Responsibilities

---

## models.py

### Responsibility:
- Define `Task` structure
- Represent domain entity

### Rules:
- No file I/O
- No CLI logic
- No business decisions

### Example responsibilities:
- `id`
- `title`
- `completed` status

This layer defines **what a task is**.

---

##  repository.py

### Responsibility:
- Persist tasks to JSON file
- Load tasks from JSON file

### Rules:
- Accept storage path in constructor
- No CLI parsing
- No business logic

### Example:

`TaskRepository(storage_path: str)`

Responsibilities:
- Create file if not exists
- Read JSON safely
- Write JSON safely
- Convert between `dict` ↔ `Task`

This layer handles **where data lives**.

---

## service.py

### Responsibility:
- Business logic
- Validation
- Orchestration

### Rules:
- Depends on repository
- Does not know about JSON
- Does not know about CLI arguments
- Raises meaningful exceptions

### Example responsibilities:
- `add_task(title)`
- `list_tasks()`
- `mark_complete(task_id)`

This layer defines **what operations are allowed**.

---

## cli.py

### Responsibility:
- Parse command line arguments
- Instantiate repository
- Instantiate service
- Call service methods
- Print output

### Rules:
- No business logic
- No file operations directly
- No validation beyond parsing

CLI is just a **translator between user and service layer**.

---

## Dependency Flow (Very Important)

Dependencies flow downward only.

```markdown
CLI  
↓  
Service  
↓  
Repository  
↓  
File System  
```

Never upward.

- Repository must NOT import CLI.
- Service must NOT import CLI.
- Models must NOT import repository.

This keeps layers clean.

---

## Testing Strategy

### `test_repository.py`
- Uses temporary file path
- Tests file creation
- Tests save/load
- Tests edge cases

### `test_service.py`
- Uses real repository with temp path
- Tests business logic
- Tests invalid inputs
- Tests marking tasks complete

We do NOT test CLI deeply.  
CLI is thin.

---

## Design Principles Applied

We are now applying:

- Separation of concerns
- Dependency injection
- Single responsibility principle
- Deterministic testing
- Configurable infrastructure
- Installable packaging

This is not beginner scripting.

---

## Final Summary

A layered CLI task manager where:

- models define the domain,
- repository handles persistence via injected storage path,
- service enforces business logic,
- cli handles user interaction,
- tests validate repository and service independently.
