# Day 73 Notes — asyncio Basics

## Running Async Code

Async code does not run by itself.
It must be executed by an **event loop**.

In modern Python:
```python
asyncio.run(main())
```

This:
- Creates the event loop
- Runs the coroutine
- Closes the loop cleanly

---

## async def vs def

```python
def normal_function():
    ...
```

```python
async def async_function():
    ...
```

- `def` → executes immediately
- `async def` → returns a coroutine
- A coroutine must be awaited

---

## await (Revisited)

`await`:
- Pauses the current coroutine
- Lets the event loop run other tasks
- Resumes when the awaited operation completes

If there is no `await`,
async code behaves like normal code.

---

## Running Tasks Concurrently

To run multiple async tasks together:
```python
await asyncio.gather(task1(), task2())
```

They:
- Start together
- Yield on await points
- Complete independently

---

## async Is Still Single-Threaded

Important reminder:
- Async runs on one thread
- Concurrency comes from waiting, not parallelism

---

## Mental Rule

> async without await is just syntax  
> await is where concurrency happens
