# Day 45 Notes — Context Managers



## What Is a Context Manager?

* A context manager is an object that:

  * Sets something up
  * Cleans it up automatically

* Used with the `with` statement



Common use cases:

* Files
* Database connections
* Locks
* Network resources



---

## The `with` Statement



```python
with open("file.txt", "r") as file:
    data = file.read()
```



What happens internally:

1. `\_\_enter\_\_()` is called
2. Code inside the `with` block runs
3. `\_\_exit\_\_()` is called — even if an error occurs



---

## Why Context Managers Matter



Without context managers:

* Manual cleanup required
* Easy to forget resource release
* Bugs during exceptions



With context managers:

* Cleanup is guaranteed
* Code is cleaner and safer

---



## Creating a Context Manager (Class-Based)



```python
class MyContext:
    def \_\_enter\_\_(self):
        print("Entering context")
        return self

    def \_\_exit\_\_(self, exc\_type, exc\_val, exc\_tb):
        print("Exiting context")
```



---

## Handling Exceptions in `\_\_exit\_\_`

* `\_\_exit\_\_` receives exception details
* Returning `True` suppresses the exception
* Returning `False` propagates it

---



## Context Managers Using `contextlib`



Python provides a helper module.



```python
from contextlib import contextmanager

@contextmanager
def my\_context():
    print("Enter")
    yield
    print("Exit")
```



---



## Mental Rule

> Acquire resources late.  
> Release resources early.

