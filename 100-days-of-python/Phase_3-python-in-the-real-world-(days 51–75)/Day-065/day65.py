# Day 65 — Caching & Memoization

import time
from functools import lru_cache


def slow_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


@lru_cache(maxsize=128)
def cached_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return cached_fibonacci(n - 1) + cached_fibonacci(n - 2)


def main():
    n = 35

    print("Calculating without caching...")
    start = time.time()
    result = slow_fibonacci(n)
    end = time.time()
    print(f"Result: {result}, Time: {end - start:.4f}s")

    print("\nCalculating with caching...")
    start = time.time()
    result = cached_fibonacci(n)
    end = time.time()
    print(f"Result: {result}, Time: {end - start:.4f}s")


if __name__ == "__main__":
    main()

print("\nDay 65 completed successfully!")
