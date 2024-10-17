#!/usr/bin/env python3

from datetime import datetime

class Task:
    id = 1
    
    def __init__(self):
        self.toDoDic = {}

    def add(self, description):
        task_id = f"Task{self.id}"
        self.toDoDic[task_id] = {
            "id": self.id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        print(f"Task added successfully (ID: {self.id})")
        self.id += 1

    def update(self, task_id, description):
        if task_id in self.toDoDic:
            self.toDoDic[task_id]["description"] = description
            self.toDoDic[task_id]["updatedAt"] = datetime.now()
            print(f"Task updated successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete(self, task_id):
        if task_id in self.toDoDic:
            del self.toDoDic[task_id]
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_in_progress(self, task_id):
        if task_id in self.toDoDic:
            self.toDoDic[task_id]["status"] = "in-progress"
            self.toDoDic[task_id]["updatedAt"] = datetime.now()
            print(f"Task marked as In Progress (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_done(self, task_id):
        if task_id in self.toDoDic:
            self.toDoDic[task_id]["status"] = "done"
            self.toDoDic[task_id]["updatedAt"] = datetime.now()
            print(f"Task marked as Done (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")

    def list(self, status):
        for task_id, task in self.toDoDic.items():
            if task['status'] == status:
                print(f"{task_id}: {task['description']} - {task['status']}")

    def print_help(self):
        help_message = """
Welcome to the Interactive Task Manager!
Manage your tasks efficiently using the following commands:

Commands:
  add <description>                Add a new task with the given description.
                                   Example: add "Finish homework"

  update <id> <description>        Update the description of the task with the given ID.
                                   Example: update 1 "Finish math homework"

  delete <id>                      Delete the task with the given ID.
                                   Example: delete 1

  mark-in-progress <id>            Mark the task with the given ID as "in-progress".
                                   Example: mark-in-progress 1

  mark-done <id>                   Mark the task with the given ID as "done".
                                   Example: mark-done 1

  list <status>                    List all tasks with the given status ("todo", "in-progress", or "done").
                                   Example: list todo
                                            list in-progress
                                            list done

  exit                             Exit the task manager.
                                   Example: exit

Notes:
  - <id> refers to the task number, e.g., "1" for Task1.
  - Use quotation marks around descriptions if they contain spaces.
  - Use 'list' with a specific status to filter tasks based on their progress.

Type 'exit' to quit the task manager at any time.

Happy Task Managing!
"""
        print(help_message)

def main():
    task = Task()  # Create a single Task instance for the session
    print("Welcome to the interactive task manager! Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter an operation: ").strip()
        parts = user_input.split(maxsplit=2)
        
        if len(parts) == 0:
            continue

        command = parts[0]
        if command == 'add' and len(parts) > 1:
            task.add(parts[1])
        elif command == 'update' and len(parts) > 2:
            task_id = f"Task{parts[1]}"  # Adjust the ID format
            task.update(task_id, parts[2])
        elif command == 'delete' and len(parts) > 1:
            task_id = f"Task{parts[1]}"  # Adjust the ID format
            task.delete(task_id)
        elif command == 'mark-in-progress' and len(parts) > 1:
            task_id = f"Task{parts[1]}"  # Adjust the ID format
            task.mark_in_progress(task_id)
        elif command == 'mark-done' and len(parts) > 1:
            task_id = f"Task{parts[1]}"  # Adjust the ID format
            task.mark_done(task_id)
        elif command == 'list' and len(parts) > 1:
            task.list(parts[1])
        elif command == 'help':
            task.print_help()
        elif command == 'exit':
            print("Exit successful.")
            break
        else:
            print("Invalid operation. Choose from 'add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list', 'help' or 'exit'.")

if __name__ == '__main__':
    main()
