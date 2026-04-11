# Day 91 Notes — Git Discipline

## Why Git History Matters

Git history is not a backup.  
It is a record of decisions.

A good history allows others to:
- Understand why changes were made  
- Review work efficiently  
- Revert safely  
- Trust the codebase  

A bad history creates confusion and risk.

---

## Commits Are Messages to Humans

A commit message should explain:
- What changed  
- Why it changed  

It should NOT:
- Describe file names only  
- Contain noise or jokes  
- Hide multiple unrelated changes  

Think of commits as documentation.

---

## Characteristics of a Good Commit

A good commit is:
- Small  
- Focused  
- Reversible  
- Understandable on its own  

Rule:
> One logical change per commit.

---

## Commit Message Structure

Recommended format:

```
<Short summary>

Optional explanation of why
the change was necessary.
```

### Example

```
Day 91: clarify Git discipline concepts

Explain why commit history matters
and how small commits improve review.
```

---

## What to Avoid

Avoid commits like:
- "fix"  
- "updates"  
- "final"  
- "working now"  

These convey no intent.

---

## When to Commit

Commit when:
- A logical unit of work is complete  
- Tests pass  
- The change can be explained clearly  

Do not commit:
- Half-broken code  
- Multiple unrelated changes together  

---

## Mental Rule

> If you cannot explain a commit clearly,  
> it probably should not exist.

---

## What to Do Today

- Read the notes carefully  
- Look at your own recent commit history  

Ask yourself:
- Can I understand what each commit did?  
- Would someone else understand it?  

Do not rewrite history yet.  
Today is about **awareness**, not action.


