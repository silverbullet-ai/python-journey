# Day 47 Notes — Refactoring: Procedural → OOP

## What Is Refactoring?

- Refactoring means **improving structure without changing behavior**
- Goal is readability, maintainability, and extensibility
- Not a rewrite — a disciplined transformation

---

## Signs Procedural Code Needs Refactoring

- Many related variables passed everywhere  
- Repeated logic  
- Large functions doing multiple things  
- Hard to test or extend  

---

## Step-by-Step Refactoring Approach

1. Identify **data that belongs together**  
2. Identify **actions performed on that data**  
3. Create a class to group them  
4. Move functions into methods  
5. Replace globals with instance variables  

---

## Example: Procedural Code

```python
balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount
```

---

## Refactored OOP Version

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
```

---

## Benefits of OOP Refactor

- State is controlled  
- Behavior is grouped  
- Code is easier to extend  
- Fewer hidden dependencies  

---

## Refactoring Discipline

- One change at a time  
- Run code after each step  
- Behavior must remain the same  

---

## Mental Rule

> Refactoring is cleanup with intent, not decoration.
