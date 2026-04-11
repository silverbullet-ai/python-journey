# Day 89 Notes — Installing Your Own Package

## Why Installation Is Required

Python does not automatically know about your project.
It only searches:
- Installed packages
- The current working directory
- Explicitly configured paths

A well-structured package still must be installed
to be importable reliably.

---

## What `pip install -e .` Means

Editable install:
- Installs the package in "editable" mode
- Links the installed package to your source code
- Allows changes without reinstalling

This is how professionals work during development.

---

## Why Editable Installs Are Important

Editable installs:
- Prevent import hacks
- Ensure correct package resolution
- Mimic production behavior during development

Without this:
- Imports may work accidentally
- Tests may import the wrong code
- Bugs appear later in CI or deployment

---

## How pip Finds Your Package

When you run:
```bash
pip install -e .
```

pip:
- Reads `pyproject.toml`
- Discovers the package under `src/`
- Registers it as an installed package

After this, Python knows where your code lives.

---

## Mental Rule
> If code is meant to be imported,
> it should be installed—even locally.
---

## What to Do Today
0. Create a Virtual Environment
```bash
python -m venv venv
```
1. Activate your virtual environment
```bash
source venv/Scripts/activate
```

2. Install your package in editable mode
```bash
pip install -e .
```
You should see output indicating:
- The package was installed
- No errors occurred

3. Start Python (Git Bash)
```bash
winpty python
```

4. Test the import
```python
from sample_pkg.core import greet
greet("Aahish")
```
Expected output:
```text
'Hello, Aahish!'
```

5. Prove it’s editable

Edit `core.py`:
```python
return f"Hi, {name}!!!"
```
Run again in the same REPL:
```python
greet("Aahish")
```

You should see the updated output without reinstalling.

That’s editable install working.
