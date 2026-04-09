# Day 98 — test_service.py


import tempfile
import unittest
from task_manager.repository import TaskRepository
from task_manager.service import TaskService


class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.repo = TaskRepository(self.temp_file.name)
        self.service = TaskService(self.repo)

    def tearDown(self):
        self.temp_file.close()

    def test_add_task(self):
        task = self.service.add_task("Learn Testing")

        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Learn Testing")
        self.assertFalse(task.completed)

    def test_empty_title_raises(self):
        with self.assertRaises(ValueError):
            self.service.add_task("")

    def test_mark_complete(self):
        task = self.service.add_task("Finish Project")
        updated = self.service.mark_complete(task.id)

        self.assertTrue(updated.completed)

    def test_mark_nonexistent_raises(self):
        with self.assertRaises(ValueError):
            self.service.mark_complete(999)
