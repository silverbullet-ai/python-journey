# Day 32 Notes — Composition vs Inheritance



## Inheritance (Is-A Relationship)

* A class **inherits** from another class
* The child class **is a type of** the parent class
* Enables code reuse through hierarchy



```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass
```

> A `Dog` \*\*is an\*\* `Animal`



---

## Problems with Overusing Inheritance

* Rigid class hierarchies
* Tight coupling
* Harder to modify later
* Small changes can break many classes



---

## Composition (Has-A Relationship)

* An object **contains** another object
* Behavior is achieved by using other objects
* More flexible and safer than inheritance



```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def \_\_init\_\_(self):
        self.engine = Engine()
```

> A `Car` \*\*has an\*\* `Engine`



---

## Why Composition Is Often Better

* Loose coupling
* Easier to change parts
* Better for real-world modeling
* Encouraged in modern OOP design



---

## When to Use Inheritance



Use inheritance when:

* There is a clear **is-a** relationship
* The hierarchy is stable
* Behavior truly belongs to the parent



---

## When to Use Composition



Use composition when:

* Objects collaborate
* Behavior may change
* Flexibility is required



---

## Mental Rule

> Prefer composition over inheritance —  
> inheritance is for \*\*identity\*\*, composition is for \*\*capability\*\*.

