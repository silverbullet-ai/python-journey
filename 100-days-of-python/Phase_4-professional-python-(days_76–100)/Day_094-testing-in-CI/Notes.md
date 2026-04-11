# Day 94 Notes — Testing in CI

## What CI Does With Tests

In CI, tests are not optional.
They are **gates**.

If tests fail:
- The change does not proceed
- The system is considered unsafe
- Human judgment is deferred

CI answers:
“Is this change allowed to move forward?”

---

## Why Failing Fast Matters

Failing fast means:
- Problems are detected immediately
- Context is fresh
- Fixes are cheaper

Late failures:
- Waste time
- Increase risk
- Hide responsibility

CI exists to fail early, not politely.

---

## Red Builds Are Signals, Not Punishments

A red build means:
- Something changed
- The system no longer meets expectations

It is not:
- A personal failure
- A reason to panic
- A reason to bypass tests

Red builds demand attention, not blame.

---

## Tests as Quality Gates

In CI:
- Unit tests protect logic
- Integration tests protect wiring
- Both must pass

If tests are flaky or weak,
CI loses trust.

Strong tests make CI meaningful.

---

## Common CI Mistakes

- Disabling tests to “unblock” work
- Ignoring failing builds
- Treating warnings as noise
- Overloading pipelines with slow tests

CI should be:
- Fast
- Deterministic
- Trusted

---

## Mental Rule

> If CI is red and you ignore it,
> you are choosing risk intentionally.

---

## What to Do Today
1. Read the notes carefully
2. Reflect on:
	- What would break your CI today?
	- Are your tests fast and reliable?
3. Do not configure GitHub Actions yet

Understanding the gate comes before building it.


