# Day 84 Notes — Error Handling as Design

## Errors Are Not Accidents

In professional systems:
- Errors are expected
- Failures are inevitable
- Handling them is a design responsibility

Ignoring errors does not make systems stable.
Designing for them does.

---

## Exceptions vs Control Flow

Exceptions are for:
- Invalid states
- Broken assumptions
- Situations the program cannot proceed from normally

Exceptions are NOT for:
- Regular branching logic
- Expected alternate paths

Using exceptions incorrectly makes code harder to reason about.

---

## What Makes a Good Exception

A good exception:
- Clearly explains what went wrong
- Provides enough context
- Is specific, not generic

Bad exceptions:
- Hide the real cause
- Swallow important information
- Are caught too early

---

## Catch Late, Not Early

Rule of thumb:
- Raise exceptions where the problem occurs
- Catch exceptions where you can handle them meaningfully

Catching too early:
- Loses context
- Hides bugs
- Creates false stability

---

## Designing Failure Paths

Ask:
- What can fail here?
- Can the program recover?
- Who should handle this failure?

Every failure path should be:
- Intentional
- Visible
- Documented through behavior

---

## Mental Rule

> A system that fails loudly and clearly
> is easier to trust than one that fails silently.
