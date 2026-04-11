# Day 67 Notes — Generator Pipelines & Streaming

## Generators as Pipelines

A generator is not just a function.
It is a **stage in a pipeline**.

Each stage:
- Receives values
- Transforms or filters them
- Passes them forward

No stage needs to know the whole dataset.

---

## Why Pipelines Matter

Pipelines allow:
- Constant memory usage
- Incremental processing
- Clean separation of concerns
- Easy composition

This is how:
- Log processors
- File readers
- Stream handlers
are built.

---

## Example Pipeline Stages

1. Source → produces data
2. Filter → removes unwanted data
3. Transform → changes data
4. Sink → consumes results

Each stage is a generator.

---

## Backpressure (Conceptual)

Backpressure means:
- Downstream is slower than upstream
- Data should not pile up uncontrollably

Generators naturally handle this because:
- They produce values only when requested

No buffering explosion.

---

## When Generators Are Ideal

Generators are ideal when:
- Data is large
- Data is infinite or unbounded
- Processing is sequential
- Memory stability matters

---

## Mental Rule

> Generators move data.
> Lists store data.
