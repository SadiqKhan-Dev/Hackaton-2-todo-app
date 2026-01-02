# Research: In-Memory Python Console Todo App

**Feature**: 001-console-todo
**Date**: 2026-01-01

## Overview

Research conducted to resolve technical design decisions for the Phase I In-Memory Python Console Todo App. All decisions align with the constitution principles (spec-driven, simple, deterministic, separation of concerns, extensible).

## Decision 1: CLI Interface Approach

**Decision**: Menu-driven interface with numbered options and keyboard navigation

**Rationale**:
- Better discoverability for users new to the application (matches spec FR-009 requirement for clear menu)
- Reduces cognitive load compared to memorizing commands
- Supports easy expansion of features in Phase II
- Standard pattern for console applications that prioritizes usability

**Alternatives considered**:
- **Command-driven interface** (e.g., `todo add "Buy groceries"`): More power-user friendly but requires learning commands. Would be better for advanced users but less discoverable for initial users.
- **Hybrid approach** (menu + command shortcuts): Provides both options but adds complexity. Not needed for Phase I scope of 5 basic operations.

**Constitution alignment**:
- ✅ Simplicity: Single consistent interaction model
- ✅ Deterministic: Clear menu options with predictable navigation
- ✅ Extensibility: Easy to add new menu items in Phase II

## Decision 2: In-Memory Data Structure

**Decision**: Python list of dictionaries for todo storage, with auto-incrementing integer ID counter

**Rationale**:
- Simple and straightforward (FR-002 requires sequential IDs starting from 1)
- Natural mapping to todo entity attributes (id, title, completed)
- Built-in list operations (append, remove, iteration) cover all CRUD requirements
- No overhead of class definitions for Phase I scope
- Easy to migrate to database in Phase II

**Data structure example**:
```python
todos = []  # List of todo dictionaries
next_id = 1  # Auto-increment counter

# Todo structure:
{
    "id": 1,
    "title": "Buy groceries",
    "completed": False
}
```

**Alternatives considered**:
- **Class-based model** (Todo class with methods): More object-oriented but adds boilerplate. Could be better for Phase II but premature abstraction for Phase I.
- **Dictionary with ID keys** (e.g., `{1: todo1, 2: todo2}`): Faster lookups by ID but more complex iteration. List is simpler for the primary use case of viewing all todos.

**Constitution alignment**:
- ✅ Simplicity: Uses standard Python data structures
- ✅ Extensibility: Can be refactored to class or database without breaking logic layer

## Decision 3: Input Validation Strategy

**Decision**: Defensive programming with explicit validation before operations, clear error messages

**Rationale**:
- Prevents invalid state changes (matches spec FR-013, FR-014)
- Provides clear user feedback (matches spec FR-010)
- Catches errors early with specific messages
- Supports deterministic behavior (same input always produces same error)

**Validation points**:
- Todo title: Non-empty after stripping whitespace (FR-013)
- Todo ID: Must be numeric integer (FR-014)
- Todo existence: Must exist in list before update/delete (FR-014)
- Menu option: Must be valid menu number

**Error handling pattern**:
```python
def validate_todo_title(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    return title.strip()

def validate_todo_id(todos, id_str):
    try:
        todo_id = int(id_str)
    except ValueError:
        raise ValueError("ID must be a number")

    if not any(todo["id"] == todo_id for todo in todos):
        raise ValueError(f"Todo with ID {todo_id} not found")

    return todo_id
```

**Alternatives considered**:
- **Exception-only validation**: Rely on try/except everywhere. Less explicit and harder to provide specific error messages.
- **Regex-based validation**: Overkill for simple numeric and non-empty checks.

**Constitution alignment**:
- ✅ Simplicity: Straightforward validation logic
- ✅ Deterministic: Clear validation rules produce consistent outcomes
- ✅ Correctness: Explicit validation prevents invalid states

## Decision 4: Console Output Formatting

**Decision**: Column-aligned table format with consistent spacing, clear headers, and status indicators

**Rationale**:
- Readable presentation of todo data (matches spec FR-003 requirement for formatted list)
- Consistent with console application patterns
- Supports large lists (up to 1000 todos as per SC-007)
- Easy to parse visually while being deterministic

**Output format example**:
```
=== Your Todos ===
ID  | Title              | Status
----+--------------------+--------
 1  | Buy groceries      | ⬜ Incomplete
 2  | Write code         | ✅ Complete
 3  | Review spec        | ⬜ Incomplete
```

**Alternatives considered**:
- **Simple list format**: Less structured, harder to scan for large lists.
- **JSON output**: Machine-readable but not user-friendly for console interface.
- **External library (tabulate)**: Violates standard library constraint.

**Constitution alignment**:
- ✅ Simplicity: Uses string formatting, no external dependencies
- ✅ Deterministic: Consistent output for same data
- ✅ Extensibility: Can be replaced with richer formatting in Phase II

## Decision 5: Application Flow Control

**Decision**: Event loop with continue/exit options, graceful shutdown

**Rationale**:
- Allows multiple operations in single session (matches user scenario workflows)
- Clear exit point (FR-008 requires reset on exit)
- Standard pattern for console applications
- Supports testing of multiple operations

**Flow pattern**:
```python
def main():
    while True:
        display_menu()
        choice = get_user_choice()
        handle_choice(choice)
        if should_exit(choice):
            break
```

**Alternatives considered**:
- **Single-operation mode**: User runs app, performs one operation, exits. Less efficient for typical usage.
- **State machine with explicit states**: Overkill for simple menu-driven interface.

**Constitution alignment**:
- ✅ Simplicity: Simple while loop with clear logic
- ✅ Deterministic: Predictable flow from menu to action
- ✅ Separation of concerns: Business logic separated from flow control

## Research Summary

All technical decisions aligned with constitution principles and specification requirements:

1. **CLI Interface**: Menu-driven for discoverability and usability
2. **Data Structure**: List of dictionaries with auto-increment IDs
3. **Input Validation**: Defensive programming with clear error messages
4. **Output Formatting**: Column-aligned table format
5. **Flow Control**: Event loop with graceful exit

No NEEDS CLARIFICATION items remain. Ready to proceed to Phase 1 (Design & Contracts).
