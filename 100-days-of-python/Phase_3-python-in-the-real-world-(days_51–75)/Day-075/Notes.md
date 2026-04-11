# Day 75 Notes — Choosing the Right Concurrency Model

## The Core Question

Concurrency is not about speed.
It is about **structure**.

Before writing code, ask:
- Does this task wait?
- Does it compute?
- Does it scale?
- Does it share state?

---

## Concurrency Models (When to Use What)

### 1. Synchronous (Plain Code)
Use when:
- Tasks are simple
- Performance is acceptable
- Complexity is unnecessary

Default choice until proven otherwise.

---

### 2. Threads
Use when:
- Tasks are I/O-bound
- Libraries are blocking
- Async alternatives don’t exist

Avoid for CPU-heavy work.

---

### 3. Async (async / await)
Use when:
- Many I/O-bound tasks
- Async-friendly libraries
- High concurrency
- Clear control flow

Avoid mixing blocking calls.

---

### 4. Multiprocessing
Use when:
- CPU-bound workloads
- Heavy computation
- True parallelism needed

Trade-off: higher memory & complexity.

---

## Combining Models (Advanced)

Common real-world pattern:
- Async for orchestration
- Threads for blocking I/O
- Processes for CPU-heavy tasks

Good design isolates concerns.

---

## Final Mental Model (Lock This In)

> Choose the simplest model that satisfies correctness,
> then scale deliberately.

Concurrency is a **design decision**, not a feature.
