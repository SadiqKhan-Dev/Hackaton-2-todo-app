# Implementation Plan: In-Memory Python Console Todo App

**Branch**: `001-console-todo` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-console-todo/spec.md`

**Note**: This template is filled in by `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Command-line todo application providing five core CRUD operations (create, read, update title, toggle completion status, delete) with in-memory storage. The application uses a menu-driven interface with clear command structure, deterministic output, and comprehensive error handling. All implementation follows spec-driven development principles with clean separation between business logic and CLI presentation layers.

**Architecture Overview**:
- **Entry point**: main.py (CLI loop and command routing)
- **Domain model**: Todo (id, title, completed)
- **In-memory store**: List-based repository
- **Services**: TodoService (business logic)
- **CLI layer**: Input parsing and output rendering
- **Utils**: Validation and error handling

**Implementation Sequence**:
1. Define Todo data model
2. Implement in-memory repository
3. Implement core operations (add, view, update, delete, complete)
4. Build CLI command loop
5. Add input validation and user feedback
6. Final manual test via console

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python standard library only)
**Storage**: In-memory data structures (no persistence)
**Testing**: Manual testing via CLI (no automated tests required for Phase I)
**Target Platform**: Cross-platform (Windows, macOS, Linux) via Python console
**Project Type**: Single project with modular structure
**Performance Goals**: Display operations < 2 seconds for up to 1000 todos; create/update/delete operations < 1 second
**Constraints**: No external dependencies, no file system/database persistence, no network calls, PEP-8 compliance required
**Scale/Scope**: Single user, single session, up to 1000 todos per session, 5 CRUD operations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Spec-Driven Development
- **Status**: ✅ PASS
- **Evidence**: All features originate from written specification (FR-001 to FR-014). Implementation scope is locked to 5 basic operations as defined in spec.

### Simplicity & Correctness
- **Status**: ✅ PASS
- **Evidence**: Design uses standard library only, minimal dependencies, straightforward data model. No premature optimization or over-engineering planned. List-based repository with TodoService is simple and correct.

### Deterministic Behavior
- **Status**: ✅ PASS
- **Evidence**: All CLI operations produce predictable output. No randomness or hidden behavior. Input validation ensures consistent responses. Single-user, deterministic flow enforced.

### Separation of Concerns
- **Status**: ✅ PASS
- **Evidence**: Planned structure separates business logic (models, services) from CLI presentation (cli module). Clear module boundaries defined: main.py (entry), TodoService (logic), CLI layer (presentation), Utils (validation).

### Extensibility
- **Status**: ✅ PASS
- **Evidence**: Architecture designed for Phase II migration (persistence, web, AI). No barriers to future extension identified. Modular structure supports incremental enhancement. List-based repository can be replaced with database without breaking service layer.

**Overall Status**: ✅ ALL GATES PASS - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── cli-contracts.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── todo.py          # Todo data model
├── services/
│   └── todo_service.py  # Business logic for todo operations
├── cli/
│   ├── menu.py          # CLI menu interface
│   └── commands.py      # Command handlers
├── utils/
│   └── validation.py    # Input validation and error handling
└── main.py              # Application entry point (CLI loop and command routing)

tests/
├── contract/
├── integration/
└── unit/
```

**Structure Decision**: Single project structure chosen because:
- Feature scope is contained (5 CRUD operations)
- No frontend/backend separation required
- Standard library only, no complex dependencies
- Clear separation: models (data), services (logic), cli (presentation), utils (validation)
- Architecture supports Phase II extension without refactoring
- List-based repository in TodoService provides simple, correct in-memory storage

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution violations. Complexity tracking not required.

## Design Artifacts

### Phase 0: Research
- **File**: `research.md`
- **Status**: ✅ Complete
- **Decisions**:
  1. Menu-driven CLI interface (better discoverability)
  2. List of dictionaries for in-memory storage (simple, extensible)
  3. Defensive programming with explicit validation (correctness)
  4. Column-aligned table format for output (readable, deterministic)
  5. Event loop with graceful exit (standard pattern)

### Phase 1: Data Model
- **File**: `data-model.md`
- **Status**: ✅ Complete
- **Entity**: Todo (id: int, title: str, completed: bool)
- **Storage**: Python list of dictionaries with auto-increment ID counter
- **Validation**: Title non-empty, ID numeric and exists

### Phase 1: Contracts
- **File**: `contracts/cli-contracts.md`
- **Status**: ✅ Complete
- **Operations Defined**:
  1. Create Todo (input: title)
  2. View All Todos (input: none)
  3. Update Todo Title (input: id, title)
  4. Toggle Todo Status (input: id)
  5. Delete Todo (input: id)
  6. Display Menu (input: none)
  7. Quit Application (input: none)

### Phase 1: Quickstart
- **File**: `quickstart.md`
- **Status**: ✅ Complete
- **Contents**: Installation, common workflows, commands reference, error handling, troubleshooting

## Constitution Check (Post-Design)

*Re-evaluation after Phase 1 design completion*

### Spec-Driven Development
- **Status**: ✅ PASS
- **Evidence**: All design decisions trace to specification requirements. Data model (id, title, completed) matches spec FR-001. Contracts cover FR-001 to FR-014. Quickstart aligns with user scenarios.

### Simplicity & Correctness
- **Status**: ✅ PASS
- **Evidence**: Data model uses simple Python dictionary (no classes or ORM). List-based repository in TodoService is straightforward. Validation logic is in utils module (type checking, existence checks). No abstraction layers beyond required separation.

### Deterministic Behavior
- **Evidence**: CLI contracts define exact input/output formats. Validation rules are explicit (non-empty title, numeric ID). Error messages are consistent across operations. Output format (table, emojis) is standardized. Single-user, deterministic flow enforced by architecture.

### Separation of Concerns
- **Status**: ✅ PASS
- **Evidence**: Design defines clear boundaries: models (data structure), services (business logic via TodoService), cli (presentation via menu and commands), utils (validation and error handling). Contracts document interface between layers. Quickstart focuses on user experience, not implementation.

### Extensibility
- **Status**: ✅ PASS
- **Evidence**: Dictionary structure can be converted to ORM model for persistence. List-based repository can be replaced with database without breaking TodoService. Service layer can be enhanced without breaking CLI. Utils validation can be reused across Phase II features. No tight coupling between components.

**Overall Status**: ✅ ALL GATES PASS - Proceed to Phase 2 (Tasks)

## Phase 2: Implementation Tasks

**Next Step**: Run `/sp.tasks` to generate testable, dependency-ordered tasks based on:
- User stories from spec.md (with priorities P1, P2, P3)
- Data model from data-model.md
- CLI contracts from contracts/cli-contracts.md
- Research findings from research.md

**Implementation Steps** (from architecture plan):
1. Define Todo data model (src/models/todo.py)
2. Implement in-memory repository in TodoService (src/services/todo_service.py)
3. Implement core operations (add, view, update, delete, complete) in TodoService
4. Build CLI command loop (src/main.py)
5. Add input validation and user feedback (src/utils/validation.py, src/cli/menu.py, src/cli/commands.py)
6. Final manual test via console

**Prerequisites**:
- All Phase 0 and Phase 1 artifacts complete ✅
- Constitution checks pass (initial and post-design) ✅
- Agent context updated ✅

**Expected Output**: `specs/001-console-todo/tasks.md` with tasks organized by user story and phase.
