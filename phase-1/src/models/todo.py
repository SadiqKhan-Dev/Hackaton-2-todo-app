"""
Todo data model.
"""
from typing import TypedDict


class Todo(TypedDict):
    """
    Represents a todo item.

    Attributes:
        id: Unique numeric identifier (immutable)
        title: Todo description (can be modified)
        completed: Completion status (can be toggled)
    """
    id: int
    title: str
    completed: bool
