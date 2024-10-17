# Task Tracker CLI

Task Tracker is a simple command line interface (CLI) application to track and manage your tasks. This project allows users to add, update, delete tasks, and manage their status. It stores the tasks in a JSON file and handles basic operations like listing tasks by status.

## Features

- **Add Tasks**: Add new tasks with a description.
- **Update Tasks**: Update the description of an existing task.
- **Delete Tasks**: Remove tasks from the list.
- **Mark Task Status**: Mark tasks as `todo`, `in-progress`, or `done`.
- **List Tasks**: Display all tasks or filter tasks by their status (`todo`, `in-progress`, `done`).

## Task Properties

Each task is stored with the following properties in the JSON file:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The status of the task (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

## Requirements

- The application runs directly from the command line.
- Accepts user actions and inputs as arguments.
- Handles errors and edge cases gracefully.
- No external libraries or frameworks are used.

## Usage

Below are examples of how to use the Task Tracker CLI:

### Add a new task

```bash
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Update a task

```bash
task-cli update 1 "Buy groceries and cook dinner"
# Output: Task updated successfully (ID: 1)
```

### Delete a task

```bash
task-cli delete 1
# Output: Task deleted successfully (ID: 1)
```

### Mark a task as in-progress or done

```bash
task-cli mark-in-progress 1
# Output: Task marked as in progress (ID: 1)

task-cli mark-done 1
# Output: Task marked as done (ID: 1)
```

### List all tasks

```bash
task-cli list
```

### List tasks by status

```bash
task-cli list done
# Output: Lists all tasks with status 'done'

task-cli list todo
# Output: Lists all tasks with status 'todo'

task-cli list in-progress
# Output: Lists all tasks with status 'in-progress'
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mikege2/BackendRoadmapJourney.git
cd Task-CLI-Python
```

2. Make the script executable:

```bash
chmod +x task-cli
```

3. Add the CLI to your `PATH` (optional):

This step allows you to run `task-cli` from anywhere in your terminal.

```bash
export PATH=$PATH:/path/to/task-tracker-cli
```

## Acknowledgments

This project is part of the [Task Tracker project](https://roadmap.sh/projects/task-tracker) from the Roadmap.sh programming projects series.

