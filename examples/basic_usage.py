"""
Example: Basic Workflow Usage

This example demonstrates how to use the AI Coding Workflow Manager
to create and execute a simple code review workflow.
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

    # Create a new workflow
    workflow = manager.create_workflow(
        name="my_code_review",
        description="Review my Python code"
    )

    # Add tasks to the workflow
    workflow.add_task(
        model="claude",
        task_type="code_review",
        file_path="src/main.py",
        check_style=True,
        check_security=True
    )

    workflow.add_task(
        model="openai",
        task_type="security_audit",
        file_path="src/main.py",
        deep_scan=True
    )

    # Execute the workflow
    print(f"Executing workflow: {workflow.name}")
    print(f"Number of tasks: {len(workflow.tasks)}")

    results = workflow.execute()

    # Print results
    print("\n=== Results ===")
    for task_id, result in results.items():
        print(f"\nTask {task_id}:")
        print(f"  Status: {result.get('status')}")
        print(f"  Output: {result.get('output')}")

    # Save the workflow
    output_path = manager.save_workflow("my_code_review")
    print(f"\nWorkflow saved to: {output_path}")


if __name__ == "__main__":
    main()
