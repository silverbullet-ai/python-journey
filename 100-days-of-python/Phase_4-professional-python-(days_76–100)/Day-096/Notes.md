# Day 96 Notes — Designing a Small Professional Project

## Why Design Comes Before Code

Most bugs originate from:
- Poor boundaries
- Undefined expectations
- Vague requirements
- Implicit assumptions

Writing code too early hides design flaws.

Professionals design before implementing.

---

## Project Criteria for the Capstone

The project must:
- Be small but realistic
- Use packaging structure
- Include tests
- Include logging
- Include proper error handling
- Be installable (editable mode)
- Be CI-ready

This is not a toy script.
It must resemble production thinking.

---

## Recommended Capstone Idea

CLI-based Task Manager (Minimal but Professional)

Core features:
- Add task
- List tasks
- Mark task complete
- Persist tasks to file (JSON)

Constraints:
- No database
- No frameworks
- Standard library preferred
- Clean package structure

Why this project works:
- Has state
- Has edge cases
- Has user interaction
- Requires error handling
- Requires testing
- Benefits from logging

---

## Defining Scope Clearly

In scope:
- Core task operations
- File persistence
- Basic validation
- Test coverage

Out of scope:
- GUI
- Authentication
- Networking
- Performance optimization

Professional design means:
Knowing what NOT to build.

---

## Defining Responsibilities

Example layers:
- models (Task)
- repository (file storage)
- service (business logic)
- cli (user interaction)

Separation matters.
Do not mix concerns.

---

## Non-Functional Requirements

The project must:
- Be testable
- Fail loudly when invalid input occurs
- Log meaningful events
- Pass all tests before “release”

This mirrors real engineering constraints.

---

## Mental Rule

> If the project cannot be explained clearly in one paragraph,
> the design is not ready.

---

## What to Do Today

1. Read the notes carefully
2. Decide:

	- Do you accept the CLI Task Manager idea?

	- Or do you want to propose an alternative?
3. Write a short design summary (in your own words)

Do not start coding yet.
Today is about clarity.
