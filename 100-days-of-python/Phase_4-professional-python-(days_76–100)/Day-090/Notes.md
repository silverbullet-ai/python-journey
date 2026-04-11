# Day 90 Notes — Tooling Overview & Code Quality Discipline

## Why Tooling Exists

As projects grow:
- Code is written by many people
- Style differences multiply
- Bugs hide in plain sight

Tooling exists to:
- Enforce consistency
- Catch obvious mistakes early
- Reduce human review burden

Tools do not replace thinking.
They support it.

---

## The Three Core Tool Categories

### Formatters
Examples: black

Purpose:
- Enforce consistent code style
- Remove debates about formatting

Rule:
> Formatting should be automatic and boring.

---

### Linters
Examples: flake8, pylint

Purpose:
- Detect suspicious patterns
- Warn about unused variables
- Catch common logic mistakes

Linters highlight problems,
they do not fix them for you.

---

### Type Checkers
Examples: mypy (conceptual)

Purpose:
- Catch type mismatches early
- Improve code clarity
- Document intent

Type checking is about correctness,
not verbosity.

---

## Why Professionals Trust Tools

Tools are:
- Consistent
- Impartial
- Tireless

Humans:
- Miss things
- Get tired
- Have style preferences

Good teams let tools handle the obvious,
and humans handle the hard decisions.

---

## When Tooling Goes Wrong

Tooling becomes harmful when:
- Rules are blindly followed
- Warnings are ignored completely
- Tools replace understanding

Tools should:
- Guide
- Warn
- Enforce baseline quality

They should not:
- Dictate design
- Hide complexity

---

## Mental Rule

> Tools enforce standards.
> Engineers make decisions.

---

## What to Do Today

1. Read the notes slowly

2. Look at `sample.py`

3. Ask yourself:

 	- What could a linter warn about?
 	- What would a formatter change?
 	- What type hints could clarify intent?

4. Do not install tools yet

This day is about mental models, not commands.