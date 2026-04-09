# Day 85 — observable_app.py
# Purpose: Demonstrate observability-oriented thinking

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def process_order(order_id: int):
    logging.info(f"Processing order {order_id}")

    if order_id <= 0:
        logging.error("Invalid order ID encountered")
        raise ValueError("Order ID must be positive")

    logging.info(f"Order {order_id} processed successfully")
    return True


def main():
    logging.info("Application started")

    try:
        process_order(1)
        process_order(-5)
    except ValueError as e:
        logging.warning(f"Order processing failed: {e}")

    logging.info("Application finished")


if __name__ == "__main__":
    main()
