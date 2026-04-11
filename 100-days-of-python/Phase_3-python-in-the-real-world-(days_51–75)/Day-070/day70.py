# Day 70 — Race Conditions, Locks & Shared State

import threading
import time

counter = 0
lock = threading.Lock()


def unsafe_increment():
    """
    Intentionally unsafe.
    `sleep(0)` forces a context switch, increasing the chance
    that threads interleave during the read-modify-write cycle.
    This makes the race condition visible even on fast CPUs.
    """
    global counter
    for _ in range(100_000):
        temp = counter
        time.sleep(0)  # Yield execution to another thread
        counter = temp + 1


def safe_increment():
    """
    Thread-safe version.
    Lock ensures that the critical section is executed
    by only one thread at a time.
    """
    global counter
    for _ in range(100_000):
        with lock:
            temp = counter
            time.sleep(0)  # Still safe due to lock
            counter = temp + 1



def run_without_lock():
    global counter
    counter = 0

    t1 = threading.Thread(target=unsafe_increment)
    t2 = threading.Thread(target=unsafe_increment)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Without lock:", counter)


def run_with_lock():
    global counter
    counter = 0

    t1 = threading.Thread(target=safe_increment)
    t2 = threading.Thread(target=safe_increment)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("With lock:", counter)


def main():
    run_without_lock()
    run_with_lock()


if __name__ == "__main__":
    main()

print("\nDay 70 completed successfully!")
