# Day 95 Notes — Quality Gates

## What a Quality Gate Is

A quality gate is a rule that says:
“This change cannot proceed unless conditions are met.”

Quality gates:
- Are enforced automatically
- Apply to everyone equally
- Remove ambiguity from decisions

They turn standards into behavior.

---

## Common Quality Gates in Python Projects

Typical gates include:
- All tests pass
- No failing linters
- No critical warnings
- Build completes successfully

Not every project needs every gate.
But every project needs clarity.

---

## Why Quality Gates Matter

Without gates:
- Standards drift
- Risk accumulates
- Responsibility becomes unclear

With gates:
- Expectations are explicit
- Failures are immediate
- Trust increases over time

Gates protect the system from gradual decay.

---

## Tests vs Gates (Important Distinction)

Tests:
- Verify behavior

Quality gates:
- Decide whether behavior is acceptable to merge or release

A test can pass,
and still fail a quality gate
if broader standards aren’t met.

---

## Choosing the Right Gates

Ask:
- What failures are unacceptable?
- What signals indicate risk?
- What can be automated reliably?

Avoid gates that:
- Are flaky
- Are slow
- Produce false positives

A bad gate erodes trust.

---

## Failing Fast with Confidence

Failing fast works only if:
- Failures are meaningful
- Signals are trusted
- Fixing is prioritized

If failures are ignored,
the gate no longer exists.

---

## Mental Rule

> If a rule matters,
> enforce it automatically.

---

## What to Do Today
1. Reflect on your Phase 4 work:
	- What would you gate today?
	- What would you allow through?

2. Think in terms of policy, not tools

3. Do not add new automation yet

This day is about **deciding standards**, not wiring them.
