# Day 73 — Writing Async Code (asyncio Basics)

import asyncio
import time


async def simulate_io(task_name: str, delay: float):
    print(f"{task_name} started")
    await asyncio.sleep(delay)  # Non-blocking wait
    print(f"{task_name} finished")


async def main():
    start = time.time()

    await asyncio.gather(
        # 2 seconds dealy added to each thread.
        # Still the time taken to complete all the task would be almost 2 seconds, and not 6 seconds.
        simulate_io("Task 1", 2),
        simulate_io("Task 2", 2),
        simulate_io("Task 3", 2),
    )

    end = time.time()
    print(f"\nTotal time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

print("\nDay 73 completed successfully!")
