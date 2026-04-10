# Day 39 Notes — Dataclasses



## What Is a Dataclass?

* A dataclass is a class designed primarily to **store data**
* Python automatically generates common methods for you



Generated methods include:

* `\_\_init\_\_`
* `\_\_repr\_\_`
* `\_\_eq\_\_`



Dataclasses are provided by the `dataclasses` module.



---

## Basic Dataclass Example



```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int
```



This automatically creates:

* Constructor
* Readable representation
* Equality comparison



---

## Using the Dataclass



```python
s1 = Student("Aahish", 90)
s2 = Student("Aahish", 90)

print(s1)
print(s1 == s2)
```



---

## Dataclass vs Normal Class



### Normal Class

* More control
* More boilerplate
* Better for complex behavior



### Dataclass

* Less boilerplate
* Ideal for data containers
* Clean and readable



---

## Adding Custom Methods



Dataclasses can still have methods.



```python
@dataclass
class Student:
    name: str
    marks: int

    def is\_passed(self):
        return self.marks >= 40
```



---

## When NOT to Use Dataclasses

* Heavy business logic
* Complex inheritance
* Mutable shared state



---

## Mental Rule

> Use dataclasses when the data matters more than behavior.

