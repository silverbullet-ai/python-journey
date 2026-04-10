# Day 42 Notes — Generators



## What Is a Generator?

* A generator is a special type of **iterator**
* It generates values **one at a time**
* It does not store all values in memory

Generators are created using `yield`.

---



## `yield` vs `return`



### `return`

* Ends the function
* Returns a single value



### `yield`

* Pauses the function
* Saves execution state
* Continues from where it left off



---

## Simple Generator Example



```python
def count\_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```



---

## Using a Generator



```python
gen = count\_up(3)

for num in gen:
    print(num)
```



---

## Generator vs Iterator



| Iterator | Generator |
|--------|-----------|
| Manual class | Simple function |
| More boilerplate | Clean syntax |
| Explicit state | Implicit state |

---



## Why Generators Matter

* Memory efficiency
* Streaming large data
* Cleaner iteration logic



---

## Generator Exhaustion

* Once exhausted, generators cannot be reused
* Create a new generator to iterate again

---



## Mental Rule

> Use generators when data is produced, not stored.

