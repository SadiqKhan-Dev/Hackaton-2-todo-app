"""
Input validation utilities for Todo Application.
"""
from typing import List


def validate_title(title: str) -> str:
    """
    Validate todo title.

    Args:
        title: Title string to validate

    Returns:
        Trimmed and validated title

    Raises:
        ValueError: If title is empty or whitespace-only
    """
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")

    return title.strip()


def validate_id(id_str: str) -> int:
    """
    Validate and parse todo ID from string input.

    Args:
        id_str: String representation of ID

    Returns:
        Parsed integer ID

    Raises:
        ValueError: If ID is not a valid integer
    """
    try:
        todo_id = int(id_str)
    except (ValueError, TypeError):
        raise ValueError("ID must be a number")

    return todo_id


def validate_id_exists(todos: List[dict], todo_id: int) -> None:
    """
    Validate that a todo ID exists in the current list.

    Args:
        todos: List of todo dictionaries
        todo_id: ID to validate

    Raises:
        ValueError: If ID does not exist in the list
    """
    if not any(todo["id"] == todo_id for todo in todos):
        raise ValueError(f"Todo with ID {todo_id} not found")
