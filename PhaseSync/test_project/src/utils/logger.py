# @phase utils
# @task logging
# @weight medium

import logging
from datetime import datetime
from typing import Optional

class TaskLogger:
    def __init__(self, log_file: str = "task_operations.log"):
        self.logger = logging.getLogger("TaskLogger")
        self.logger.setLevel(logging.INFO)
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_task_creation(self, task_title: str, priority: int) -> None:
        self.logger.info(f"Created task: {task_title} with priority {priority}")
    
    def log_task_completion(self, task_title: str) -> None:
        self.logger.info(f"Completed task: {task_title}")
    
    def log_error(self, error_message: str) -> None:
        self.logger.error(f"Error occurred: {error_message}") 