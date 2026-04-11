# Day 54 — Assertions, Defensive Programming & Fail Fast

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_square_root(value: float) -> float:
    # Assertion: this function is never meant to receive negative numbers
    assert value >= 0, "Value must be non-negative"

    logger.info("Calculating square root")
    return value ** 0.5


def withdraw(balance: float, amount: float) -> float:
    # Runtime validation: user-controlled input
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    logger.info("Withdrawal successful")
    return balance - amount


def main():
    logger.info("Program started")

    # Assertion example (developer responsibility)
    result = calculate_square_root(16)
    logger.info(f"Square root result: {result}")

    # Exception example (user responsibility)
    new_balance = withdraw(1000, 250)
    logger.info(f"Remaining balance: {new_balance}")

    logger.info("Program finished")


if __name__ == "__main__":
    main()

print("\nDay 54 completed successfully!")
