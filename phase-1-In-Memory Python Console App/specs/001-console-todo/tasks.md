# Tasks: In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Manual testing via CLI (no automated tests required for Phase I)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below match structure defined in plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per implementation plan
- [X] T002 Initialize Python project with UV for Python 3.13+ compatibility
- [X] T003 [P] Create `__init__.py` files for all modules (src/, src/models/, src/services/, src/cli/, src/utils/)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create validation utility functions in `src/utils/validation.py` (validate_title, validate_id, validate_id_exists)
- [X] T005 [P] Define error message constants in `src/utils/errors.py` (all error messages from contracts)
- [X] T006 [P] Create Todo data model in `src/models/todo.py` with id, title, completed fields
- [X] T007 Implement TodoService class in `src/services/todo_service.py` with in-memory list storage and next_id counter
- [X] T008 [P] Configure CLI output formatting utilities in `src/utils/formatting.py` (table headers, status indicators, emojis)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Todos (Priority: P1) 🎯 MVP

**Goal**: Users can create new todos and view all todos in a list showing their current status

**Independent Test**: Can be fully tested by creating multiple todos with different titles, viewing the complete list, and verifying each todo appears with correct ID, title, and completion status. Delivers the core todo tracking capability.

### Implementation for User Story 1

- [X] T009 [P] [US1] Implement create_todo method in TodoService in `src/services/todo_service.py` (auto-increment ID, validate title, append to list)
- [X] T010 [P] [US1] Implement get_all_todos method in TodoService in `src/services/todo_service.py` (return list of all todos)
- [X] T011 [US1] Implement display_menu function in `src/cli/menu.py` (show menu options 1-5, m, q)
- [X] T012 [US1] Implement get_user_choice function in `src/cli/menu.py` (read input, validate menu option)
- [X] T013 [US1] Implement handle_create_todo command in `src/cli/commands.py` (prompt for title, call TodoService.create_todo, display confirmation)
- [X] T014 [US1] Implement handle_view_todos command in `src/cli/commands.py` (call TodoService.get_all_todos, format table output, handle empty list)
- [X] T015 [US1] Create main application loop in `src/main.py` (display menu, get choice, route to commands, continue/quit)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update Todo Status and Title (Priority: P2)

**Goal**: Users can modify existing todos by updating their title or toggling their completion status between complete and incomplete

**Independent Test**: Can be fully tested by creating multiple todos, then updating titles and toggling completion status. Verify updates persist and reflect correctly when viewing the list. Delivers task lifecycle management capability.

### Implementation for User Story 2

- [X] T016 [P] [US2] Implement update_todo_title method in TodoService in `src/services/todo_service.py` (validate ID and title, update title field)
- [X] T017 [P] [US2] Implement toggle_todo_status method in TodoService in `src/services/todo_service.py` (validate ID, toggle completed boolean)
- [X] T018 [US2] Implement handle_update_title command in `src/cli/commands.py` (prompt for ID and title, call TodoService.update_todo_title, display confirmation)
- [X] T019 [US2] Implement handle_toggle_status command in `src/cli/commands.py` (prompt for ID, call TodoService.toggle_todo_status, display confirmation)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Delete Todos (Priority: P2)

**Goal**: Users can permanently remove todos from the list by their unique identifier

**Independent Test**: Can be fully tested by creating multiple todos, deleting specific ones by ID, and verifying the deleted todos no longer appear while other todos remain intact. Delivers list cleanup capability.

### Implementation for User Story 3

- [X] T020 [P] [US3] Implement delete_todo method in TodoService in `src/services/todo_service.py` (validate ID, remove from list)
- [X] T021 [US3] Implement handle_delete_todo command in `src/cli/commands.py` (prompt for ID, call TodoService.delete_todo, display confirmation)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Command-Based Interface Navigation (Priority: P3)

**Goal**: Users interact with the application through a clear, intuitive command-based interface that displays available options, prompts for input as needed, and provides deterministic output with helpful feedback messages

**Independent Test**: Can be fully tested by launching the application, navigating through all menu options, and verifying each command produces clear, deterministic output. Delivers a usable and discoverable interface.

### Implementation for User Story 4

- [X] T022 [P] [US4] Enhance display_menu in `src/cli/menu.py` (add menu header, clear command descriptions, formatting)
- [X] T023 [US4] Enhance get_user_choice in `src/cli/menu.py` (handle invalid choices with error message, show valid options)
- [X] T024 [US4] Add error handling wrapper in `src/main.py` (catch exceptions, display user-friendly errors, continue loop)
- [X] T025 [US4] Enhance all command handlers in `src/cli/commands.py` (add clear success/error messages with emojis, consistent formatting)
- [X] T026 [US4] Implement graceful exit in `src/main.py` (display goodbye message, handle 'q' command)

**Checkpoint**: All user stories should now be independently functional with polished UI

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and final validation

- [X] T027 [P] Add PEP-8 compliance comments and docstrings to all modules
- [X] T028 Code cleanup and refactoring (remove any redundant code, optimize imports)
- [X] T029 Performance verification (test with 1000 todos to ensure <2s display time)
- [X] T030 [P] Verify all error messages match contracts in `src/utils/errors.py`
- [X] T031 Manual testing per quickstart.md workflows
- [X] T032 Final validation of all 5 CRUD operations

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (US1 → US2/US3 → US4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) and US1 basic CLI is present - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) and US1 basic CLI is present - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after all user stories (US1, US2, US3) complete - Enhances existing interface across all commands

### Within Each User Story

- Validation utilities (T004, T005) before service methods
- Models (T006) before services (T007)
- Service methods (T007, T009-T010, T016-T017, T020) before CLI command handlers
- CLI components (T011-T012, T013-T015, T018-T019, T021, T022-T026) before main loop (T015 enhanced in later stories)

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, user stories can start in parallel (if team capacity allows)
- Service methods within a story marked [P] can run in parallel
- Different user stories (US2 and US3) can be worked on in parallel by different team members after US1 is complete

---

## Parallel Example: Foundational Phase

```bash
# Launch all foundational setup tasks together:
Task: "Create validation utility functions in src/utils/validation.py"
Task: "Define error message constants in src/utils/errors.py"
Task: "Create Todo data model in src/models/todo.py"
Task: "Implement TodoService class in src/services/todo_service.py"
Task: "Configure CLI output formatting utilities in src/utils/formatting.py"
```

---

## Parallel Example: User Story 2 (Update Todo)

```bash
# Launch service methods together:
Task: "Implement update_todo_title method in TodoService in src/services/todo_service.py"
Task: "Implement toggle_todo_status method in TodoService in src/services/todo_service.py"

# Then launch CLI commands together:
Task: "Implement handle_update_title command in src/cli/commands.py"
Task: "Implement handle_toggle_status command in src/cli/commands.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently via CLI
5. Demo create and view functionality

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo
4. Add User Story 3 → Test independently → Demo
5. Add User Story 4 → Test independently → Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers (if applicable to Phase II):

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (create, view)
   - Developer B: User Story 2 (update)
   - Developer C: User Story 3 (delete)
3. Stories complete and integrate independently
4. Developer D or team: User Story 4 (interface polish)
5. Team: Polish and final validation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual testing via CLI (no automated tests required for Phase I)
- Follow PEP-8 naming and formatting conventions
- Use only Python standard library (no external dependencies)
- Data persists only during application session (resets on exit)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
