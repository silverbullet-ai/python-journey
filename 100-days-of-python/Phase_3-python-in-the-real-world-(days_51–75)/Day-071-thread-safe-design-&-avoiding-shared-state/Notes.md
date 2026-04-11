# Day 71 Notes — Thread-Safe Design

## The Root Cause of Concurrency Bugs

Most concurrency bugs come from:
- Shared
- Mutable
- State

Remove one of these, and the problem largely disappears.

---

## Strategy 1: Avoid Shared State

Best solution:
- Don’t share mutable data
- Give each thread its own data
- Combine results afterward

No locks needed.

---

## Strategy 2: Message Passing (Preferred)

Threads communicate by:
- Sending messages
- Not touching each other’s state

This is safer because:
- Ownership is clear
- No race conditions
- Easier reasoning

Queues are the most common tool.

---

## Strategy 3: Immutable Data

Immutable data:
- Cannot be changed after creation
- Is safe to share freely
- Eliminates synchronization needs

Examples:
- Tuples instead of lists
- Frozen dataclasses
- Read-only objects

---

## Locks as a Last Resort

Locks:
- Are sometimes necessary
- Increase complexity
- Reduce scalability

Use them only when:
- Shared state is unavoidable
- Critical sections are tiny
- Alternatives are worse

---

## Mental Rules (Lock These In)

> Prefer isolation over synchronization  
> Prefer messages over shared memory  
> Prefer immutability over locks  

Design beats defense.
