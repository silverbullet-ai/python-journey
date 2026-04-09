# Day 86 Notes — Virtual Environments & Isolation

## Why Environments Exist

Python code depends on:
- Python version
- Installed packages
- Package versions

Without isolation:
- One project breaks another
- Upgrades cause hidden failures
- Bugs appear “randomly”

Virtual environments solve this.

---

## What a Virtual Environment Is

A virtual environment:
- Isolated Python interpreter
- Separate package installation space
- Local to a project

Each project gets:
- Its own dependencies
- Its own versions
- Its own safety

---

## Why Global Installs Are Dangerous

Installing packages globally means:
- Projects share dependencies
- Version conflicts are inevitable
- Debugging becomes unpredictable

Rule:
> Never trust global state.

---

## Creating a Virtual Environment

Inside a project directory:

```bash
python -m venv venv
```
This creates a local environment folder.

---

## Activating the Environment
On Windows (Git Bash / PowerShell):

```bash
source venv/Scripts/activate
```

On macOS / Linux:
```bash
source venv/bin/activate
```
When activated:
- `python` points to the environment
- `pip` installs locally
---

## How to Know You’re Inside a venv

Indicators:
- (venv) appears in terminal
- which python / where python changes
- Installed packages differ

If unsure, check before installing anything.
---

Mental Rule

> If you didn’t activate a virtual environment,
> you probably shouldn’t install packages.
---

## What to Do Today
1. Run the script without a virtual environment:
```bash
python code/demo.py
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Run the script again
4. Observe how `sys.executable` changes

This makes isolation **visible**, not theoretical.
