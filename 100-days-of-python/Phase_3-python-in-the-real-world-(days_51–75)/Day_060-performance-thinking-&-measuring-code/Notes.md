# Day 60 Notes — Performance Thinking

## The Biggest Performance Mistake

The most common mistake:
"I think this is slow."

Thinking is useless here.
Only measurement matters.

---

## What Performance Actually Means

Performance is about:
- Time
- Memory
- Scalability

Today we focus on **time**.

---

## Premature Optimization (Very Important)

Premature optimization:
- Makes code complex
- Introduces bugs
- Solves imaginary problems

Rule:
> Make it correct.
> Make it clear.
> Then measure.
> Then optimize.

---

## Measuring Time Correctly

### time.time()
- Simple wall-clock measurement
- Good for rough comparisons

### timeit
- Designed for benchmarking
- Runs code multiple times
- More reliable

---

## What to Measure

Measure:
- Hot paths
- Loops
- Repeated operations

Do NOT measure:
- One-time setup
- Logging
- I/O-heavy operations casually

---

## Mental Rule

> If you didn’t measure it,
> you don’t know it.
