"""
Command handlers for Todo Application CLI.
"""
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.errors import (
    ERROR_EMPTY_TITLE,
    ERROR_INVALID_ID_FORMAT,
    ERROR_ID_NOT_FOUND,
    SUCCESS_TODO_CREATED,
    SUCCESS_TODO_UPDATED,
    SUCCESS_TODO_DELETED,
    SUCCESS_TODO_MARKED_COMPLETE,
    SUCCESS_TODO_MARKED_INCOMPLETE,
)
from utils.formatting import format_todo_list, format_todo_details
from utils.validation import validate_title, validate_id


def handle_create_todo(service):
    """
    Handle create todo command.

    Args:
        service: TodoService instance
    """
    try:
        title = input("Enter todo title: ")
        validated_title = validate_title(title)

        todo = service.create_todo(validated_title)
        print()
        print(format_todo_details(todo, "created"))
        print()

    except ValueError as e:
        print(f"\n{e}\n")


def handle_view_todos(service):
    """
    Handle view todos command.

    Args:
        service: TodoService instance
    """
    todos = service.get_all_todos()
    output = format_todo_list(todos)
    print()
    print(output)
    print()


def handle_update_title(service):
    """
    Handle update todo title command.

    Args:
        service: TodoService instance
    """
    try:
        id_str = input("Enter todo ID: ")
        todo_id = validate_id(id_str)

        new_title = input("Enter new title: ")
        validated_title = validate_title(new_title)

        todo = service.update_todo_title(todo_id, validated_title)
        print()
        print(f"ID: {todo['id']}")
        print(f"Old title: {todo['title']}")
        print(format_todo_details(todo, "updated"))

    except ValueError as e:
        print(f"\n{e}\n")


def handle_toggle_status(service):
    """
    Handle toggle todo status command.

    Args:
        service: TodoService instance
    """
    try:
        id_str = input("Enter todo ID: ")
        todo_id = validate_id(id_str)

        todo = service.toggle_todo_status(todo_id)
        print()
        if todo['completed']:
            print(SUCCESS_TODO_MARKED_COMPLETE)
        else:
            print(SUCCESS_TODO_MARKED_INCOMPLETE)
        print(format_todo_details(todo))
        print()

    except ValueError as e:
        print(f"\n{e}\n")


def handle_delete_todo(service):
    """
    Handle delete todo command.

    Args:
        service: TodoService instance
    """
    try:
        id_str = input("Enter todo ID: ")
        todo_id = validate_id(id_str)

        todo = service.delete_todo(todo_id)
        print()
        print(SUCCESS_TODO_DELETED)
        print(format_todo_details(todo))
        print()

    except ValueError as e:
        print(f"\n{e}\n")
