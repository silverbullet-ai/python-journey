# Day 40 Notes — Immutability \& Design Choices



## What Is Immutability?

* An immutable object **cannot be changed after creation**
* Any “modification” creates a **new object**
* Immutable objects are predictable and safe



---

## Examples of Immutable Types

* `int`
* `float`
* `str`
* `tuple`
* `frozenset`



```python
x = 10
x += 1  # new object created
```



---

## Why Immutability Matters



Immutability:

* Prevents accidental state changes
* Avoids shared-reference bugs
* Makes code easier to reason about
* Improves thread safety



---

## Mutable vs Immutable Design



### Mutable Design



```python
class Counter:
    def \_\_init\_\_(self, value):
        self.value = value

    def increment(self):
        self.value += 1
```



* State changes over time
* Harder to track bugs



### Immutable Design



```python
class Counter:
    def \_\_init\_\_(self, value):
        self.value = value

    def increment(self):
        return Counter(self.value + 1)
```



* Original object unchanged
* New object returned

---



## Immutable Dataclasses



Dataclasses can be made immutable.



```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```



* Attempts to modify raise errors
* Guarantees object safety



---

## When to Use Immutability



Use immutability when:

* Data represents a value
* State should not change
* Predictability is important



Avoid immutability when:

* Frequent state changes are required
* Performance is critical and mutation is safe

---



## Mental Rule

> Mutable for behavior.  
> Immutable for values.

