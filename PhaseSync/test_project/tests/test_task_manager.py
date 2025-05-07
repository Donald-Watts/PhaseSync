# @phase tests
# @task unit_testing
# @weight high

import unittest
from src.core.task_manager import TaskManager, Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        
    def test_add_task(self):
        task = self.task_manager.add_task("Test Task", "Test Description", 3)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, 3)
        
    def test_complete_task(self):
        self.task_manager.add_task("Test Task", "Test Description")
        self.assertTrue(self.task_manager.complete_task(0))
        self.assertTrue(self.task_manager.tasks[0].completed)
        
    def test_get_high_priority_tasks(self):
        self.task_manager.add_task("Low Priority", "Description", 1)
        self.task_manager.add_task("High Priority", "Description", 3)
        high_priority_tasks = self.task_manager.get_high_priority_tasks()
        self.assertEqual(len(high_priority_tasks), 1)
        self.assertEqual(high_priority_tasks[0].title, "High Priority")
        
    def test_get_task_summary(self):
        self.task_manager.add_task("Task 1", "Description")
        self.task_manager.add_task("Task 2", "Description")
        self.task_manager.complete_task(0)
        summary = self.task_manager.get_task_summary()
        self.assertEqual(summary['total'], 2)
        self.assertEqual(summary['completed'], 1)
        self.assertEqual(summary['pending'], 1)

if __name__ == '__main__':
    unittest.main() 