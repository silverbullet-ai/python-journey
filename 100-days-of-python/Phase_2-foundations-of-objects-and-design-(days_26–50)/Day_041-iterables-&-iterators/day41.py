# Day 41 — Iterables & Iterators

print("ITERABLES & ITERATORS PRACTICE\n")

nums = [10, 20, 30]

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

print("\n------------------\n")

class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(5)

for num in counter:
    print(num)
