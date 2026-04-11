# Day 97 — test_repository.py


import tempfile
import unittest
from task_manager.repository import TaskRepository
from task_manager.models import Task


class TestTaskRepository(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.repo = TaskRepository(self.temp_file.name)

    def tearDown(self):
        self.temp_file.close()

    def test_file_created_if_missing(self):
        tasks = self.repo.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load_tasks(self):
        tasks = [Task(id=1, title="Test Task")]
        self.repo.save_tasks(tasks)

        loaded = self.repo.load_tasks()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].title, "Test Task")
        self.assertFalse(loaded[0].completed)


if __name__ == "__main__":
    unittest.main()
