"""
TodoService - Business logic for todo operations.

Manages in-memory storage of todos with CRUD operations.
"""
import sys
import os

# Add parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.todo import Todo
from typing import List, Optional


class TodoService:
    """
    Service class managing todos with in-memory storage.
    """

    def __init__(self) -> None:
        """Initialize TodoService with empty storage and ID counter."""
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def create_todo(self, title: str) -> Todo:
        """
        Create a new todo with auto-incremented ID.

        Args:
            title: Title for the todo

        Returns:
            Created todo object

        Raises:
            ValueError: If title is invalid
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        cleaned_title = title.strip()
        todo = Todo(id=self._next_id, title=cleaned_title, completed=False)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in current session.

        Returns:
            List of all todos (empty list if none exist)
        """
        return self._todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Find a todo by its ID.

        Args:
            todo_id: Unique identifier

        Returns:
            Todo object if found, None otherwise
        """
        for todo in self._todos:
            if todo["id"] == todo_id:
                return todo
        return None

    def update_todo_title(self, todo_id: int, new_title: str) -> Todo:
        """
        Update the title of an existing todo.

        Args:
            todo_id: ID of todo to update
            new_title: New title value

        Returns:
            Updated todo object

        Raises:
            ValueError: If ID not found or title invalid
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            raise ValueError(f"Todo with ID {todo_id} not found")

        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty")

        todo["title"] = new_title.strip()
        return todo

    def toggle_todo_status(self, todo_id: int) -> Todo:
        """
        Toggle completion status of a todo.

        Args:
            todo_id: ID of todo to toggle

        Returns:
            Updated todo object

        Raises:
            ValueError: If ID not found
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            raise ValueError(f"Todo with ID {todo_id} not found")

        todo["completed"] = not todo["completed"]
        return todo

    def delete_todo(self, todo_id: int) -> Todo:
        """
        Delete a todo by ID.

        Args:
            todo_id: ID of todo to delete

        Returns:
            Deleted todo object

        Raises:
            ValueError: If ID not found
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            raise ValueError(f"Todo with ID {todo_id} not found")

        self._todos.remove(todo)
        return todo

    def count(self) -> int:
        """
        Get total count of todos.

        Returns:
            Number of todos in storage
        """
        return len(self._todos)
