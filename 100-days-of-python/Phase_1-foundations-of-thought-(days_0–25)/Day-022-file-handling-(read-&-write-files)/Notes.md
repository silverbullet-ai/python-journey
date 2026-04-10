# Day 22 Notes — File Handling

## What is File Handling?

File handling allows a program to:

- Read data from files  
- Write data to files  
- Store information permanently  

---

## Opening a File

### Syntax

```python
file = open("filename", "mode")
```

### Common Modes

- `"r"` → read  
- `"w"` → write (overwrites file)  
- `"a"` → append  
- `"r+"` → read & write  

---

## Reading Files

```python
file = open("file.txt", "r")

file.read()       # Reads entire file
file.readline()   # Reads one line
file.readlines()  # Reads all lines into a list

file.close()
```

---

## Writing Files

```python
file = open("file.txt", "w")

file.write("Hello World")
file.writelines(["Line 1
", "Line 2
"])

file.close()
```

---

## `with` Statement (BEST PRACTICE)

Automatically closes the file.

```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

---

## Why Use `with`?

- No need to close file manually  
- Prevents memory leaks  
- Cleaner and safer code  
- Handles exceptions properly  
