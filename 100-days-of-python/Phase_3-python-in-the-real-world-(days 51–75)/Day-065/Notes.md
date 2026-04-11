# Day 65 Notes — Caching & Memoization

## What Is Caching?

Caching means:
- Storing results of expensive operations
- Reusing them instead of recomputing

It trades:
- More memory → less computation

---

## What Is Memoization?

Memoization is:
- A specific type of caching
- Applied to pure functions
- Based on function inputs

Same input → same output → safe to cache.

---

## When Caching Helps

Caching helps when:
- Function is expensive
- Function is called repeatedly
- Inputs repeat
- Output is deterministic

Examples:
- Recursive computations
- Parsing
- Configuration lookups

---

## When Caching Hurts

Caching hurts when:
- Inputs are unbounded
- Data grows indefinitely
- Results are large
- Cache is never cleared

This leads to:
- Memory bloat
- Slower systems
- Crashes over time

---

## lru_cache (Important)

`lru_cache`:
- Automatically caches results
- Evicts least-recently-used entries
- Prevents unbounded growth (if maxsize is set)

Never use it without thinking about `maxsize`.

---

## Mental Rule

> Cache what repeats.
> Limit what grows.
