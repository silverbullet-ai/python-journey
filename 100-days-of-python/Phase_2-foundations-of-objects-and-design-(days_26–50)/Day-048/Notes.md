# Day 48 Notes — Error Handling in OOP Systems

## Errors vs Exceptions

- Errors represent **unexpected failures**
- Exceptions represent **expected failure cases**
- Good design anticipates exceptions

---

## Where `try-except` Belongs

Use `try-except`:
- At **system boundaries**
- Around user input
- Around external resources (files, APIs)

Avoid:
- Wrapping every method in `try-except`
- Swallowing exceptions silently

---

## Raising Exceptions in Methods

Methods should:
- Validate input  
- Raise meaningful exceptions  
- Let callers decide how to handle them  

```python
class BankAccount:
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
```

---

## Custom Exceptions

Use custom exceptions to:
- Represent domain-specific errors  
- Improve readability  

```python
class InsufficientFundsError(Exception):
    pass
```

---

## Using Custom Exceptions

```python
class BankAccount:
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance")
```

---

## Handling Exceptions at the Boundary

```python
try:
    account.withdraw(5000)
except InsufficientFundsError as e:
    print("Transaction failed:", e)
```

---

## Error Handling Discipline

- Fail fast  
- Fail loudly  
- Fail clearly  

---

## Mental Rule

> Methods raise exceptions.  
> Systems handle exceptions.
