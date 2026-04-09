# Day 23 Notes — Advanced File Handling

## Why Read Line by Line?

- Saves memory for large files  
- Allows processing as data streams  
- Cleaner logic for text processing  

---

## Reading Line by Line

Use a `for` loop on the file object.

```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## Common Patterns

```python
line.strip()          # Remove newline & spaces
line.split()          # Break into words
line.lower()          # Normalize text
```

Frequency analysis example:

```python
word_count = {}

with open("file.txt", "r") as file:
    for line in file:
        words = line.lower().strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

print(word_count)
```

---

## Writing Processed Output

Open a new file in `"w"` or `"a"` mode and write results.

```python
with open("output.txt", "w") as file:
    file.write("Processed data here")
```

---

## Mental Rule

> Read → Clean → Process → Write
