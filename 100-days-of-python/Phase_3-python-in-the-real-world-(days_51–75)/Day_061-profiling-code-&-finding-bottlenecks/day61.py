# Day 61 — Profiling Code & Finding Bottlenecks

import cProfile


def slow_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total


def medium_function():
    return slow_function()


def fast_function():
    return sum(range(1_000_000))


def main():
    medium_function()
    fast_function()


if __name__ == "__main__":
    # Profile the main function
    cProfile.run("main()")

print("\nDay 61 completed successfully!")
