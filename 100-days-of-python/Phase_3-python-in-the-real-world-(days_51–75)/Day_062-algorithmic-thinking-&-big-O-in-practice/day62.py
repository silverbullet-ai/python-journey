# Day 62 — Algorithmic Thinking & Big-O in Practice

import time


def linear_search(data: list[int], target: int) -> bool:
    for value in data:
        if value == target:
            return True
    return False


def quadratic_search(data: list[int], target: int) -> bool:
    for i in data:
        for j in data:
            if i + j == target:
                return True
    return False


def measure(func, data, target):
    start = time.time()
    func(data, target)
    end = time.time()
    return end - start


def main():
    data = list(range(10_000))
    target = 19_998         # We intentionally chose a target that forces the algorithm to explore the entire data set,
                            # so the measured time reflects the worst-case complexity.
                            # The algorithm cannot take longer than this for that input size.

    linear_time = measure(linear_search, data, target)
    quadratic_time = measure(quadratic_search, data, target)

    print(f"Linear search time: {linear_time:.4f}s")
    print(f"Quadratic search time: {quadratic_time:.4f}s")


if __name__ == "__main__":
    main()

print("\nDay 62 completed successfully!")
