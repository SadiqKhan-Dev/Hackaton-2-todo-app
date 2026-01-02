"""
Menu functions for Todo Application CLI.
"""
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.validation import validate_id


def display_menu() -> None:
    """
    Display the main menu options.
    """
    from utils.formatting import format_menu
    print(format_menu())


def get_user_choice() -> str:
    """
    Get and validate user's menu choice.

    Returns:
        User's choice string
    """
    choice = input("Enter your choice (1-5, m, q): ").strip()
    return choice


def is_valid_menu_choice(choice: str) -> bool:
    """
    Validate menu choice.

    Args:
        choice: User's menu choice

    Returns:
        True if valid, False otherwise
    """
    valid_choices = ["1", "2", "3", "4", "5", "m", "q"]
    return choice in valid_choices
