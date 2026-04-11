# Day 97 — repository.py
# Handles JSON persistence for tasks


import json
from pathlib import Path
from typing import List
from task_manager.models import Task


class TaskRepository:
    def __init__(self, storage_path: str):
        self._path = Path(storage_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        if not self._path.exists():
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.write_text("[]")

    def load_tasks(self) -> List[Task]:
        try:
            content = self._path.read_text().strip()
            if not content:
                return []
            data = json.loads(content)
            return [Task(**item) for item in data]
        except json.JSONDecodeError:
            return []
        
    def save_tasks(self, tasks: List[Task]) -> None:
        data = [task.__dict__ for task in tasks]
        self._path.write_text(json.dumps(data, indent=2))
