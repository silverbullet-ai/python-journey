# Day 34 Notes — Method Overriding \& Polymorphism



## What Is Method Overriding?

* Method overriding occurs when:

  * A child class defines a method
  * With the **same name** as in the parent class

* The child’s method replaces the parent’s version



```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
```



---

## What Is Polymorphism?

* Polymorphism means **many forms**
* The same method name behaves differently
* Behavior depends on the **object**, not the reference



---

## Polymorphism in Action



```python
animals = \[Dog(), Animal()]

for animal in animals:
    animal.speak()
```



* Python calls the correct `speak()` method
* Decision is made **at runtime**



---

## Why Polymorphism Matters



Without polymorphism:

* Heavy use of `if-else`
* Rigid and fragile code



With polymorphism:

* Cleaner logic
* Easier extension
* More readable systems



---

## Dynamic Method Resolution



Python checks in order:

1. Object’s class
2. Parent class
3. Further ancestors

This process is called **Method Resolution Order (MRO)**.



---

## Mental Rule

> One interface.  
> Many behaviors.

