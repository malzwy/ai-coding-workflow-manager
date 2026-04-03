"""
AI Coding Workflow Manager - Main Manager
"""

import os
from typing import Dict, List, Optional
from pathlib import Path
from dotenv import load_dotenv

from .workflow import Workflow
from .models import ModelConfig


class WorkflowManager:
    """Main workflow manager for AI coding tasks"""

    def __init__(
        self,
        claude_api_key: Optional[str] = None,
        openai_api_key: Optional[str] = None,
        config_file: Optional[str] = None
    ):
        """
        Initialize the workflow manager

        Args:
            claude_api_key: Claude API key (optional, can be set via env)
            openai_api_key: OpenAI API key (optional, can be set via env)
            config_file: Path to configuration file (optional)
        """
        # Load environment variables
        load_dotenv()

        # Initialize model configurations
        self.claude_config = ModelConfig(
            api_key=claude_api_key or os.getenv("CLAUDE_API_KEY"),
            model=os.getenv("CLAUDE_MODEL", "claude-3-opus-20240229"),
            max_tokens=int(os.getenv("CLAUDE_MAX_TOKENS", "4096")),
            temperature=float(os.getenv("CLAUDE_TEMPERATURE", "0.7"))
        )

        self.openai_config = ModelConfig(
            api_key=openai_api_key or os.getenv("OPENAI_API_KEY"),
            model=os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview"),
            max_tokens=int(os.getenv("OPENAI_MAX_TOKENS", "4096")),
            temperature=float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
        )

        # Workflow storage
        self.workflows: Dict[str, Workflow] = {}
        self.active_workflow: Optional[Workflow] = None

        # Configuration
        self.max_concurrent_tasks = int(os.getenv("MAX_CONCURRENT_TASKS", "5"))
        self.default_timeout = int(os.getenv("DEFAULT_WORKFLOW_TIMEOUT", "300"))

        # Output directory
        self.output_dir = Path(os.getenv("OUTPUT_DIR", "output"))
        self.output_dir.mkdir(exist_ok=True)

    def create_workflow(
        self,
        name: str,
        description: str = "",
        template: Optional[str] = None
    ) -> Workflow:
        """
        Create a new workflow

        Args:
            name: Workflow name
            description: Workflow description
            template: Template name to use (optional)

        Returns:
            Workflow instance
        """
        workflow = Workflow(
            name=name,
            description=description,
            manager=self
        )

        # Load template if specified
        if template:
            workflow.load_template(template)

        self.workflows[name] = workflow
        self.active_workflow = workflow

        return workflow

    def get_workflow(self, name: str) -> Optional[Workflow]:
        """
        Get a workflow by name

        Args:
            name: Workflow name

        Returns:
            Workflow instance or None
        """
        return self.workflows.get(name)

    def list_workflows(self) -> List[str]:
        """
        List all workflow names

        Returns:
            List of workflow names
        """
        return list(self.workflows.keys())

    def delete_workflow(self, name: str) -> bool:
        """
        Delete a workflow

        Args:
            name: Workflow name

        Returns:
            True if deleted, False if not found
        """
        if name in self.workflows:
            del self.workflows[name]
            if self.active_workflow and self.active_workflow.name == name:
                self.active_workflow = None
            return True
        return False

    def get_available_templates(self) -> List[str]:
        """
        Get list of available workflow templates

        Returns:
            List of template names
        """
        templates_dir = Path(__file__).parent.parent / "templates"
        if templates_dir.exists():
            return [f.stem for f in templates_dir.glob("*.yaml")]
        return []

    def save_workflow(self, name: str, output_path: Optional[str] = None) -> str:
        """
        Save workflow to file

        Args:
            name: Workflow name
            output_path: Output file path (optional)

        Returns:
            Path to saved file
        """
        workflow = self.get_workflow(name)
        if not workflow:
            raise ValueError(f"Workflow '{name}' not found")

        if output_path is None:
            output_path = self.output_dir / f"{name}.json"

        workflow.save(str(output_path))
        return str(output_path)

    def load_workflow(self, file_path: str) -> Workflow:
        """
        Load workflow from file

        Args:
            file_path: Path to workflow file

        Returns:
            Loaded workflow
        """
        workflow = Workflow.load(file_path, manager=self)
        self.workflows[workflow.name] = workflow
        return workflow

    def __repr__(self) -> str:
        return f"WorkflowManager(workflows={len(self.workflows)}, active={self.active_workflow.name if self.active_workflow else None})"
