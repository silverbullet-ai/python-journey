# Day 82
# Purpose: Demonstrate basic logging usage

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def divide(a, b):
    logging.debug(f"Attempting to divide {a} by {b}")

    if b == 0:
        logging.error("Division by zero attempted")
        raise ValueError("Division by zero is not allowed")

    result = a / b
    logging.info(f"Division successful: result={result}")
    return result


def main():
    logging.info("Application started")

    try:
        divide(10, 2)
        divide(5, 0)
    except ValueError:
        logging.warning("Handled a division error gracefully")

    logging.info("Application finished")


if __name__ == "__main__":
    main()
