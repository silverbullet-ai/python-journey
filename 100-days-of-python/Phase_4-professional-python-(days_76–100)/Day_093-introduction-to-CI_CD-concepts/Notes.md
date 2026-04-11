# Day 93 Notes — Introduction to CI/CD Concepts

## What CI/CD Really Means

CI/CD stands for:
- Continuous Integration
- Continuous Delivery (or Deployment)

At its core, CI/CD is about:
- Reducing human error
- Increasing confidence
- Making change safe

It is not about speed alone.
It is about **reliability**.

---

## Why Continuous Integration Exists

Without CI:
- Code is merged late
- Bugs pile up
- Integration becomes painful

Continuous Integration means:
- Changes are merged frequently
- Tests run automatically
- Problems are detected early

CI answers the question:
“Is the system still healthy after this change?”

---

## Why Continuous Delivery Exists

Even if code works:
- Manual releases are risky
- Steps are forgotten
- Environments drift

Continuous Delivery means:
- The system is always in a releasable state
- Release steps are automated
- Confidence replaces fear

CD answers:
“Can this be safely released right now?”

---

## CI/CD Is About Trust

CI/CD builds trust between:
- Developers and the codebase
- Teams and deployments
- Humans and automation

If automation says “green,”
teams move forward confidently.

---

## What CI/CD Is NOT

CI/CD is not:
- A tool
- A YAML file
- GitHub Actions specifically
- Magic

Those are implementations.
CI/CD is a **discipline**.

---

## Mental Rule

> If a change cannot be verified automatically,
> it will eventually break something.

---

## What to Do Today
1. Read the notes slowly
2. Reflect on:	
	- How many steps you currently do manually
	- Where mistakes could creep in
3. Do not set up CI yet

Understanding must come before automation.
