# Day 68 Notes — Concurrency vs Parallelism

## First: The Core Difference (Memorize This)

Concurrency:
- Managing multiple tasks
- Making progress on more than one task
- Not necessarily at the same time

Parallelism:
- Executing multiple tasks
- Literally at the same time
- Requires multiple CPU cores

They are related — but not the same.

---

## Simple Analogy (Very Important)

### Concurrency
You are cooking:
- You boil water
- While it boils, you chop vegetables
- While chopping, you check the oven

You are not doing all tasks at once,
but you are **not blocked by waiting**.

---

### Parallelism
You and a friend:
- You chop vegetables
- Your friend prepares sauce
- Both at the same time

Work is **physically divided**.

---

## What Concurrency Solves

Concurrency helps when:
- Tasks spend time waiting
- I/O is slow (network, disk, sleep)
- You want responsiveness

Concurrency improves **throughput**, not raw speed.

---

## What Parallelism Solves

Parallelism helps when:
- Tasks are CPU-heavy
- Work can be split
- You want faster computation

Parallelism improves **raw execution time**.

---

## Python’s Reality (Important)

Python (CPython):
- Has the GIL (Global Interpreter Lock)
- Allows only one thread to execute Python bytecode at a time

This means:
- Threads → good for I/O-bound tasks
- Threads → NOT good for CPU-bound parallelism

Parallelism in Python usually requires:
- Multiple processes
- Not threads

---

## Why This Matters Before Coding

Using the wrong model leads to:
- Slower programs
- More complexity
- False expectations
- Debugging nightmares

Correct model first.
Tool second.

---

## Mental Rules (Lock These In)

> If tasks wait → think concurrency  
> If tasks compute → think parallelism  

> Threads help waiting.  
> Processes help computing.

---

## What Comes Next

Now that the mental model is clear,
we can safely learn:
- Threads
- Async
- Multiprocessing

Without confusion.

---

## The GIL Today & the Road Ahead (Important Clarification)

Historically, Python (CPython) uses the **Global Interpreter Lock (GIL)**,
which allows only one thread to execute Python bytecode at a time.

This affects **CPU-bound parallelism**, not I/O-bound concurrency.

---

## Recent Developments (Python 3.13+)

Python has begun a **transition toward a GIL-optional future**:

- PEP 703 introduced **free-threaded Python**
- Python now ships with:
  - A **GIL-enabled build** (default, stable)
  - A **free-threaded build** (experimental, opt-in)

Important:
- The GIL is **not removed by default**
- The ecosystem is still adapting
- Many C extensions assume the GIL exists

---

## What This Means in Practice

As of today and the near future:
- Threads are still best for **I/O-bound concurrency**
- CPU-bound parallelism still prefers **multiprocessing**
- Design decisions still matter more than runtime details

The mental models learned today remain valid.

---

## Key Insight

> The GIL is being *relaxed*, not erased.
> Correct concurrency thinking outlives implementation details.

Understanding concurrency vs parallelism is still essential,
even in a future without the GIL.

