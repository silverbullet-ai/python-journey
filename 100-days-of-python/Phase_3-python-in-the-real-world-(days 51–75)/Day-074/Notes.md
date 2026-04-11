# Day 74 Notes — Async Pitfalls & Patterns

## The #1 Async Mistake

Using **blocking code** inside async functions.

Async only works if:
- Tasks yield control
- The event loop can switch tasks

Blocking breaks both.

---

## Blocking Calls (Danger Zone)

These calls **block the event loop**:

- `time.sleep()`
- Blocking file I/O
- Blocking network requests
- Heavy CPU computation
- Long loops without `await`

They freeze *all* async tasks.

---

## Bad Example (Looks Async, Isn’t)

```python
async def bad_task():
    time.sleep(2)  # Blocks event loop
```

This turns async into synchronous code.

---

## Correct Async Alternatives

Use non-blocking equivalents:

- `time.sleep()` → `await asyncio.sleep()`
- Blocking HTTP → async HTTP client
- Blocking DB calls → async DB drivers

Async requires async-friendly libraries.

---

## Async Can Silently Become Sync

Warning signs:
- Tasks run one after another
- Total time equals sum of waits
- No interleaving output
- High CPU usage in async code

Async syntax ≠ async behavior.

---

## CPU-Bound Work in Async

Async does NOT help with CPU-heavy work.

Options:
- Offload to thread pool
- Offload to process pool
- Redesign workload

Async event loops must stay **lightweight**.

---

## Safe Async Patterns

Good async code:
- Has frequent `await` points
- Keeps tasks short
- Delegates heavy work
- Uses async-native libraries

---

## Mental Rules (Lock These In)

> If it blocks → it breaks async  
> Async must stay non-blocking  
> Event loop health comes first
