# Day 37 Notes — `\_\_str\_\_`, `\_\_repr\_\_` \& Comparisons



## `\_\_str\_\_` vs `\_\_repr\_\_`



### `\_\_str\_\_`

* Human-readable
* Used by `print()`
* Meant for end users



### `\_\_repr\_\_`

* Developer-readable
* Used for debugging
* Should be unambiguous



```python
class User:
    def \_\_init\_\_(self, name):
        self.name = name

    def \_\_str\_\_(self):
        return f"User: {self.name}"

    def \_\_repr\_\_(self):
        return f"User('{self.name}')"
```



---

## Equality vs Identity



### Identity

* Checked using `is`
* Do both variables point to the same object?



```python
a = \[1, 2]
b = a
print(a is b)  # True
```



### Equality

* Checked using `==`
* Do objects have the same value?

```python
x = \[1, 2]
y = \[1, 2]
print(x == y)  # True
```



---

## `\_\_eq\_\_` — Equality Comparison



```python
class Student:
    def \_\_init\_\_(self, roll):
        self.roll = roll

    def \_\_eq\_\_(self, other):
        return self.roll == other.roll
```



---

## Ordering Comparisons

* `\_\_lt\_\_` → `<`
* `\_\_le\_\_` → `<=`
* `\_\_gt\_\_` → `>`
* `\_\_ge\_\_` → `>=`



```python
class Score:
    def \_\_init\_\_(self, marks):
        self.marks = marks

    def \_\_lt\_\_(self, other):
        return self.marks < other.marks
```



---

## Why Comparisons Matter

* Sorting objects
* Searching
* Removing duplicates
* Clean, expressive code



---

## Mental Rule

> Identity checks \*\*where\*\* an object is.  
> Equality checks \*\*what\*\* an object represents.

