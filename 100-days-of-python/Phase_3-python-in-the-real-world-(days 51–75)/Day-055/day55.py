# Day 55 — Testing Mindset & Introduction to Unit Testing

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_total_price(price: float, tax_rate: float) -> float:
    """
    Pure function:
    - No side effects
    - Easy to test
    """
    if price < 0:
        raise ValueError("Price cannot be negative")

    return price + (price * tax_rate)


def main():
    logger.info("Program started")

    total = calculate_total_price(1000, 0.18)
    logger.info(f"Total price: {total}")

    logger.info("Program finished")


if __name__ == "__main__":
    main()

print("\nDay 55 completed successfully!\n")
