# Day 64 — Memory Thinking & Space Complexity

import sys


def list_based_sum(n: int) -> int:
    numbers = list(range(n))  # stores all numbers in memory
    return sum(numbers)


def generator_based_sum(n: int) -> int:
    numbers = (i for i in range(n))  # generates values on demand
    return sum(numbers)


def main():
    n = 1_000_000

    list_numbers = list(range(n))
    generator_numbers = (i for i in range(n))

    print(f"List size in memory: {sys.getsizeof(list_numbers)} bytes")
    print(f"Generator size in memory: {sys.getsizeof(generator_numbers)} bytes")

    print("\nComputing sums:")
    print("List-based sum:", list_based_sum(n))
    print("Generator-based sum:", generator_based_sum(n))


if __name__ == "__main__":
    main()

print("\nDay 64 completed successfully!")
