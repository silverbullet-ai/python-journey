# Day 82 Notes — Logging Fundamentals

## Why print() Is Not Logging

print():
- Has no severity level
- Cannot be filtered easily
- Mixes debugging with program output
- Is hard to manage at scale

Logging exists to provide:
- Structured visibility
- Severity classification
- Configurable output
- Long-term diagnostics

---

## What Logging Is Really For

Logging answers questions like:
- What happened?
- When did it happen?
- How often does it happen?
- In what order did events occur?

Logs are for:
- Developers
- Operators
- Future debugging

They are not user messages.

---

## Logging Levels (Mental Model)

Common levels:
- DEBUG → Detailed internal state
- INFO → Normal operation milestones
- WARNING → Unexpected but recoverable situations
- ERROR → Failures that affect functionality
- CRITICAL → System is unusable

Rule of thumb:
Severity reflects **impact**, not emotion.

---

## What Makes a Good Log Message

Good logs are:
- Specific
- Context-rich
- Actionable

Bad logs are:
- Vague
- Emotional
- Redundant

Logs should explain *what happened*, not *how you feel*.

---

## Logging as Design

Where you place logs matters.

Log:
- State transitions
- Important decisions
- Errors with context

Do not log:
- Every line
- Obvious control flow
- Sensitive data

---

## Mental Rule

> If you had only logs,
> could you understand what happened?

If not, logging is insufficient.
