# Day 46 Notes — OOP Design Patterns (Mini Patterns)



## What Is a Design Pattern?

* A design pattern is a **reusable solution** to a common problem
* It is a **concept**, not code you copy-paste
* Patterns give names to good design decisions



---

## Pattern 1: Factory (Simple Factory)



### Problem

Object creation logic clutters code.



### Solution

Move object creation to a dedicated function.



```python
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def animal\_factory(kind):
    if kind == "dog":
        return Dog()
    elif kind == "cat":
        return Cat()
```



---

## Pattern 2: Strategy (Behavior Injection)



### Problem

Same task, multiple algorithms.



### Solution

Pass behavior instead of hard-coding logic.



```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a \* b

class Calculator:
    def \_\_init\_\_(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy(a, b)
```



---

## Pattern 3: Composition (Revisited)



### Problem

Inheritance becomes rigid.



### Solution

Build objects using other objects.



```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def \_\_init\_\_(self, engine):
        self.engine = engine
```



---

## Pattern Discipline

* Patterns are tools, not rules
* Use them when the problem repeats
* Avoid forcing patterns where simple code works



---

## Mental Rule

> Patterns describe intent, not structure.

