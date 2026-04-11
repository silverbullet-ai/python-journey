# Day 90 — sample.py

def calculate_total(price, tax):
    total = price + price * tax
    return total


def main():
    result = calculate_total(100, 0.18)
    print("Total:", result)


if __name__ == "__main__":
    main()

# This file is intentionally simple.
# The lesson is how tooling would look at it, not what it does.