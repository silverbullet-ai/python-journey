# Day 92 — review_example.py

def calculate_discount(price, discount):
    if discount > 1:
        discount = discount / 100
    return price - (price * discount)


def checkout(price, discount):
    total = calculate_discount(price, discount)
    print("Total:", total)
    return total
