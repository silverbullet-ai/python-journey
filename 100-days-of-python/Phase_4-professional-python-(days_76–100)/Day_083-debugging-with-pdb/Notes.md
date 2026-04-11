# Day 83 Notes — Debugging with pdb

## Why Interactive Debugging Exists

Sometimes:
- Logs are insufficient
- Tracebacks are not enough
- You need to inspect live state

Interactive debugging allows you to:
- Pause execution
- Inspect variables
- Control program flow

---

## What pdb Is

pdb is:
- Python’s built-in debugger
- Interactive and stateful
- Designed for investigation, not speed

It allows you to ask:
“What is the program thinking right now?”

---

## How Debugging with pdb Works

You:
- Insert a breakpoint
- Run the program
- Interact with execution
- Step line by line

This reveals:
- Actual values
- Control flow decisions
- Broken assumptions

---

## Common pdb Commands

- `l` → show current code
- `n` → execute next line
- `s` → step into function
- `c` → continue execution
- `p <var>` → print variable value
- `q` → quit debugger

You don’t need all of them.
You need to use them intentionally.

---

## When to Use pdb (and When Not To)

Use pdb when:
- Behavior is unclear
- State matters
- Logs would be too noisy

Avoid pdb when:
- Debugging trivial mistakes
- You already know the cause
- You can reason it out faster

---

## Debugging Mental Rule

> Observe before modifying.

The debugger is a microscope,
not a hammer.

---

## What to Do Today

1. Run the program:
```bash
python code/debug_app.py
```
2. Execution will pause at pdb.set_trace()
3. Use:
	- `l` to view code
	- `p price`, `p discount`
	- `n` and `s` to step
4. Observe how data flows
5. Quit with `q`

---

## `n` — next line

Use `n` when:
- You trust the function being called
- You don’t care about its internal logic
- You only want to see what happens after

## `s` — step into

Use `s` when:
- You don’t trust the function
- You want to see how values change inside it
- The bug might be inside the called function
