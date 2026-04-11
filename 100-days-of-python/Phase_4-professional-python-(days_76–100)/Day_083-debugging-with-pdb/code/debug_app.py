# Day 83 — debug_app.py
# Purpose: Practice interactive debugging with pdb

import pdb


def calculate_discount(price, discount):
    final_price = price - (price * discount)
    return final_price


def checkout(price, discount):
    pdb.set_trace()  # Breakpoint
    return calculate_discount(price, discount)


def main():
    total = checkout(100, 0.2)
    print(f"Final price: {total}")


if __name__ == "__main__":
    main()
