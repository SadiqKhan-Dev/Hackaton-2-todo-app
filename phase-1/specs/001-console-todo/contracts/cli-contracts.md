# API Contracts: In-Memory Python Console Todo App

**Feature**: 001-console-todo
**Date**: 2026-01-01
**Based on**: spec.md Functional Requirements FR-001 to FR-014

## Overview

This document defines the contracts for all user-facing operations in the todo application. While this is a CLI application (not a REST API), these contracts define the interface between the user and the system, including inputs, outputs, errors, and side effects.

## Operation: Create Todo

### Command
`1` (menu option) → "Create Todo"

### Input
```
Enter todo title: [string]
```

### Request Contract
```python
{
    "operation": "create_todo",
    "input": {
        "title": {
            "type": "string",
            "required": true,
            "validation": "non-empty after stripping whitespace"
        }
    }
}
```

### Success Response
```
✓ Todo created successfully!
ID: 1
Title: Buy groceries
Status: Incomplete
```

### Error Responses
| Error Code | Message | Trigger |
|------------|---------|---------|
| INVALID_TITLE | "Error: Title cannot be empty. Please try again." | Title is empty or whitespace-only |

### Side Effects
- Adds new todo to in-memory list
- Increments next_id counter
- No external state changes

### Specification Reference
- FR-001: Create todos with unique ID, title, completion status
- FR-002: Sequential ID assignment starting from 1
- FR-013: Prevent empty titles
- FR-011: Display confirmation messages

---

## Operation: View All Todos

### Command
`2` (menu option) → "View All Todos"

### Input
No input required

### Request Contract
```python
{
    "operation": "view_todos",
    "input": {}
}
```

### Success Response (Non-empty list)
```
=== Your Todos ===
ID  | Title              | Status
----+--------------------+--------
 1  | Buy groceries      | ⬜ Incomplete
 2  | Write code         | ✅ Complete
 3  | Review spec        | ⬜ Incomplete
Total: 3 todos
```

### Success Response (Empty list)
```
=== Your Todos ===
No todos found. Create your first todo to get started!
```

### Error Responses
None (read operation, no errors expected)

### Side Effects
- None (read-only operation)

### Specification Reference
- FR-003: View all todos with formatted list
- FR-012: Handle empty list with descriptive message
- FR-011: Display confirmation/status messages

---

## Operation: Update Todo Title

### Command
`3` (menu option) → "Update Todo Title"

### Input
```
Enter todo ID: [integer]
Enter new title: [string]
```

### Request Contract
```python
{
    "operation": "update_title",
    "input": {
        "id": {
            "type": "integer",
            "required": true,
            "validation": "must exist in current todo list"
        },
        "title": {
            "type": "string",
            "required": true,
            "validation": "non-empty after stripping whitespace"
        }
    }
}
```

### Success Response
```
✓ Todo updated successfully!
ID: 2
Old title: Write code
New title: Write Python code
```

### Error Responses
| Error Code | Message | Trigger |
|------------|---------|---------|
| INVALID_ID_FORMAT | "Error: ID must be a number. Please try again." | ID is not numeric |
| ID_NOT_FOUND | "Error: Todo with ID 999 not found." | ID does not exist in list |
| INVALID_TITLE | "Error: Title cannot be empty. Please try again." | Title is empty or whitespace-only |

### Side Effects
- Updates title field of specified todo
- ID and completed status remain unchanged
- No external state changes

### Specification Reference
- FR-004: Update todo title by ID
- FR-014: Validate todo ID exists
- FR-013: Prevent empty titles
- FR-011: Display confirmation messages

---

## Operation: Toggle Todo Status

### Command
`4` (menu option) → "Toggle Todo Status"

### Input
```
Enter todo ID: [integer]
```

### Request Contract
```python
{
    "operation": "toggle_status",
    "input": {
        "id": {
            "type": "integer",
            "required": true,
            "validation": "must exist in current todo list"
        }
    }
}
```

