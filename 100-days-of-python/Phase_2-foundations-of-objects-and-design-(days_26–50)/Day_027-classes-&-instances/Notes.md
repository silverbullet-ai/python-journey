# Day 27 Notes — Classes \& Instances



## What Is a Class?



* A class is a **blueprint**
* It defines:

  * What data an object will have
  * What actions an object can perform

* A class does not represent a real object by itself



---

## Example (Blueprint)

```python
class Car:
    pass
```

---

## What Is an Instance?



* An instance is a real object created from a class
* Multiple instances can be created from the same class
* Each instance is independent



```python
car1 = Car()
car2 = Car()
```

---

## Class vs Instance



| Class | Instance |
|------|----------|
| Blueprint | Real object |
| Defined once | Can create many |
| No real data | Holds actual data |

---

## How Python Creates Objects



When you write:

```python
car = Car()
```

Python:

1. Creates a new empty object
2. Assigns it the type `Car`
3. Returns the object reference



---

## Why Classes Matter



Classes allow you to:

* Model real-world entities
* Group data and behavior together
* Write scalable and maintainable code



---

## Naming Convention



* Class names use **PascalCase**
* Instance names use **snake\_case**

```python
class Student:
    pass

student\_1 = Student()
```

---

## Mental Rule

> A class describes what an object can be.  
> An instance is what the object actually is.

