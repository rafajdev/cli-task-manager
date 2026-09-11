# Task Manager CLI

A small Python CLI for keeping track of tasks from the terminal.

You can add tasks, list them, mark them as completed, or delete them. Tasks are kept in memory, so the list is cleared when the program closes.

## Usage

Run the program with:

```bash
python main.py
```

You'll get a simple menu:

```text
=== Task Manager ===

1. Add task
2. List tasks
3. Complete task
4. Delete task
5. Exit
```

Choose an option by entering its number.

When a task is created, it gets an ID and starts as incomplete. Internally, a task looks like this:

```python
{
    "id": 1,
    "title": "Study Python",
    "completed": False
}
```

Listing the tasks shows their current status:

```text
[ ] 1 - Study Python
[x] 2 - Finish project
```

Tasks can be completed or deleted using their ID.

The program also handles basic invalid input, such as unknown menu options or task IDs that don't exist.

## Requirements

Python 3 is the only requirement. The project has no external dependencies or database setup.
