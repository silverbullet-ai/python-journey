# Day 41 Notes — Iterables \& Iterators



## What Is an Iterable?

* An iterable is an object that can be looped over
* It implements the `\_\_iter\_\_()` method



Examples:

* `list`
* `tuple`
* `string`
* `dictionary`



```python
nums = \[1, 2, 3]
iter(nums)
```



---

## What Is an Iterator?

* An iterator is an object that produces values **one at a time**
* It implements:

  * `\_\_iter\_\_()`
  * `\_\_next\_\_()`



```python
it = iter(nums)
print(next(it))
```



---

## Iterable vs Iterator



| Iterable | Iterator |
|--------|----------|
| Can create iterators | Produces values |
| Has `\_\_iter\_\_()` | Has `\_\_iter\_\_()` and `\_\_next\_\_()` |
| Reusable | Exhausted after use |



---

## How a `for` Loop Works Internally



```python
for x in nums:
    print(x)
```



Internally:

1. `iter(nums)` is called
2. `\_\_next\_\_()` is called repeatedly
3. Loop stops on `StopIteration`



---

## Writing a Custom Iterator



```python
class CountUp:
    def \_\_init\_\_(self, limit):
        self.limit = limit
        self.current = 1

    def \_\_iter\_\_(self):
        return self

    def \_\_next\_\_(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
```



---

## Why Iterators Matter

* Memory efficiency
* Streaming data
* Foundation for generators
* Used everywhere in Python



---

## Mental Rule

> Iterables create iterators.  
> Iterators produce values.

