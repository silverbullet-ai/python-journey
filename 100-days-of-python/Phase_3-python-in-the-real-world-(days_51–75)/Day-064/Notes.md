# Day 64 Notes — Memory Thinking & Space Complexity

## What Is Space Complexity?

Space complexity describes:
- How memory usage grows
- As input size grows

Just like time complexity,
memory usage can scale poorly.

---

## Why Memory Matters

Memory problems cause:
- Slowdowns due to swapping
- Crashes (OutOfMemory)
- Unpredictable behavior
- Poor scalability

Fast code that eats memory is dangerous.

---

## Time vs Space Trade-Off

You often trade:
- More memory → faster execution
- Less memory → slower execution

Neither is always correct.
Context decides.

---

## Common Hidden Memory Costs

- Creating large intermediate lists
- Caching without limits
- Copying data unnecessarily
- Holding references longer than needed

Python makes memory easy to allocate —
and easy to forget.

---

## Generators vs Lists (Important)

Lists:
- Store all values in memory

Generators:
- Produce values on demand
- Use far less memory

---

## Mental Rule

> If data doesn’t need to exist all at once,
> don’t store it all at once.
