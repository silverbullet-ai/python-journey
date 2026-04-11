# Day 79 — service.py
# Purpose: Demonstrate mocking of external dependencies


def fetch_data():
    """
    Simulates an external dependency.
    In real systems, this could be an API call or database access.
    """
    raise RuntimeError("Real external call should not be made in unit tests")


def process_data():
    """
    Uses fetch_data and applies business logic.
    """
    data = fetch_data()
    return data.upper()
