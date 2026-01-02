"""
Main entry point for Todo Application CLI.
"""
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.menu import display_menu, get_user_choice
from cli.commands import (
    handle_create_todo,
    handle_view_todos,
    handle_update_title,
    handle_toggle_status,
    handle_delete_todo,
)
from services.todo_service import TodoService
from utils.errors import ERROR_INVALID_MENU_CHOICE, GOODBYE_MESSAGE


def main() -> None:
    """
    Main application loop.
    """
    service = TodoService()

    while True:
        try:
            # Display menu
            display_menu()

            # Get user choice
            choice = get_user_choice()

            # Handle choice
            if choice == "1":
                handle_create_todo(service)
            elif choice == "2":
                handle_view_todos(service)
            elif choice == "3":
                handle_update_title(service)
            elif choice == "4":
                handle_toggle_status(service)
            elif choice == "5":
                handle_delete_todo(service)
            elif choice == "m":
                continue
            elif choice == "q":
                print()
                print(GOODBYE_MESSAGE)
                break
            else:
                print(f"\n{ERROR_INVALID_MENU_CHOICE}\n")

        except KeyboardInterrupt:
            print("\n")
            print(GOODBYE_MESSAGE)
            break
        except Exception as e:
            print(f"\nError: An unexpected error occurred: {e}\nPlease try again.\n")


if __name__ == "__main__":
    main()
