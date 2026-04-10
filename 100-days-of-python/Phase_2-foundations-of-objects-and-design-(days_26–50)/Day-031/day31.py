# Day 31 — Encapsulation & Access Conventions

print("ENCAPSULATION PRACTICE\n")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._branch = "Main"       # Protected (convention)
        self.__balance = balance    # Private

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

# Create object
account = BankAccount("Aahish", 5000)

print("Owner:", account.owner)
print("Branch:", account._branch)

account.show_balance()
account.deposit(1500)
account.show_balance()

print("\nDay 31 completed successfully!")
