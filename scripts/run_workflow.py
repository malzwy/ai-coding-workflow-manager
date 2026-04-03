#!/usr/bin/env python3
"""
AI Coding Workflow Manager - CLI Tool

Command-line interface for managing AI coding workflows.
"""

import click
import os
import sys
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from ai_coding_workflow import WorkflowManager

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """AI Coding Workflow Manager - CLI Tool"""
    pass


@cli.command()
@click.option('--claude-key', envvar='CLAUDE_API_KEY', help='Claude API key')
@click.option('--openai-key', envvar='OPENAI_API_KEY', help='OpenAI API key')
def init(claude_key, openai_key):
    """Initialize a new workflow manager"""
    console.print("[bold green]Initializing AI Coding Workflow Manager...[/bold green]")

    manager = WorkflowManager(
        claude_api_key=claude_key,
        openai_api_key=openai_key
    )

    console.print(f"[green]✓[/green] Workflow manager initialized")
    console.print(f"  Available templates: {len(manager.get_available_templates())}")
    console.print(f"  Max concurrent tasks: {manager.max_concurrent_tasks}")


@cli.command()
@click.option('--name', required=True, help='Workflow name')
@click.option('--description', default='', help='Workflow description')
@click.option('--template', help='Template to use')
def create(name, description, template):
    """Create a new workflow"""
    console.print(f"[bold blue]Creating workflow: {name}[/bold blue]")

    manager = WorkflowManager()

    workflow = manager.create_workflow(
        name=name,
        description=description,
        template=template
    )

    console.print(f"[green]✓[/green] Workflow created")
    console.print(f"  Name: {workflow.name}")
    console.print(f"  Description: {workflow.description}")
    console.print(f"  Tasks: {len(workflow.tasks)}")


@cli.command()
def list():
    """List all workflows"""
    manager = WorkflowManager()
    workflows = manager.list_workflows()

    if not workflows:
        console.print("[yellow]No workflows found[/yellow]")
        return

    table = Table(title="Workflows")
    table.add_column("Name", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Tasks", justify="right")
    table.add_column("Status", style="green")

    for name in workflows:
        workflow = manager.get_workflow(name)
        table.add_row(
            workflow.name,
            workflow.description[:50] + "..." if len(workflow.description) > 50 else workflow.description,
            str(len(workflow.tasks)),
            workflow.status
        )

    console.print(table)


@cli.command()
@click.option('--name', required=True, help='Workflow name')
def execute(name):
    """Execute a workflow"""
    console.print(f"[bold yellow]Executing workflow: {name}[/bold yellow]")

    manager = WorkflowManager()
    workflow = manager.get_workflow(name)

    if not workflow:
        console.print(f"[red]✗[/red] Workflow '{name}' not found")
        sys.exit(1)

    console.print(f"  Tasks: {len(workflow.tasks)}")

    results = workflow.execute()

    console.print(f"\n[green]✓[/green] Workflow completed")
    console.print(f"  Status: {workflow.status}")

    for task_id, result in results.items():
        status = result.get('status', 'unknown')
        status_color = 'green' if status == 'completed' else 'red'
        console.print(f"  Task {task_id[:8]}: [{status_color}]{status}[/{status_color}]")


@cli.command()
@click.option('--name', required=True, help='Workflow name')
@click.option('--output', help='Output file path')
def save(name, output):
    """Save a workflow to file"""
    manager = WorkflowManager()
    output_path = manager.save_workflow(name, output)

    console.print(f"[green]✓[/green] Workflow saved to: {output_path}")


@cli.command()
@click.option('--file', required=True, help='Workflow file to load')
def load(file):
    """Load a workflow from file"""
    manager = WorkflowManager()
    workflow = manager.load_workflow(file)

    console.print(f"[green]✓[/green] Workflow loaded")
    console.print(f"  Name: {workflow.name}")
    console.print(f"  Tasks: {len(workflow.tasks)}")


@cli.command()
def templates():
    """List available templates"""
    manager = WorkflowManager()
    templates = manager.get_available_templates()

    if not templates:
        console.print("[yellow]No templates found[/yellow]")
        return

    table = Table(title="Available Templates")
    table.add_column("Template", style="cyan")
    table.add_column("Description", style="magenta")

    for template in templates:
        table.add_row(template, "Workflow template")

    console.print(table)


if __name__ == "__main__":
    cli()
