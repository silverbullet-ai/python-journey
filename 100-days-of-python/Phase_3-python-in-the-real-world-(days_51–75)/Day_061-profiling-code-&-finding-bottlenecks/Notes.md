# Day 61 Notes — Profiling & Bottlenecks

## What Is Profiling?

Profiling answers:
- Which functions run the most?
- Which functions take the most time?
- Where is the program actually slow?

Profiling is **measurement with context**.

---

## Why Guessing Is Dangerous

Without profiling:
- You optimize the wrong code
- You add complexity needlessly
- You miss real bottlenecks

With profiling:
- You see reality
- You optimize only what matters

---

## The 80/20 Rule (Very Important)

In most programs:
- 80% of time is spent in
- 20% of the code

Profiling helps you find that 20%.

---

## What cProfile Shows

Key columns:
- ncalls → number of calls
- tottime → time spent in function itself
- cumtime → time including called functions

Focus on:
- High cumtime
- High call counts

---

## Mental Rule

> Never optimize code you haven’t profiled.
