# Day 63 Notes — Data Structures & Performance

## Why Data Structures Matter

Performance problems are often caused by:
- Using the wrong data structure
- Not the wrong algorithm

Choosing the right structure can change:
- O(n) → O(1)
- Seconds → milliseconds

---

## List (`list`)

Best for:
- Ordered data
- Iteration
- Small collections

Costly for:
- Membership checks (`x in list`)
- Frequent removals

Time complexity:
- Access by index → O(1)
- Membership test → O(n)

---

## Set (`set`)

Best for:
- Membership checks
- Uniqueness
- Fast lookups

Trade-offs:
- No ordering
- No duplicates

Time complexity:
- Membership test → O(1) average

---

## Dict (`dict`)

Best for:
- Key → value mapping
- Fast lookups by key
- Caching and indexing

Time complexity:
- Lookup by key → O(1) average

---

## Choosing the Right Structure

Question to ask:
- Do I care about order? → list
- Do I care about uniqueness / presence? → set
- Do I need mapping? → dict

Habit is expensive.
Intent is cheap.

---

## Type Hints & Data Structures (Important)

Type hints clarify **how data is meant to be used**.

Examples:
```python
numbers: list[int]
visited_ids: set[int]
user_scores: dict[str, int]
```

These are not restrictions.
They are **design signals**.

---

## Mental Rule

> If you’re using a list for membership checks,
> you’re probably doing it wrong.
