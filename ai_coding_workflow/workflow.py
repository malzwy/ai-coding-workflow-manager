"""
AI Coding Workflow Manager - Workflow
"""

import json
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime

from .task import Task
from .manager import WorkflowManager


class Workflow:
    """Represents a workflow with multiple tasks"""

    def __init__(
        self,
        name: str,
        description: str = "",
        manager: Optional[WorkflowManager] = None
    ):
        """
        Initialize a workflow

        Args:
            name: Workflow name
            description: Workflow description
            manager: Workflow manager instance
        """
        self.name = name
        self.description = description
        self.manager = manager
        self.tasks: List[Task] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.status = "created"
        self.results: Dict[str, Any] = {}

    def add_task(
        self,
        model: str,
        task_type: str,
        **kwargs
    ) -> Task:
        """
        Add a task to the workflow

        Args:
            model: Model to use (claude or openai)
            task_type: Type of task
            **kwargs: Additional task parameters

        Returns:
            Created task
        """
        task = Task(
            model=model,
            task_type=task_type,
            **kwargs
        )
        self.tasks.append(task)
        self.updated_at = datetime.now()
        return task

    def remove_task(self, task_id: str) -> bool:
        """
        Remove a task from the workflow

        Args:
            task_id: Task ID to remove

        Returns:
            True if removed, False if not found
        """
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                self.updated_at = datetime.now()
                return True
        return False

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Get a task by ID

        Args:
            task_id: Task ID

        Returns:
            Task or None
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> List[str]:
        """
        List all task IDs

        Returns:
            List of task IDs
        """
        return [task.id for task in self.tasks]

    def execute(self) -> Dict[str, Any]:
        """
        Execute all tasks in the workflow

        Returns:
            Dictionary of results
        """
        self.status = "running"
        results = {}

        for task in self.tasks:
            try:
                result = task.execute()
                results[task.id] = result
            except Exception as e:
                results[task.id] = {
                    "error": str(e),
                    "status": "failed"
                }

        self.results = results
        self.status = "completed"
        self.updated_at = datetime.now()

        return results

    def load_template(self, template_name: str) -> None:
        """
        Load a workflow template

        Args:
            template_name: Name of template to load
        """
        templates_dir = Path(__file__).parent.parent / "templates"
        template_file = templates_dir / f"{template_name}.yaml"

        if template_file.exists():
            import yaml
            with open(template_file, 'r') as f:
                template_data = yaml.safe_load(f)

            self.description = template_data.get("description", "")

            for task_data in template_data.get("tasks", []):
                self.add_task(**task_data)

    def save(self, file_path: str) -> None:
        """
        Save workflow to file

        Args:
            file_path: Path to save workflow
        """
        data = {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "status": self.status,
            "tasks": [task.to_dict() for task in self.tasks],
            "results": self.results
        }

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load(cls, file_path: str, manager: Optional[WorkflowManager] = None) -> 'Workflow':
        """
        Load workflow from file

        Args:
            file_path: Path to workflow file
            manager: Workflow manager instance

        Returns:
            Loaded workflow
        """
        with open(file_path, 'r') as f:
            data = json.load(f)

        workflow = cls(
            name=data["name"],
            description=data.get("description", ""),
            manager=manager
        )

        workflow.created_at = datetime.fromisoformat(data["created_at"])
        workflow.updated_at = datetime.fromisoformat(data["updated_at"])
        workflow.status = data.get("status", "created")
        workflow.results = data.get("results", {})

        for task_data in data.get("tasks", []):
            task = Task.from_dict(task_data)
            workflow.tasks.append(task)

        return workflow

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert workflow to dictionary

        Returns:
            Dictionary representation
        """
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "status": self.status,
            "tasks": [task.to_dict() for task in self.tasks],
            "results": self.results
        }

    def __repr__(self) -> str:
        return f"Workflow(name={self.name}, tasks={len(self.tasks)}, status={self.status})"
