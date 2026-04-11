# Day 53 Notes — Logging vs Print & Professional Debugging

## Why print() Is Not Debugging

print():
- Is temporary
- Has no severity
- Cannot be filtered
- Cannot be disabled cleanly
- Pollutes output

It answers only one question:
“What is this value right now?”

---

## What Is Logging?

Logging is a structured way for a program to:
- Report its state
- Explain decisions
- Surface failures
- Leave a trace of execution

Logging is **not** for developers only —  
it is for operators, debuggers, and future you.

---

## Logging Levels (Very Important)

### DEBUG
- Detailed internal information
- Used during development

### INFO
- Normal, expected events
- Program milestones

### WARNING
- Something unexpected, but recoverable

### ERROR
- A failure occurred
- Program may continue

### CRITICAL
- Program cannot continue safely

---

## Mental Model

> print() asks:
> “What is happening right now?”

> logging asks:
> “What should be remembered about this run?”

---

## Logging Discipline

- Log **events**, not values blindly
- Do not log everything
- Each log message should have intent
- Logs are part of your program’s API

---

## Mental Rule

> If an issue happens in production,
> logs are all you have.
