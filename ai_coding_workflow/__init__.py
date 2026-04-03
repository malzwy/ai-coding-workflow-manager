"""
AI Coding Workflow Manager - Core Package
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .manager import WorkflowManager
from .workflow import Workflow
from .task import Task
from .models import ModelConfig

__all__ = [
    "WorkflowManager",
    "Workflow",
    "Task",
    "ModelConfig",
]
