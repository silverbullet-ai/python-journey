# Day 92 Notes — Code Review Mindset

## Why Code Reviews Exist

Code reviews are not:
- Exams
- Competitions
- Personal critiques

They exist to:
- Improve code quality
- Share knowledge
- Catch bugs early
- Align understanding across a team

A good review protects the system,
not the reviewer’s ego.

---

## How to Read Code in a Review

Read code in layers:

1. What problem is this trying to solve?
2. Does the structure match the intent?
3. Is the behavior correct?
4. Are edge cases handled?
5. Is the code readable and maintainable?

Do not start with syntax.
Start with intent.

---

## What to Look For First

Prioritize:
- Correctness
- Clarity
- Simplicity
- Safety

Deprioritize:
- Personal style preferences
- Micro-optimizations
- Minor formatting (tools handle this)

---

## Good Review Comments

Good comments:
- Ask questions
- Explain reasoning
- Suggest alternatives
- Stay respectful

Examples:
- “What happens if this value is None?”
- “Could this be simplified?”
- “Is this behavior intentional?”

---

## Bad Review Comments

Avoid:
- “This is wrong.”
- “I don’t like this.”
- “Rewrite this.”
- Nitpicking style manually

Reviews are conversations, not verdicts.

---

## Approving vs Blocking

Block a change when:
- Behavior is incorrect
- Edge cases are missing
- The design is risky

Do not block for:
- Naming preferences
- Formatting issues
- Non-critical improvements

---

## Mental Rule

> Review code as if you will
> maintain it in six months.

---

## What to Do Today
1. Read review_example.py

2. Answer for yourself:

	- What assumptions does this code make?
	- What could go wrong?
	- What would you comment in a review?

3. Focus on clarity and behavior, not style

No need to change code today.
