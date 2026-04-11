# Day 63 — Data Structures for Performance

import time

# Type hints clarify intent:
# `data` is expected to be a list of integers and the function
# returns a boolean indicating membership.
# Type hints are not enforced at runtime.
# They document expected input/output types and help
# readers, IDEs, and static analysis tools understand intent.
# Type hints express design intent, not runtime constraints.
def membership_test_list(data: list[int], target: int) -> bool:
    return target in data


def membership_test_set(data: set[int], target: int) -> bool:
    return target in data


def measure(func, data, target):
    start = time.time()
    func(data, target)
    end = time.time()
    return end - start


def main():
    data_list: list[int] = list(range(1_000_000))
    data_set: set[int] = set(data_list)
    target = 999_999

    list_time = measure(membership_test_list, data_list, target)
    set_time = measure(membership_test_set, data_set, target)

    print(f"List membership time: {list_time:.6f}s")
    print(f"Set membership time:  {set_time:.6f}s")


if __name__ == "__main__":
    main()

print("\nDay 63 completed successfully!")
