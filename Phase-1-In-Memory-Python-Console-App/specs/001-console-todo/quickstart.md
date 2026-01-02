# Quickstart Guide: In-Memory Python Console Todo App

**Feature**: 001-console-todo
**Date**: 2026-01-01
**Target**: Users and developers wanting to understand and use the application

## Overview

The In-Memory Python Console Todo App is a command-line interface application that allows you to manage todos in a single session. Create, view, update, and delete tasks through an intuitive menu system.

## Prerequisites

- Python 3.13 or higher installed
- Basic familiarity with command-line interfaces
- No external dependencies required (standard library only)

## Installation

### Option 1: Run with UV (Recommended)

```bash
# Install UV (if not already installed)
pip install uv

# Run application with UV
uv run python src/main.py
```

### Option 2: Run with Python Directly

```bash
# Navigate to project directory
cd path/to/hackaton-2-todo-app

# Run application
python src/main.py
```

## First Launch

When you first launch the application, you'll see the main menu:

```
=== Todo App Menu ===
1. Create Todo
2. View All Todos
3. Update Todo Title
4. Toggle Todo Status
5. Delete Todo
m. Display Menu (this screen)
q. Quit Application

Enter your choice (1-5, m, q):
```

## Common Workflows

### Workflow 1: Create Your First Todo

1. Launch the application
2. Enter `1` to select "Create Todo"
3. Enter a title when prompted:
   ```
   Enter todo title: Buy groceries
   ```
4. See confirmation:
   ```
   ✓ Todo created successfully!
   ID: 1
   Title: Buy groceries
   Status: Incomplete
   ```

### Workflow 2: View All Todos

1. From the menu, enter `2` to select "View All Todos"
2. See your todo list:
   ```
   === Your Todos ===
   ID  | Title              | Status
   ----+--------------------+--------
    1  | Buy groceries      | ⬜ Incomplete
   Total: 1 todos
   ```

### Workflow 3: Mark a Todo as Complete

1. From the menu, enter `4` to select "Toggle Todo Status"
2. Enter the todo ID:
   ```
   Enter todo ID: 1
   ```
3. See confirmation:
   ```
   ✓ Todo marked as complete!
   ID: 1
   Title: Buy groceries
   Status: Complete
   ```

### Workflow 4: Update a Todo Title

1. From the menu, enter `3` to select "Update Todo Title"
2. Enter the todo ID:
   ```
   Enter todo ID: 1
   ```
3. Enter the new title:
   ```
   Enter new title: Buy groceries and milk
   ```
4. See confirmation:
   ```
   ✓ Todo updated successfully!
   ID: 1
   Old title: Buy groceries
   New title: Buy groceries and milk
   ```

### Workflow 5: Delete a Todo

1. From the menu, enter `5` to select "Delete Todo"
2. Enter the todo ID:
   ```
   Enter todo ID: 1
   ```
3. See confirmation:
   ```
   ✓ Todo deleted successfully!
   ID: 1
   Title: Buy groceries
   ```

## Commands Reference

| Command | Action | Input Required |
|---------|--------|----------------|
| `1` | Create Todo | Title (string) |
| `2` | View All Todos | None |
| `3` | Update Todo Title | ID (integer), new title (string) |
| `4` | Toggle Todo Status | ID (integer) |
| `5` | Delete Todo | ID (integer) |
| `m` | Display Menu | None |
| `q` | Quit Application | None |

## Error Handling

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Title cannot be empty" | You pressed Enter without typing or entered only spaces | Type a valid title and press Enter |
| "ID must be a number" | You entered a letter or symbol instead of a number | Enter the numeric ID of the todo |
| "Todo with ID X not found" | The todo ID doesn't exist in your current list | View your todos first (option 2) to see valid IDs |
| "Invalid choice" | You entered a menu option that doesn't exist | Enter 1-5, `m` for menu, or `q` to quit |

## Important Notes

### Data Persistence
⚠️ **All data is lost when you quit the application**

This is Phase I of the application with in-memory storage only. When you quit (`q`), all todos are permanently deleted and will not be available when you restart the application.

### Todo IDs
- IDs are assigned sequentially starting from 1
- IDs are never reused (deleted todos leave gaps in numbering)
- IDs help you identify which todo to update or delete
- Use "View All Todos" (option 2) to see all current IDs

### Session Scope
- Application runs in a single session
- Close the application to reset (clear all data)
- Reopen to start fresh

## Tips for Efficient Use

1. **View first, then act**: Use option 2 to see all todos before updating or deleting
2. **Keep track of IDs**: Note the IDs of todos you want to modify
3. **Use descriptive titles**: Clear titles help you identify todos easily in the list
4. **Mark complete gradually**: Use option 4 as you complete tasks to track progress
5. **Clean up regularly**: Use option 5 to delete completed or cancelled todos

## Example Session

```
=== Todo App Menu ===
1. Create Todo
2. View All Todos
3. Update Todo Title
4. Toggle Todo Status
5. Delete Todo
m. Display Menu (this screen)
q. Quit Application

Enter your choice (1-5, m, q): 1
Enter todo title: Write Python code
✓ Todo created successfully!
ID: 1
Title: Write Python code
Status: Incomplete

Enter your choice (1-5, m, q): 1
Enter todo title: Review specification
✓ Todo created successfully!
ID: 2
Title: Review specification
Status: Incomplete

Enter your choice (1-5, m, q): 2
=== Your Todos ===
ID  | Title                  | Status
----+------------------------+--------
 1  | Write Python code       | ⬜ Incomplete
 2  | Review specification  | ⬜ Incomplete
Total: 2 todos

Enter your choice (1-5, m, q): 4
Enter todo ID: 2
✓ Todo marked as complete!
ID: 2
Title: Review specification
Status: Complete

Enter your choice (1-5, m, q): 2
=== Your Todos ===
ID  | Title                  | Status
----+------------------------+--------
 1  | Write Python code       | ⬜ Incomplete
 2  | Review specification  | ✅ Complete
Total: 2 todos

Enter your choice (1-5, m, q): q
Thank you for using Todo App!
Goodbye!
```

## Troubleshooting

### Application Won't Start

**Problem**: Python version error or module not found

**Solution**:
1. Check Python version: `python --version` (must be 3.13+)
2. Ensure you're in the correct project directory
3. Try running with UV: `uv run python src/main.py`

### Menu Doesn't Display Correctly

**Problem**: Text alignment or formatting issues

**Solution**:
- This can happen with very long titles or narrow terminal windows
- Try widening your terminal window
- Long titles will wrap but remain functional

### Input Appears Stuck

**Problem**: Application seems frozen after entering input

**Solution**:
- Press Enter to submit your input
- Ensure you've entered the required information
- Check for error messages above the prompt

## Next Steps

After familiarizing yourself with the application:

1. **Explore all features**: Try each menu option with different inputs
2. **Test edge cases**: Enter invalid data to see error handling
3. **Manage multiple todos**: Create, update, and delete several todos in one session
4. **Provide feedback**: Report any issues or suggestions for Phase II

## Phase II Preview

Future enhancements planned for Phase II include:
- Data persistence (save todos between sessions)
- Web interface (browser-based todo management)
- AI-powered features (smart suggestions, categorization)
- Cloud sync and multi-device access

Stay tuned for updates!
