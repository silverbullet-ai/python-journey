# Day 38 Notes — Operator Overloading



## What Is Operator Overloading?

* Operator overloading allows custom objects to use operators
* Python translates operators into magic method calls



Example:

```python
a + b   # internally calls a.\_\_add\_\_(b)
```



---

## Common Operator Magic Methods

* `\_\_add\_\_` → `+`
* `\_\_sub\_\_` → `-`
* `\_\_mul\_\_` → `\*`
* `\_\_eq\_\_` → `==`
* `\_\_lt\_\_` → `<`



---

## Simple Addition Example



```python
class Vector:
    def \_\_init\_\_(self, x, y):
        self.x = x
        self.y = y

    def \_\_add\_\_(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```



---

## Using the Overloaded Operator



```python
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
```



---

## Why Operator Overloading Matters

* Makes code readable
* Models real-world concepts naturally
* Reduces boilerplate method calls



---

## Operator Overloading Discipline

* Overload only when behavior is obvious
* Do not surprise the user
* Keep semantics intuitive



---

## Mental Rule

> Operators should clarify meaning, not hide logic.

