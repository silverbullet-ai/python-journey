# Day 29 Notes — Instance Variables vs Class Variables



## Instance Variables

* Belong to a **specific object**
* Defined using `self`
* Each instance has its **own copy**



```python
class Student:
    def \_\_init\_\_(self, name):
        self.name = name
```

```python
s1 = Student("Aahish")
s2 = Student("Rahul")
```

* `s1.name` and `s2.name` are independent



---

## Class Variables

* Belong to the **class**
* Shared by **all instances**
* Defined inside the class, outside methods



```python
class Student:
    college = "ABC University"
```

```python
print(Student.college)
```

---

## Accessing Class Variables via Instances

```python
s1 = Student("Aahish")
print(s1.college)
```

Python lookup order:

1. Looks in the instance
2. If not found, looks in the class



---

## Important Pitfall

Modifying a class variable using an instance:

```python
s1.college = "XYZ University"
```

* This creates a **new instance variable**
* It does **not** change the class variable



---

## Attribute Lookup Order

1. Instance (`obj.\_\_dict\_\_`)
2. Class (`Class.\_\_dict\_\_`)
3. Parent classes



---

## When to Use What

### Use Instance Variables When:

* Data belongs to one object
* Data differs per object



### Use Class Variables When:

* Data is common to all objects
* Represents shared state or constants



---

## Mental Rule

> Instance variables describe who the object is.  
> Class variables describe what all objects share.

