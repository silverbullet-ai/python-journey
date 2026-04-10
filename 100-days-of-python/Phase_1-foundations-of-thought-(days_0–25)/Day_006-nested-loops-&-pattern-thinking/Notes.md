# Day 6 Notes — Nested Loops

## What is a Nested Loop?

A nested loop is a loop **inside another loop**.

- Outer loop → controls rows  
- Inner loop → controls columns  

---

## How Nested Loops Work

For each iteration of the outer loop,  
the inner loop runs **completely**.

### Example Explanation

If:
- Outer loop runs 3 times  
- Inner loop runs 5 times each time  

Total executions = 3 × 5 = 15

---

## Basic Nested Loop Example

```python
for i in range(3):          # Outer loop (rows)
    for j in range(5):      # Inner loop (columns)
        print("*", end=" ")
    print()                 # Move to next line
```

---

## Why Patterns Matter

Patterns help in:

- Understanding logic flow  
- Visualizing loop execution  
- Building strong fundamentals  
- Preparing for problem-solving and interviews  

---

## Important Rule

Always understand:

- Which loop controls rows  
- Which loop controls columns  

### Mental Model

Outer loop → controls how many lines  
Inner loop → controls what happens inside each line
