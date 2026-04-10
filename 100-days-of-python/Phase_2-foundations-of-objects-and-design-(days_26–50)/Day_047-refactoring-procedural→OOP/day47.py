# Day 47 — Refactoring Procedural Code to OOP

print("REFACTORING PRACTICE\n")

# Procedural version
balance = 500

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

deposit(200)
withdraw(100)
print("Procedural balance:", balance)

print("\n------------------\n")

# OOP refactored version
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(500)
account.deposit(200)
account.withdraw(100)
print("OOP balance:", account.balance)

print("\nDay 47 completed successfully!")