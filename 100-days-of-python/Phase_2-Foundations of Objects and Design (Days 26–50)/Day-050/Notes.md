# Day 50 Notes — Phase 2 Revision (Foundations of Objects and Design)

## Phase 2 Objective (Big Picture)

Phase 2 was about moving from:
- Writing scripts  
to  
- Designing structured, predictable systems

The focus was **how Python works internally** and **how to model real-world problems using OOP**.

---

## 1. Object Model

- Everything in Python is an object
- Objects have:
  - Identity
  - Type
  - Value
- Variables store **references**, not values
- Mutability defines behavior

Key idea:
> You don’t control values — you control references to objects.

---

## 2. Classes & Instances

- Class → blueprint
- Instance → real object
- Multiple instances can be created from one class
- Each instance has its own data

Key idea:
> A class describes what an object *can be*.  
> An instance is what the object *actually is*.

---

## 3. Constructors & `self`

- `__init__` initializes objects
- `self` refers to the current instance
- Instance attributes live inside the object

Key idea:
> `self` is the object itself.

---

## 4. Instance Variables vs Class Variables

- Instance variables → unique per object
- Class variables → shared across all objects
- Attribute lookup:
  1. Instance
  2. Class
  3. Parent classes

Key idea:
> Bugs happen when shared data is treated as personal data.

---

## 5. Methods & Behavior

- Methods are functions inside classes
- Methods define **what objects do**
- Behavior belongs with data

Key idea:
> Objects exist to perform actions, not just store data.

---

## 6. Encapsulation

- Public → no underscore
- Protected → single underscore (`_`)
- Private → double underscore (`__`)
- Python uses **convention over enforcement**

Key idea:
> Encapsulation is about intent, not secrecy.

---

## 7. Composition vs Inheritance

- Inheritance → *is-a* relationship
- Composition → *has-a* relationship
- Composition is generally more flexible

Key idea:
> Prefer composition over inheritance unless identity truly matters.

---

## 8. Inheritance, `super()` & Overriding

- Child classes extend parent behavior
- `super()` connects parent and child safely
- Method overriding enables specialization

Key idea:
> Inheritance is for extension, not duplication.

---

## 9. Polymorphism

### Inheritance-based
- Same method name, different behavior

### Duck typing
- Behavior matters more than class type

Key idea:
> Don’t ask what an object *is*. Ask what it *can do*.

---

## 10. Magic (Dunder) Methods

- Special methods called automatically by Python
- Examples:
  - `__init__`
  - `__str__`
  - `__repr__`
  - `__eq__`
  - `__add__`

Key idea:
> Dunder methods define how your object behaves in Python’s world.

---

## 11. Operator Overloading

- Operators map to magic methods
- Enables expressive domain models
- Must be used carefully

Key idea:
> Operators should clarify meaning, not hide logic.

---

## 12. Dataclasses

- Reduce boilerplate for data-heavy classes
- Auto-generate common methods
- Can include custom behavior
- Can be immutable (`frozen=True`)

Key idea:
> Use dataclasses when data matters more than behavior.

---

## 13. Immutability

- Immutable objects cannot be changed
- New objects are created instead
- Reduces bugs and side effects

Key idea:
> Mutable for behavior. Immutable for values.

---

## 14. Iterators & Generators

- Iterables create iterators
- Iterators produce values
- Generators simplify iterator creation using `yield`
- Enable lazy, memory-efficient execution

Key idea:
> Produce data when needed, not all at once.

---

## 15. Decorators (Functions & Classes)

- Decorators wrap behavior without modifying logic
- Function decorators → simple, stateless
- Class decorators → stateful, configurable

Key idea:
> Decorators modify behavior, not purpose.

---

## 16. Context Managers

- Manage resources safely using `with`
- Guarantee cleanup
- Use `__enter__` / `__exit__` or `contextlib`

Key idea:
> Discipline enforced by design is better than discipline by habit.

---

## 17. Mini Design Patterns

- Factory
- Strategy
- Composition
- Patterns are concepts, not templates

Key idea:
> Patterns describe intent, not structure.

---

## 18. Refactoring Procedural → OOP

- Identify responsibilities
- Group data with behavior
- Improve structure without changing behavior

Key idea:
> Refactoring is cleanup with intent.

---

## 19. Error Handling in OOP

- Methods raise exceptions
- Systems handle exceptions
- Custom exceptions improve clarity

Key idea:
> Good systems define how failure happens.

---

## Phase 2 Final Takeaway

Phase 2 transformed Python from:
- Syntax → Structure  
- Code → Systems  
- Working programs → Well-designed programs

OOP is no longer a feature.
It is a **way of thinking**.

Phase 2 is complete.
