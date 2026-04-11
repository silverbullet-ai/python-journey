# Day 71 — Thread-Safe Design & Avoiding Shared State

import threading
import queue


def worker(task_queue: queue.Queue, results: list):
    """
    Worker thread:
    - Pulls tasks from a shared queue
    - Computes results independently
    - Avoids shared counters or global state
    """
    while True:
        try:
            # Try to fetch a task without blocking
            value = task_queue.get_nowait()
        except queue.Empty:
            # No more tasks → exit the worker loop
            break

        # Perform computation (thread-local work)
        result = value * value

        # Collect result (simple, controlled shared structure)
        results.append(result)

        # Inform the queue that the task is done
        task_queue.task_done()


def main():
    # Queue owns the work; threads request tasks from it
    task_queue = queue.Queue()

    # Stores results produced by workers
    results = []

    # Populate the queue with independent tasks
    for i in range(10):
        task_queue.put(i)

    threads = []

    # Create multiple identical worker threads
    for _ in range(3):
        t = threading.Thread(
            target=worker,
            args=(task_queue, results)
        )
        threads.append(t)
        t.start()   # Start thread execution

    # Wait for all threads to finish processing
    for t in threads:
        t.join()

    # Order is non-deterministic; sorting for clean output
    print("Results:", sorted(results))


if __name__ == "__main__":
    main()

print("\nDay 71 completed successfully!")
