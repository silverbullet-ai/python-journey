# Day 75 — Real-World Concurrency Design (Capstone)

import asyncio
import time


async def fetch_data(source: str):
    """Simulates async I/O (API, network, etc.)"""
    print(f"Fetching data from {source}")
    await asyncio.sleep(2)
    print(f"Finished fetching from {source}")
    return f"data_from_{source}"


async def process_pipeline():
    """
    Async orchestration layer:
    - Runs multiple I/O tasks concurrently
    - Collects results safely
    """
    results = await asyncio.gather(
        fetch_data("Service A"),
        fetch_data("Service B"),
        fetch_data("Service C"),
    )

    print("\nPipeline results:")
    for result in results:
        print(result)


def main():
    start = time.time()
    asyncio.run(process_pipeline())
    end = time.time()

    print(f"\nTotal pipeline time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()

print("\nDay 75 completed successfully!")
