"""
Example: Using Workflow Templates

This example demonstrates how to use pre-defined workflow templates
to quickly set up common coding workflows.
"""

import os
from ai_coding_workflow import WorkflowManager


def main():
    """Main example function"""

    # Initialize the workflow manager
    manager = WorkflowManager(
        claude_api_key=os.getenv("CLAUDE_API_KEY"),
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    # List available templates
    templates = manager.get_available_templates()
    print("Available templates:")
    for template in templates:
        print(f"  - {template}")

    # Create a workflow from a template
    workflow = manager.create_workflow(
        name="code_review_from_template",
        template="code_review"
    )

    print(f"\nCreated workflow from template: {workflow.name}")
    print(f"Description: {workflow.description}")
    print(f"Number of tasks: {len(workflow.tasks)}")

    # List tasks in the workflow
    print("\nTasks:")
    for task in workflow.tasks:
        print(f"  - {task.task_type} ({task.model})")

    # Execute the workflow
    print("\nExecuting workflow...")
    results = workflow.execute()

    # Print results
    print("\n=== Results ===")
    for task_id, result in results.items():
        print(f"\nTask {task_id}:")
        print(f"  Status: {result.get('status')}")
        if result.get('error'):
            print(f"  Error: {result.get('error')}")
        else:
            print(f"  Output: {result.get('output')}")


if __name__ == "__main__":
    main()
