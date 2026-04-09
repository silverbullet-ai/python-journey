# Day 44 Notes — Decorators (Classes)



## Why Class-Based Decorators?



Function decorators are great, but they:

* Cannot easily maintain state
* Become messy for complex logic



Class decorators:

* Can store data
* Can manage long-term behavior
* Are easier to extend

---



## How a Class Becomes a Decorator

A class becomes a decorator when:

* It takes a function in `\_\_init\_\_`
* It implements `\_\_call\_\_`

---



## Basic Class Decorator Example



```python
class MyDecorator:
    def \_\_init\_\_(self, func):
        self.func = func

    def \_\_call\_\_(self):
        print("Before function")
        self.func()
        print("After function")
```



---

## Using the Class Decorator



```python
@MyDecorator
def greet():
    print("Hello")
```



Calling `greet()` actually calls:



```python
MyDecorator(greet).\_\_call\_\_()
```

---

## Class Decorator with Arguments



```python
class Repeat:
    def \_\_init\_\_(self, times):
        self.times = times

    def \_\_call\_\_(self, func):
        def wrapper(\*args, \*\*kwargs):
            for \_ in range(self.times):
                func(\*args, \*\*kwargs)
        return wrapper
```



---

## When to Use Class Decorators

Use class decorators when:

* You need to store state
* You need complex configuration
* Behavior must persist across calls



---

## Mental Rule

> Use function decorators for simplicity.  
> Use class decorators for control.

