#!/usr/bin/env python3

import json
import sys
import os

TASK_FILE = 'tasks.json'

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Update an existing task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['description'] = description
            save_tasks(tasks)
            print(f"Task {task_id} updated: {description}")
            return
    print(f"Task {task_id} not found")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != int(task_id)]
    save_tasks(tasks)
    print(f"Task {task_id} deleted")

# Change task status
def change_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(task_id):
            task['status'] = status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

# List tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    for task in tasks:
        if filter_status is None or task['status'] == filter_status:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")

# Main function to handle command line arguments
def main():
    if len(sys.argv) < 2:
        print("Usage: task_tracker.py <command> [<args>]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task_tracker.py add <description>")
        else:
            add_task(" ".join(sys.argv[2:]))
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task_tracker.py update <id> <description>")
        else:
            update_task(sys.argv[2], " ".join(sys.argv[3:]))
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task_tracker.py delete <id>")
        else:
            delete_task(sys.argv[2])
    elif command == "in-progress":
        if len(sys.argv) < 3:
            print("Usage: task_tracker.py in-progress <id>")
        else:
            change_task_status(sys.argv[2], "in progress")
    elif command == "done":
        if len(sys.argv) < 3:
            print("Usage: task_tracker.py done <id>")
        else:
            change_task_status(sys.argv[2], "done")
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        elif sys.argv[2] == "done":
            list_tasks("done")
        elif sys.argv[2] == "todo":
            list_tasks("todo")
        elif sys.argv[2] == "in-progress":
            list_tasks("in progress")
        else:
            print("Usage: task_tracker.py list [done|todo|in-progress]")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
