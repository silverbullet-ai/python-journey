# Day 87 Notes — Dependency Management

## Why Dependency Management Exists

Python projects depend on external libraries.
Without control:
- Versions drift
- Bugs appear unexpectedly
- Code works on one machine but not another

Dependency management exists to make projects reproducible.

---

## What pip Really Does

pip:
- Installs packages from PyPI
- Resolves dependencies
- Places them into the active environment

pip does NOT:
- Guarantee future compatibility
- Protect you from breaking updates

That responsibility is yours.

---

## Why requirements.txt Matters

requirements.txt:
- Lists exact dependencies
- Documents what the project needs
- Allows others to recreate the same environment

Without it:
- Setup becomes guesswork
- Bugs become unreproducible

---

## Creating requirements.txt

After installing packages:

```bash
pip freeze > requirements.txt
```
This records:
- Package names
- Exact versions

Exact versions matter for stability.

---

## Installing From requirements.txt

On a fresh environment:
```bash
pip install -r requirements.txt
```
This recreates the dependency set reliably.

---

## Version Pinning (Important Concept)

Pinning versions:
- Prevents accidental breaking changes
- Improves reproducibility
- Makes bugs traceable

Unpinned dependencies introduce uncertainty.
---

## Mental Rule

> If you cannot recreate the environment,
> you cannot reliably debug the project.
---

## What to Do Today
0. Create a Virtual Environment
```bash
python -m venv venv
```
1. Activate your virtual environment:
```bash
source venv/Scripts/activate
```
2. Install dependency:
```bash
pip install requests
```
3. Generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```
4. Run the program:
```bash
python code/demo.py
```
5. (Optional) Create a fresh venv and reinstall using:
```bash
pip install -r requirements.txt
```

Observe how dependencies become explicit and repeatable.
