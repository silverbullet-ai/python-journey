# Day 88 Notes — Packaging Basics

## What “Packaging” Really Means

Packaging is about:
- Structure
- Intent
- Discoverability

It answers:
“Can this code be used as a project, not just a script?”

Packaging is NOT:
- Uploading to PyPI
- Adding heavy tooling
- Overengineering

---

## What Makes a Python Project Installable

A project becomes installable when:
- Code is organized as a package
- Dependencies are declared
- Metadata exists

This allows tools to:
- Discover the package
- Install it
- Import it reliably

---

## Why pyproject.toml Exists

`pyproject.toml` is:
- A standardized project configuration file
- The modern replacement for scattered configs
- The place where tools look first

It declares:
- Project metadata
- Build system requirements
- (Later) tool configurations

---

## src/ Layout (Important Concept)

Using a `src/` directory:
- Prevents accidental imports
- Ensures tests use installed code
- Matches professional project structure

Without `src/`:
- Imports may work locally
- Fail when installed

This layout enforces correctness.

---

## Packages vs Modules

- A **module** is a single `.py` file
- A **package** is a directory with `__init__.py`

Packages:
- Group related functionality
- Scale better
- Are easier to distribute

---

## Mental Rule

> If code is meant to be reused,
> it should be structured as a package.

---

## What to Do Today
1. Explore the folder structure
2. Notice how:
	- Code lives inside a package
	- Metadata lives outside

3. (Optional) From repo root, try:
```bash
winpty python
>>> from sample_pkg.core import greet
>>> greet("Aahish")
>>> exit()
```
4. Observe how structure enables clarity

Do not install or publish anything today.
This is about understanding, not execution.
