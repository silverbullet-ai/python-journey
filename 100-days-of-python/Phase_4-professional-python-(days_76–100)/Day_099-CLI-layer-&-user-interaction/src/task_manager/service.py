# Day 98 — service.py
# Business logic layer


from typing import List
from task_manager.models import Task
from task_manager.repository import TaskRepository


class TaskService:

    def __init__(self, repository: TaskRepository):
        self._repo = repository

    def list_tasks(self) -> List[Task]:
        return self._repo.load_tasks()

    def add_task(self, title: str) -> Task:
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        tasks = self._repo.load_tasks()
        next_id = self._generate_next_id(tasks)

        new_task = Task(id=next_id, title=title.strip())
        tasks.append(new_task)
        self._repo.save_tasks(tasks)

        return new_task

    def mark_complete(self, task_id: int) -> Task:
        tasks = self._repo.load_tasks()

        for task in tasks:
            if task.id == task_id:
                task.completed = True
                self._repo.save_tasks(tasks)
                return task

        raise ValueError("Task not found")

    def _generate_next_id(self, tasks: List[Task]) -> int:
        if not tasks:
            return 1
        return max(task.id for task in tasks) + 1
