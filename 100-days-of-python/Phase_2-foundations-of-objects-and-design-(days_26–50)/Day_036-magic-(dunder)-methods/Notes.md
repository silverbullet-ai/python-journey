# Day 36 Notes — Magic (Dunder) Methods



## What Are Magic (Dunder) Methods?

* Special methods with **double underscores**
* Automatically called by Python
* Not meant to be called directly



Examples:

* `\_\_init\_\_`
* `\_\_str\_\_`
* `\_\_repr\_\_`
* `\_\_add\_\_`



---

## Why They Exist

Magic methods allow:

* Built-in functions to work on custom objects
* Operators to work with user-defined classes
* Python to stay consistent and expressive



---

## `\_\_str\_\_` — Human-Readable Output

* Called when using `print(object)`
* Should return a readable string



```python
class Student:
    def \_\_init\_\_(self, name):
        self.name = name

    def \_\_str\_\_(self):
        return f"Student name: {self.name}"
```



---

## `\_\_repr\_\_` — Developer-Readable Output

* Used in debugging
* Should be unambiguous
* Often used in interactive shells



```python
class Student:
    def \_\_repr\_\_(self):
        return f"Student('{self.name}')"
```



---

## Difference Between `\_\_str\_\_` and `\_\_repr\_\_`

* `\_\_str\_\_` → user-friendly
* `\_\_repr\_\_` → developer-friendly

If `\_\_str\_\_` is missing, Python falls back to `\_\_repr\_\_`.



---

## Magic Methods Are Hooks

* You don’t call them
* Python calls them for you



Example:

```python
print(obj)   # internally calls obj.\_\_str\_\_()
```



---

## Mental Rule

> Magic methods define  
> how your object behaves in Python’s world.

