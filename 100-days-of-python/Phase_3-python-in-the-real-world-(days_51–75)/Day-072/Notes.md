# Day 72 Notes — Async / Await Mental Models

## What Async Really Is

Async is:
- Single-threaded
- Non-blocking
- Cooperative concurrency

Tasks **voluntarily yield control** when they wait.

This is very different from threads.

---

## The Core Idea (One Sentence)

> Async lets one thread manage many waiting tasks
> without blocking on any single one.

---

## Async vs Threads (Big Picture)

### Threads
- OS-managed
- Preemptive (can be interrupted)
- Shared memory
- Need locks
- Harder to reason about

### Async
- Event-loop managed
- Cooperative (tasks yield explicitly)
- No shared-state concurrency
- No locks needed (usually)
- Easier to reason about

---

## The Event Loop (Conceptual)

Think of the event loop as:
- A scheduler
- That runs one task at a time
- Switches tasks only when they **await**

Flow:
1. Task runs
2. Task hits `await` (I/O, sleep, etc.)
3. Task pauses
4. Event loop runs another ready task
5. Paused task resumes later

No task is interrupted mid-execution.

---

## What `async` Means

```python
async def fetch_data():
    ...
```

Means:
- This function returns a **coroutine**
- It does not run immediately
- It must be scheduled by the event loop

---

## What `await` Means

```python
await some_io()
```

Means:
- “Pause here”
- “Let the event loop run something else”
- “Resume me when this is ready”

This is **explicit yielding**.

---

## When Async Is a Great Fit

Async shines when:
- Tasks are I/O-bound
- Many concurrent waits exist
- You want high throughput
- You want to avoid threads and locks

Examples:
- Web servers
- API clients
- Chat systems
- Network services

---

## When Async Is the Wrong Tool

Async is bad when:
- Tasks are CPU-bound
- Libraries are blocking
- Codebase is small/simple
- You need parallel computation

Async does NOT make CPU work faster.

---

## Async Is Not Magic

Async does NOT:
- Use multiple cores
- Run code in parallel
- Replace multiprocessing

It replaces **waiting inefficiency**, not computation.

---

## Mental Rules (Lock These In)

> If tasks wait → async fits  
> If tasks compute → async doesn’t help  

> Async avoids locks by avoiding shared state  
> Cooperative beats preemptive for clarity
