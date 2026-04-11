# Day 67 — Generators in the Real World (Pipelines & Streaming)

import time


def source():
    """Simulates a data source"""
    for i in range(1_000_000):
        yield i


def filter_even(numbers):
    """Filters even numbers"""
    for n in numbers:
        if n % 2 == 0:
            yield n


def transform_square(numbers):
    """Squares numbers"""
    for n in numbers:
        yield n * n


def sink(numbers, limit=10):
    """Consumes and processes final output"""
    for i, value in enumerate(numbers):
        print(value)
        if i + 1 == limit:
            break


def main():
    pipeline = transform_square(
        filter_even(
            source()
        )
    )

    sink(pipeline)


if __name__ == "__main__":
    main()

print("\nDay 67 completed successfully!")
