# Day 33 Notes — Inheritance \& `super()`



## What Is Inheritance?

* Inheritance allows a class to **reuse** another class
* The child class automatically gets:

  * Parent attributes
  * Parent methods

* The child can also **extend or override** behavior



```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass
```



---

## Why `super()` Exists

* `super()` allows access to the parent class
* Prevents duplication of code
* Keeps inheritance chains clean



---

## Using `super()` in Constructors



```python
class Animal:
    def \_\_init\_\_(self, name):
        self.name = name

class Dog(Animal):
    def \_\_init\_\_(self, name, breed):
        super().\_\_init\_\_(name)
        self.breed = breed
```



---

## Method Overriding

* Child class can redefine parent methods
* Method name must be the same

```python
class Dog(Animal):
    def speak(self):
        print("Dog barks")
```



---

## Common Mistake



Forgetting to call `super().\_\_init\_\_()`:



```python
# ❌ Parent data not initialized
```

* This can lead to missing attributes



---

## Mental Rule

> Use inheritance to \*\*extend\*\*, not to copy.

