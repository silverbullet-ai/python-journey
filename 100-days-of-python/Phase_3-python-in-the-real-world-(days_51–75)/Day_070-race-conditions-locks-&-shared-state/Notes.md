# Day 70 Notes — Race Conditions & Locks

## What Is a Race Condition?

A race condition occurs when:
- Multiple threads access shared data
- At least one thread modifies it
- The outcome depends on timing

Timing is not a contract.

---

## Why Race Conditions Are Dangerous

Race conditions:
- Are intermittent
- Are hard to reproduce
- Disappear during debugging
- Cause corrupted state

The worst bugs are nondeterministic.

---

## Shared State Is the Root Problem

Shared mutable state includes:
- Global variables
- Shared objects
- Shared counters
- Shared collections

The more sharing, the more danger.

---

## What Locks Do

A lock:
- Allows only one thread to enter a critical section
- Protects shared data from concurrent modification

Locks enforce **mutual exclusion**, not correctness.

---

## Using Locks Correctly

Rules:
- Lock the smallest possible critical section
- Always release locks
- Prefer context managers (`with lock:`)

Avoid:
- Locking everything
- Nested locks
- Complex lock hierarchies

---

## Why Locks Are a Last Resort

Locks:
- Reduce concurrency
- Introduce deadlocks
- Increase complexity

Best solution:
> Avoid shared state entirely when possible.

---

## Mental Rules (Lock These In)

> If state is shared → danger exists  
> If locks are complex → design is wrong  
> Simpler concurrency beats clever concurrency

---

### Why `time.sleep(0)` Is Used in Examples

`time.sleep(0)` does not slow execution meaningfully.
It yields control to the thread scheduler, increasing the
chance of context switches.

This is used intentionally in examples to make race
conditions reproducible on fast systems.

Real race conditions exist even without sleep —
they are just harder to observe.

