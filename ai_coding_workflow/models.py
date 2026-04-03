"""
AI Coding Workflow Manager - Models
"""

from typing import Optional
from pydantic import BaseModel, Field


class ModelConfig(BaseModel):
    """Configuration for AI models"""

    api_key: str = Field(..., description="API key for the model")
    model: str = Field(..., description="Model name")
    max_tokens: int = Field(default=4096, description="Maximum tokens for response")
    temperature: float = Field(default=0.7, description="Temperature for generation")

    class Config:
        """Pydantic config"""
        json_schema_extra = {
            "example": {
                "api_key": "your-api-key",
                "model": "claude-3-opus-20240229",
                "max_tokens": 4096,
                "temperature": 0.7
            }
        }


class TaskResult(BaseModel):
    """Result of a task execution"""

    task_id: str = Field(..., description="Task ID")
    model: str = Field(..., description="Model used")
    task_type: str = Field(..., description="Type of task")
    status: str = Field(..., description="Task status")
    output: Optional[str] = Field(None, description="Task output")
    error: Optional[str] = Field(None, description="Error message if failed")
    execution_time: Optional[float] = Field(None, description="Execution time in seconds")

    class Config:
        """Pydantic config"""
        json_schema_extra = {
            "example": {
                "task_id": "123e4567-e89b-12d3-a456-426614174000",
                "model": "claude",
                "task_type": "code_review",
                "status": "completed",
                "output": "Code review completed successfully",
                "error": None,
                "execution_time": 2.5
            }
        }


class WorkflowResult(BaseModel):
    """Result of a workflow execution"""

    workflow_name: str = Field(..., description="Workflow name")
    status: str = Field(..., description="Workflow status")
    total_tasks: int = Field(..., description="Total number of tasks")
    completed_tasks: int = Field(..., description="Number of completed tasks")
    failed_tasks: int = Field(..., description="Number of failed tasks")
    results: dict = Field(..., description="Task results")
    execution_time: Optional[float] = Field(None, description="Total execution time in seconds")

    class Config:
        """Pydantic config"""
        json_schema_extra = {
            "example": {
                "workflow_name": "code_review",
                "status": "completed",
                "total_tasks": 3,
                "completed_tasks": 3,
                "failed_tasks": 0,
                "results": {},
                "execution_time": 7.5
            }
        }
