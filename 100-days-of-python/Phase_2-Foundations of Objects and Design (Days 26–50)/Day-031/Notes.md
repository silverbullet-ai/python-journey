# Day 31 Notes — Encapsulation \& Access Conventions



## What Is Encapsulation?

* Encapsulation means **controlling access to data**
* It protects object state from accidental misuse
* It exposes only what is necessary



---

## Public Attributes

* Accessible from anywhere
* Default behavior in Python

```python
class Student:
    def \_\_init\_\_(self, name):
        self.name = name


```

---

## Protected Attributes (Convention)

* Prefixed with a single underscore `\_`
* Indicates internal use
* Still accessible, but discouraged

```python
class Student:
    def \_\_init\_\_(self, name):
        self.\_name = name


```

---

## Private Attributes (Name Mangling)

* Prefixed with double underscores `\_\_`
* Python mangles the name internally
* Reduces accidental access



```python
class Student:
    def \_\_init\_\_(self, name):
        self.\_\_name = name
```



---

## Name Mangling Explained

```python
student = Student("Aahish")
print(student.\_Student\_\_name)
```

* This works, but **should not be used**
* Privacy is enforced by **discipline, not force**

---



## Why Python Uses Conventions

* Python trusts developers
* Encourages responsibility over restriction
* Keeps the language flexible and clean



---

## Mental Rule

> Encapsulation is about intent, not secrecy.

