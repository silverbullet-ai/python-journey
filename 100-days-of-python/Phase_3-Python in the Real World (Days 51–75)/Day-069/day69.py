# Day 69 — Threads in Python (I/O-Bound Concurrency)

import threading
import time


def simulate_io(task_name: str, delay: float):
    print(f"{task_name} started")
    time.sleep(delay)  # Simulates I/O wait
    print(f"{task_name} finished")


def main():
    start = time.time()

    t1 = threading.Thread(target=simulate_io, args=("Task 1", 2))
    t2 = threading.Thread(target=simulate_io, args=("Task 2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print(f"\nTotal time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()

print("\nDay 69 completed successfully!")
