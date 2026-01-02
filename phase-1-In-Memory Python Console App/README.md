# In-Memory Python Console Todo App

Phase I of a spec-driven todo application using Spec-Kit Plus and Claude Code.

## Features

- Create todos with auto-incremented IDs
- View all todos in a formatted table
- Update todo titles
- Toggle todo completion status
- Delete todos
- Menu-driven CLI interface
- In-memory storage (data resets on exit)

## Prerequisites

- Python 3.13+ (or Python 3.12+)
- UV package manager (optional but recommended)

## Installation

### Using UV (Recommended)

```bash
uv run python src/main.py
```

### Using Python Directly

```bash
python src/main.py
```

## Usage

Launch the application and follow the menu prompts:

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

## Architecture

```
src/
├── models/
│   └── todo.py          # Todo data model
├── services/
│   └── todo_service.py  # Business logic
├── cli/
│   ├── menu.py          # Menu interface
│   └── commands.py      # Command handlers
├── utils/
│   ├── validation.py    # Input validation
│   ├── errors.py        # Error messages
│   └── formatting.py   # Output formatting
└── main.py              # Application entry point
```

## Development

This project follows Spec-Driven Development:

- Specification: `specs/001-console-todo/spec.md`
- Implementation Plan: `specs/001-console-todo/plan.md`
- Data Model: `specs/001-console-todo/data-model.md`
- CLI Contracts: `specs/001-console-todo/contracts/cli-contracts.md`
- Tasks: `specs/001-console-todo/tasks.md`
- Quickstart: `specs/001-console-todo/quickstart.md`

## Constitution

All development follows the project constitution at `.specify/memory/constitution.md`:

- Spec-Driven Development as single source of truth
- Simplicity and correctness over premature optimization
- Deterministic behavior (predictable inputs/outputs)
- Clean separation of concerns (logic, state, UI/CLI)
- Extensibility for future phases (web, AI, cloud)

## Scope

**In Scope**:
- All 5 CRUD operations
- Menu-driven CLI interface
- In-memory storage during session
- Error handling and validation
- PEP-8 compliant code

**Out of Scope**:
- Persistence to files or databases
- Web APIs or network connectivity
- Authentication or multi-user support
- AI-powered features

## Phase II Preview

Future enhancements will include:
- Data persistence (files or database)
- Web interface
- AI-powered features and smart suggestions
- Cloud sync and multi-device access

## License

Internal project for hackathon demonstration.
