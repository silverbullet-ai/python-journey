# Day 69 Notes — Threads in Python

## What Threads Actually Do in Python

Threads allow:
- Multiple tasks to make progress
- While others are waiting (I/O)

They do NOT:
- Run Python bytecode in parallel (in default CPython)
- Speed up CPU-heavy computation

---

## When Threads Help

Threads are ideal for:
- Network requests
- File I/O
- Sleeping / waiting
- User input
- External APIs

In these cases, threads improve **responsiveness and throughput**.

---

## When Threads Hurt

Threads hurt when:
- Tasks are CPU-bound
- Shared state is mutated carelessly
- Synchronization is ignored

More threads ≠ more speed.

---


## I/O-Bound vs CPU-Bound Tasks (Concrete Examples)

Understanding this distinction is critical for using threads correctly.

---

## I/O-Bound Tasks (Threads Help)

I/O-bound tasks spend most of their time **waiting**, not computing.

Examples:
- Network requests (API calls, HTTP requests)
- Reading or writing files
- Database queries
- Waiting for user input
- Sleeping or timers (`time.sleep`)
- Calling external services

Characteristics:
- CPU is mostly idle
- Threads can overlap waiting time
- Concurrency improves responsiveness and throughput

Threads are a good fit here.

---

## CPU-Bound Tasks (Threads Don’t Help)

CPU-bound tasks spend most of their time **actively computing**.

Examples:
- Large mathematical calculations
- Image or video processing
- Data compression or encryption
- Machine learning computations
- Parsing or transforming large datasets
- Heavy loops doing pure Python work

Characteristics:
- CPU is fully utilized
- GIL prevents true parallel execution (in default CPython)
- More threads do not reduce execution time

Threads are usually the wrong tool here.

---

## Practical Rule of Thumb

> If the task waits on something external → it is I/O-bound  
> If the task keeps the CPU busy → it is CPU-bound

Choose concurrency tools based on this distinction.

---

## The GIL Reminder

Because of the GIL:
- Only one thread executes Python bytecode at a time
- Threads interleave execution, they don’t parallelize computation

This is fine for I/O-bound workloads.

---

## Thread Lifecycle (Simple)

1. Create thread
2. Start thread
3. Thread runs independently
4. Join thread (wait for completion)

Always join unless you *explicitly* want background behavior.

---

## Mental Rules

> Use threads to **wait better**, not compute faster.  
> If code waits → threads help.  
> If code computes → threads don’t.

Correct expectations prevent bugs.
