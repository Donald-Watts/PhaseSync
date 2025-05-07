# @phase core
# @task task_management
# @weight high

from datetime import datetime
from typing import List, Dict, Optional

class Task:
    def __init__(self, title: str, description: str, priority: int = 1):
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        
    def add_task(self, title: str, description: str, priority: int = 1) -> Task:
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task
    
    def complete_task(self, task_index: int) -> bool:
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            return True
        return False
    
    def get_high_priority_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.priority > 2 and not task.completed]
    
    def get_task_summary(self) -> Dict[str, int]:
        return {
            'total': len(self.tasks),
            'completed': len([t for t in self.tasks if t.completed]),
            'pending': len([t for t in self.tasks if not t.completed])
        } 