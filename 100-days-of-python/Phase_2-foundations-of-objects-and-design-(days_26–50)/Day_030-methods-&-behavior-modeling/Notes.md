# Day 30 Notes — Methods \& Behavior Modeling



## What Is a Method?

* A method is a **function defined inside a class**
* It represents the **behavior of an object**
* It always works on the object’s data



```python
class Student:
    def study(self):
        print("Studying...")
```



---

## Function vs Method



### Function

* Independent
* Does not belong to any object

```python
def study():
    print("Studying...")


```

### Method

* Belongs to a class
* Acts on instance data using `self`



```python
class Student:
    def study(self):
        print(self.name, "is studying")
```

---

## Calling a Method



```python
student = Student("Aahish")
student.study()
```

Internally, Python does:



```python
Student.study(student)
```



---

## Methods Using Instance Data



```python
class Student:
    def \_\_init\_\_(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


```

---

## Multiple Methods in a Class



```python
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a \* b
```



---

## Why Methods Matter



Methods allow you to:

* Keep data and behavior together
* Reduce global functions
* Model real-world actions



---

## Mental Rule

> Data describes what an object is.  
> Methods describe what an object does.

