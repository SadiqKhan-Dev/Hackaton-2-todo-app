"""
Error message constants for Todo Application.
"""
import sys

# Use ASCII fallback for Windows
_SUCCESS_MARK = "[OK]" if sys.platform == "win32" else "✓"
_COMPLETE_MARK = "[X]" if sys.platform == "win32" else "✅"
_INCOMPLETE_MARK = "[ ]" if sys.platform == "win32" else "⬜"

# Validation errors
ERROR_EMPTY_TITLE = "Error: Title cannot be empty. Please try again."
ERROR_INVALID_ID_FORMAT = "Error: ID must be a number. Please try again."
ERROR_ID_NOT_FOUND = "Error: Todo with ID {id} not found."

# Menu errors
ERROR_INVALID_MENU_CHOICE = "Error: Invalid choice '{choice}'. Please enter 1-5, 'm' for menu, or 'q' to quit."

# Success messages
SUCCESS_TODO_CREATED = f"{_SUCCESS_MARK} Todo created successfully!"
SUCCESS_TODO_UPDATED = f"{_SUCCESS_MARK} Todo updated successfully!"
SUCCESS_TODO_DELETED = f"{_SUCCESS_MARK} Todo deleted successfully!"
SUCCESS_TODO_MARKED_COMPLETE = f"{_SUCCESS_MARK} Todo marked as complete!"
SUCCESS_TODO_MARKED_INCOMPLETE = f"{_SUCCESS_MARK} Todo marked as incomplete!"

# Empty list messages
EMPTY_TODO_LIST = "No todos found. Create your first todo to get started!"

# Application messages
MENU_HEADER = "=== Todo App Menu ==="
GOODBYE_MESSAGE = "Thank you for using Todo App!\nGoodbye!"
