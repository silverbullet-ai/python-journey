# Day 52 — PEP 8 & Clean Code Discipline

print("PEP 8 AND CLEAN CODE PRACTICE\n")


def calculate_discount(price: float, discount_rate: float) -> float:
    """
    Calculates discounted price.

    Args:
        price: original price
        discount_rate: discount as a decimal

    Returns:
        discounted price
    """
    if price <= 0:
        raise ValueError("Price must be positive")

    return price - (price * discount_rate)


def main():
    original_price = 1000.0
    discount_rate = 0.15

    final_price = calculate_discount(
        original_price,
        discount_rate
    )

    print(f"Final price after discount: {final_price}")


if __name__ == "__main__":
    main()

print("\nDay 52 completed successfully!")
