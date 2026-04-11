# Day 66 — Itertools, Efficient Loops & Lazy Computation

import time
import sys
from itertools import islice, chain


def eager_processing(n: int):
    data = list(range(n))
    processed = [x * 2 for x in data if x % 2 == 0]
    return processed


def lazy_processing(n: int):
    data = range(n)
    processed = (x * 2 for x in data if x % 2 == 0)
    return processed


def main():
    n = 1_000_000

    print("Eager processing:")
    start = time.time()
    eager = eager_processing(n)
    end = time.time()
    print(f"Time: {end - start:.4f}s")
    print(f"Memory size: {sys.getsizeof(eager)} bytes")

    print("\nLazy processing (first 10 values):")
    start = time.time()
    lazy = lazy_processing(n)
    first_ten = list(islice(lazy, 10))
    end = time.time()
    print(f"Time: {end - start:.4f}s")
    print(f"Memory size (iterator): {sys.getsizeof(lazy)} bytes")
    print("First 10 values:", first_ten)

    print("\nChaining iterables lazily:")
    combined = chain(range(5), range(5, 10))
    print(list(combined))


if __name__ == "__main__":
    main()

print("\nDay 66 completed successfully!")
