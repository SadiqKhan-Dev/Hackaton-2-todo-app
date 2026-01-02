"""
CLI output formatting utilities.
"""
import sys


def _get_status_complete() -> str:
    """Get status indicator for complete todos (with ASCII fallback for Windows)."""
    if sys.platform == "win32":
        return "[X] Complete"
    return "✅ Complete"


def _get_status_incomplete() -> str:
    """Get status indicator for incomplete todos (with ASCII fallback for Windows)."""
    if sys.platform == "win32":
        return "[ ] Incomplete"
    return "⬜ Incomplete"


def _get_success_mark() -> str:
    """Get success mark (with ASCII fallback for Windows)."""
    if sys.platform == "win32":
        return "[OK]"
    return "✓"


def format_todo_list(todos: list) -> str:
    """
    Format todos as a table with headers and status indicators.

    Args:
        todos: List of todo dictionaries

    Returns:
        Formatted table string
    """
    if not todos:
        return "No todos found. Create your first todo to get started!"

    # Define column widths
    id_width = 3
    title_width = max(12, max(len(todo["title"]) for todo in todos))
    status_width = 12

    # Build header
    header = f"{'ID':<{id_width}} | {'Title':<{title_width}} | {'Status':<{status_width}}"
    separator = f"{'-' * id_width}+{'-' * title_width}+{'-' * status_width}".replace(" ", "+")

    lines = ["=== Your Todos ===", header, separator]

    # Add todo rows
    for todo in todos:
        status_indicator = _get_status_complete() if todo["completed"] else _get_status_incomplete()
        row = f"{todo['id']:>{id_width}}  | {todo['title']:<{title_width}} | {status_indicator}"
        lines.append(row)

    lines.append(f"Total: {len(todos)} todos")
    return "\n".join(lines)


def format_todo_details(todo: dict, action: str = "") -> str:
    """
    Format todo details for display.

    Args:
        todo: Todo dictionary
        action: Action performed (optional)

    Returns:
        Formatted details string
    """
    status = "Complete" if todo["completed"] else "Incomplete"
    success = _get_success_mark()
    lines = [f"{success} {action} successfully!"] if action else ["Todo details:"]
    lines.append(f"ID: {todo['id']}")
    lines.append(f"Title: {todo['title']}")
    lines.append(f"Status: {status}")
    return "\n".join(lines)


def format_menu() -> str:
    """
    Format main menu (without prompt - prompt is handled by get_user_choice).

    Returns:
        Formatted menu string
    """
    lines = [
        "=== Todo App Menu ===",
        "1. Create Todo",
        "2. View All Todos",
        "3. Update Todo Title",
        "4. Toggle Todo Status",
        "5. Delete Todo",
        "m. Display Menu (this screen)",
        "q. Quit Application",
    ]
    return "\n".join(lines)
