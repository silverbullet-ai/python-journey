# Day 99 — cli.py
# Command-line interface for Task Manager


import argparse
from task_manager.repository import TaskRepository
from task_manager.service import TaskService
from task_manager.logging_config import configure_logging


def main():
    configure_logging()
    parser = argparse.ArgumentParser(description="CLI Task Manager")

    parser.add_argument(
        "--storage",
        type=str,
        default="tasks.json",
        help="Path to tasks storage file"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark task complete")
    complete_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    repo = TaskRepository(args.storage)
    service = TaskService(repo)

    try:
        if args.command == "add":
            task = service.add_task(args.title)
            print(f"Added task [{task.id}] {task.title}")

        elif args.command == "list":
            tasks = service.list_tasks()
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                status = "DONE" if task.completed else "PENDING"
                print(f"[{task.id}] [{status}] {task.title}")

        elif args.command == "complete":
            task = service.mark_complete(args.id)
            print(f"Task [{task.id}] marked as complete.")

        else:
            parser.print_help()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
