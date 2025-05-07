# Task Management System

A simple task management system demonstrating different architectural phases and components.

## Project Structure

```
test_project/
├── src/
│   ├── core/
│   │   └── task_manager.py    # Core task management functionality
│   └── utils/
│       └── logger.py          # Logging utilities
└── tests/
    └── test_task_manager.py   # Unit tests
```

## Features

1. Task Management
   - Create tasks with title, description, and priority
   - Mark tasks as complete
   - Get high priority tasks
   - Get task summary statistics

2. Logging
   - Log task creation and completion
   - Error logging
   - Both file and console output

3. Testing
   - Comprehensive unit tests
   - Test coverage for all major functionality

## Running the Tests

```bash
python -m unittest tests/test_task_manager.py
```

## Example Usage

```python
from src.core.task_manager import TaskManager
from src.utils.logger import TaskLogger

# Initialize components
task_manager = TaskManager()
logger = TaskLogger()

# Create a task
task = task_manager.add_task("Important Task", "This needs to be done", 3)
logger.log_task_creation(task.title, task.priority)

# Complete the task
task_manager.complete_task(0)
logger.log_task_completion(task.title)

# Get summary
summary = task_manager.get_task_summary()
print(f"Task Summary: {summary}")
``` 