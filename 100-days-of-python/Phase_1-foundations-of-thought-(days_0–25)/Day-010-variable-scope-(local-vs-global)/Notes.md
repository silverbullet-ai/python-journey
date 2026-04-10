# Day 10 Notes — Variable Scope

## What is Scope?

Scope defines **where a variable can be accessed** in a program.

---

## Local Scope

- Variables defined inside a function  
- Accessible only within that function  

### Example

```python
def func():
    x = 10   # local variable
    print(x)

func()

# print(x)  ❌ Error: x is not accessible outside the function
```

---

## Global Scope

- Variables defined outside all functions  
- Accessible everywhere (inside and outside functions)

### Example

```python
y = 5

def func():
    print(y)

func()
```

---

## Important Rule

A function can **read** a global variable,  
but it cannot **modify** it unless declared `global`.

---

## `global` Keyword

Used to modify a global variable inside a function.

### Example

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)
```

---

## Why Avoid `global`?

- Makes code harder to understand  
- Creates hidden dependencies  
- Causes unexpected side effects  

---

## Preferred Approach

- Pass values as parameters  
- Return results from functions  
- Keep data flow explicit
