# Day 62 Notes — Algorithmic Thinking & Big-O

## What Big-O Really Means

Big-O describes:
- How execution time grows
- As input size grows

It ignores:
- Hardware
- Language speed
- Minor constants

Big-O is about **scaling behavior**.

---

## Why Algorithms Matter More Than Code Tricks

A faster algorithm beats:
- Better syntax
- Micro-optimizations
- Clever hacks

Example:
O(n) will always beat O(n²) at scale.

---

## Common Complexity Patterns (Practical View)

- O(1) → Constant time
- O(n) → Linear scan
- O(n²) → Nested loops
- O(log n) → Divide and conquer

You don’t need math.
You need **pattern recognition**.

---

## Design vs Optimization

If code is slow because:
- Wrong algorithm → redesign
- Right algorithm → optimize hot paths

Never optimize bad design.

---

## Mental Rule

> If performance degrades sharply as data grows,
> suspect the algorithm first.
