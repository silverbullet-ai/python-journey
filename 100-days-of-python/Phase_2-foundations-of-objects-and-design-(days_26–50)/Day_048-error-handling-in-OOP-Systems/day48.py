# Day 48 — Error Handling in OOP Systems

print("ERROR HANDLING IN OOP PRACTICE\n")

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance")
        self.balance -= amount
        return self.balance

account = BankAccount(1000)

try:
    account.withdraw(1500)
except InsufficientFundsError as e:
    print("Error:", e)

try:
    account.withdraw(-100)
except ValueError as e:
    print("Error:", e)

print("\nCurrent balance:", account.balance)

print("\nDay 48 completed successfully!")
