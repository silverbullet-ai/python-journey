# Day 0 Notes — Orientation & Setup

## What is Python?

Python is a **high-level, interpreted, general-purpose programming language** known for its readability and simplicity.

It allows developers to focus on **problem solving** rather than syntax complexity.

---

## Brief History of Python

- Created by **Guido van Rossum**
- Development started in **December 1989**
- First official release: **Python 0.9.0 (February 1991)**
- Python 2.0 released in **2000**
- Python 3.0 released in **2008** (major improvements & not backward compatible with Python 2)
- Python is now maintained by the **Python Software Foundation (PSF)**

Python was designed to be:
- Simple
- Readable
- Powerful
- Extensible

---

## How Python Works (High Level)

1. You write Python code (`.py` file)
2. The Python interpreter reads the code
3. Code is converted into **bytecode**
4. Bytecode runs on the **Python Virtual Machine (PVM)**

Unlike C/C++, Python does **not require manual compilation**.

---

## Installing Python

### Step 1: Go to Official Website

Download from:

👉 https://www.python.org/downloads/

Choose the latest stable version.

---

### Step 2: Install

#### On Windows:
- Download installer
- ✔ Check **"Add Python to PATH"**
- Click Install

#### On macOS:
- Download `.pkg` installer
- Follow installation steps

#### On Linux:
Python is usually pre-installed.
If not:

```bash
sudo apt update
sudo apt install python3
```

---

## Verify Installation (Important)

Open terminal / command prompt and run:

```bash
python --version
```

or

```bash
python3 --version
```

If installed correctly, it will show something like:

```
Python 3.x.x
```
---

## Running a Python Script from Terminal

### Step 1: Create a file

Example:

```python
# day0.py
print("Hello, Python!")
```

### Step 2: Run it  

`python filename.py`

```bash
python day0.py
```

or

```bash
python3 day0.py
```

---

## Learning Mindset for This Journey

- Consistency > Intensity  
- Understanding > Memorizing  
- Clean code > Clever code  
- Patience is non-negotiable  

---

## Day 0 Success Criteria

Day 0 is successful if:

- Python is installed
- Version check works
- A script runs from terminal
- Mindset is clear
