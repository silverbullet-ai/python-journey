# Day 43 Notes — Decorators (Functions)



## What Is a Decorator?

* A decorator is a function that:

  * Takes another function as input
  * Returns a modified function

* Used to add behavior **before or after** a function runs

---



## Functions Are Objects



```python
def greet():
    print("Hello")

x = greet
x()
```

* Functions can be assigned, passed, and returned

---



## Basic Decorator Structure



```python
def my\_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
```



---

## Using a Decorator (Manual)



```python
def say\_hi():
    print("Hi")

say\_hi = my\_decorator(say\_hi)
say\_hi()
```



---

## Using `@` Syntax



```python
@my\_decorator
def say\_hello():
    print("Hello")
```



---

## Decorators with Arguments



```python
def decorator(func):
    def wrapper(\*args, \*\*kwargs):
        return func(\*args, \*\*kwargs)
    return wrapper
```



---

## Why Decorators Matter

* Logging
* Authentication
* Timing
* Validation
* Caching

All **without touching original code**.



---

## Mental Rule

> Decorators modify behavior, not logic.

