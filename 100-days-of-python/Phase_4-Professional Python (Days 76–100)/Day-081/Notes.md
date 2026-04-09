# Day 81 Notes — Debugging Mindset & Reading Tracebacks

## Debugging Is Not Guessing

Debugging is:
- Observation
- Reasoning
- Verification

Debugging is NOT:
- Random changes
- Trial-and-error fixes
- Blind copying from the internet

Professionals debug deliberately.

---

## What a Traceback Really Is

A traceback is:
- A record of function calls
- Showing how execution reached a failure
- Ordered from oldest call to newest

The most important line is usually:
- The **last line**
- The exception type and message

But the cause often lies earlier.

---

## How to Read a Traceback (Step-by-Step)

1. Read the **exception type**
2. Read the **error message**
3. Identify the **file and line number**
4. Walk upward through the call stack
5. Locate where incorrect data was introduced

Never fix symptoms.
Fix causes.

---

## Common Beginner Mistakes

- Only reading the last line
- Ignoring stack context
- Catching exceptions too early
- Adding prints without understanding flow

Tracebacks are information, not noise.

---

## Debugging Mental Model

Ask in order:
1. What failed?
2. Where did it fail?
3. Why did it fail?
4. What assumption was wrong?

Every bug is a broken assumption.

---

## Key Rule

> The first explanation you think of
> is usually wrong.

Slow down. Read the traceback.

---

## What to Do Today

1. Run the file:
```bash
python code/buggy_service.py
```
2. Observe the traceback carefully
3. Do not fix it immediately
4. Answer for yourself:
	- What is the exception?
	- Where does it occur?
	- Why does it occur?
	- Which assumption failed?

The fix is trivial.
The **understanding** is not.
