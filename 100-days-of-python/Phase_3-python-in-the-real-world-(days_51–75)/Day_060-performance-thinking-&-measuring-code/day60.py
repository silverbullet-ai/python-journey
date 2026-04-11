# Day 60 — Performance Thinking & Measuring Code

import time
import timeit


def slow_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


def fast_sum(n: int) -> int:
    return sum(range(n))


def measure_with_time():
    start = time.time()
    slow_sum(10_000_000)
    end = time.time()
    print(f"slow_sum time: {end - start:.4f} seconds")

    start = time.time()
    fast_sum(10_000_000)
    end = time.time()
    print(f"fast_sum time: {end - start:.4f} seconds")


def measure_with_timeit():
    slow_time = timeit.timeit(
        stmt="slow_sum(10_000_000)",
        globals=globals(),
        number=1
    )

    fast_time = timeit.timeit(
        stmt="fast_sum(10_000_000)",
        globals=globals(),
        number=1
    )

    print(f"[timeit] slow_sum: {slow_time:.4f} seconds")
    print(f"[timeit] fast_sum: {fast_time:.4f} seconds")


def main():
    print("Measuring with time.time()")
    measure_with_time()

    print("\nMeasuring with timeit")
    measure_with_timeit()


if __name__ == "__main__":
    main()

print("\nDay 60 completed successfully!")