### Success Response (Mark Complete)
```
✓ Todo marked as complete!
ID: 1
Title: Buy groceries
Status: Complete
```

### Success Response (Mark Incomplete)
```
✓ Todo marked as incomplete!
ID: 2
Title: Write code
Status: Incomplete
```

### Error Responses
| Error Code | Message | Trigger |
|------------|---------|---------|
| INVALID_ID_FORMAT | "Error: ID must be a number. Please try again." | ID is not numeric |
| ID_NOT_FOUND | "Error: Todo with ID 999 not found." | ID does not exist in list |

### Side Effects
- Toggles completed status (True ↔ False)
- All other fields remain unchanged
- No external state changes

### Specification Reference
- FR-005: Toggle completion status by ID
- FR-014: Validate todo ID exists
- FR-011: Display confirmation messages

---

## Operation: Delete Todo

### Command
`5` (menu option) → "Delete Todo"

### Input
```
Enter todo ID: [integer]
```

### Request Contract
```python
{
    "operation": "delete_todo",
    "input": {
        "id": {
            "type": "integer",
            "required": true,
            "validation": "must exist in current todo list"
        }
    }
}
```

### Success Response
```
✓ Todo deleted successfully!
ID: 3
Title: Review spec
```

### Error Responses
| Error Code | Message | Trigger |
|------------|---------|---------|
| INVALID_ID_FORMAT | "Error: ID must be a number. Please try again." | ID is not numeric |
| ID_NOT_FOUND | "Error: Todo with ID 999 not found." | ID does not exist in list |

### Side Effects
- Removes todo from in-memory list
- Remaining todos retain original IDs (no renumbering)
- No external state changes

### Specification Reference
- FR-006: Delete todo by ID
- FR-014: Validate todo ID exists
- FR-011: Display confirmation messages

---

## Operation: Display Menu

### Command
Automatic on startup, `m` or `menu` command, or after any operation

### Input
No input required

### Request Contract
```python
{
    "operation": "display_menu",
    "input": {}
}
```

### Response
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

### Error Responses
None (informational display)

### Side Effects
- None (read-only operation)

### Specification Reference
- FR-009: Provide command-based menu interface

---

## Operation: Quit Application

### Command
`q` or `quit` or `exit`

### Input
No input required

### Request Contract
```python
{
    "operation": "quit",
    "input": {}
}
```

### Response
```
Thank you for using Todo App!
Goodbye!
```

### Error Responses
None (exit operation)

### Side Effects
- Application exits
- All in-memory data is lost (no persistence)
- next_id counter resets to 1 on next startup

### Specification Reference
- FR-008: Reset all todo data on exit

---

## Global Error Handling

### Invalid Menu Choice
```
Error: Invalid choice 'x'. Please enter 1-5, 'm' for menu, or 'q' to quit.
```

### Unexpected Error
```
Error: An unexpected error occurred: [error message]
Please try again or contact support.
```

## Response Format Standard

### Success Messages
- Start with checkmark emoji: `✓`
- Clear action verb: "created", "updated", "deleted", "marked"
- Include todo details when applicable (ID, title, status)

### Error Messages
- Start with "Error:" prefix
- Describe the specific issue
- Provide guidance for correction when possible
- No technical jargon or stack traces

### Formatting
- Consistent indentation and spacing
- Table headers with separator lines for lists
- Emojis for visual indicators (✅ Complete, ⬜ Incomplete, ✓ Success, ✗ Error)

## Performance Contracts

| Operation | Max Response Time | Notes |
|-----------|------------------|-------|
| Create Todo | < 1 second | Includes validation |
| View Todos | < 2 seconds | Up to 1000 todos (SC-007) |
| Update Title | < 1 second | Includes validation |
| Toggle Status | < 1 second | Includes validation |
| Delete Todo | < 1 second | Includes validation |
| Display Menu | < 0.1 second | Static text |

## Determinism Guarantee

All operations produce deterministic output:
- Same input → Same output (success or error)
- Menu display is always consistent
- Error messages are consistent for same error type
- Todo display order is always insertion order
