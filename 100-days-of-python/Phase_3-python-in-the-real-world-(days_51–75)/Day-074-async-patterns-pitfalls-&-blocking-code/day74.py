# Day 74 — Async Patterns, Pitfalls & Blocking Code

import asyncio
import time


async def bad_async_task(name: str):
    print(f"{name} started (BAD)")
    time.sleep(2)  # Blocks the event loop. The total time taken would be equal to sum of waiting time.
    print(f"{name} finished (BAD)")


async def good_async_task(name: str):
    print(f"{name} started (GOOD)")
    await asyncio.sleep(2)  # Non-blocking
    print(f"{name} finished (GOOD)")


async def run_bad_example():
    start = time.time()
    await asyncio.gather(
        bad_async_task("Task 1"),
        bad_async_task("Task 2"),
    )
    end = time.time()
    print(f"\nBad example time: {end - start:.2f} seconds")


async def run_good_example():
    start = time.time()
    await asyncio.gather(
        good_async_task("Task 1"),
        good_async_task("Task 2"),
    )
    end = time.time()
    print(f"\nGood example time: {end - start:.2f} seconds")


async def main():
    print("Running bad async example:\n")
    await run_bad_example()

    print("\nRunning good async example:\n")
    await run_good_example()


if __name__ == "__main__":
    asyncio.run(main())

print("\nDay 74 completed successfully!")
