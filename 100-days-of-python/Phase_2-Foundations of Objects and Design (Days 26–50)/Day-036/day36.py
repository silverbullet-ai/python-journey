# Day 36 — Magic (Dunder) Methods

print("MAGIC (DUNDER) METHODS PRACTICE\n")

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

book1 = Book("Atomic Habits", 320)

print(book1)           # Calls __str__
print(repr(book1))     # Calls __repr__

print("\nDay 36 completed successfully!")