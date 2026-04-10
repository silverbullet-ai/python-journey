# Day 50 — Final OOP Project (Phase 2)

print("FINAL OOP PROJECT — PHASE 2\n")

class Task:
    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def display(self):
        status = "Done" if self.completed else "Pending"
        print(f"[{status}] {self.task_id}: {self.title}")


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task.task_id in self.tasks:
            raise ValueError("Task ID already exists")
        self.tasks[task.task_id] = task

    def complete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("Task not found")
        self.tasks[task_id].mark_done()

    def show_all(self):
        if not self.tasks:
            print("No tasks available")
        for task in self.tasks.values():
            task.display()


# Demo
manager = TaskManager()

manager.add_task(Task(1, "Learn OOP foundations"))
manager.add_task(Task(2, "Build mini project"))
manager.add_task(Task(3, "Reflect on Phase 2"))

manager.complete_task(1)

print("\nAll Tasks:")
manager.show_all()

print("\nDay 50 completed successfully!")
