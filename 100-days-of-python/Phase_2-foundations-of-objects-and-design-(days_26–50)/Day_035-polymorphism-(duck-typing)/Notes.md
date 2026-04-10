# Day 35 Notes — Polymorphism (Duck Typing)



## What Is Duck Typing?



Duck typing follows this idea:

> “If it looks like a duck and quacks like a duck,  
> then it is treated as a duck.”

* Python does not care about the **class**
* Python cares about **what the object can do**



---

## Duck Typing Example



```python
class Dog:
    def speak(self):
        print("Dog barks")

class Human:
    def speak(self):
        print("Human speaks")
```



```python
def make\_sound(obj):
    obj.speak()
```

* Both objects work
* No inheritance required



---

## Key Difference from Inheritance



### Inheritance

* Based on **is-a** relationships
* Requires shared base classes



### Duck Typing

* Based on **can-do** behavior
* No shared base class needed



---

## Why Duck Typing Is Powerful

* Less rigid code
* Easier to extend
* More Pythonic
* Encourages composition



---

## When Duck Typing Fails

* If required behavior is missing
* Causes runtime errors

```python
# AttributeError if method does not exist
```



---

## Defensive Duck Typing (Optional)



```python
if hasattr(obj, "speak"):
    obj.speak()
```

* Use sparingly
* Trust behavior when possible



---

## Mental Rule

> Don’t ask what an object is.  
> Ask what an object can do.

