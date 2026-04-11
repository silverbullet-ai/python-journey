# Day 97 — models.py
# Defines the Task domain model


from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
