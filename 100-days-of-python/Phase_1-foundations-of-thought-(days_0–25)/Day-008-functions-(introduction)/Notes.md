# Day 8 Notes — Functions

## Why Functions?

Functions allow us to:

- Reuse code  
- Avoid repetition  
- Organize logic  
- Make programs easier to read and maintain  

Instead of writing the same logic again and again,  
we define it once and reuse it.

---

## Defining a Function

### Syntax

```python
def function_name():
    statements
```

- `def` → keyword to define a function  
- `function_name` → name of the function  
- `()` → parameters (if any)  

### Example

```python
def greet():
    print("Hello")
```

---

## Calling a Function

A function runs only when it is **called**.

```python
greet()
```

---

## Parameters and Arguments

- **Parameters** → variables in function definition  
- **Arguments** → values passed during function call  

### Example

```python
def greet(name):      # name is parameter
    print("Hello", name)

greet("Aahish")       # "Aahish" is argument
```

---

## `return` Statement

- Sends a value back to the caller  
- Ends function execution  

### Example

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

---

## Important Difference

- `print()` → displays output  
- `return` → gives value back for further use
