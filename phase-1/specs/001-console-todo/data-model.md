# Data Model: In-Memory Python Console Todo App

**Feature**: 001-console-todo
**Date**: 2026-01-01
**Based on**: spec.md Functional Requirements FR-001 to FR-008

## Entity: Todo

### Overview
Represents a single task with unique identifier, title, and completion status. This is the core entity for the todo application.

### Attributes

| Attribute | Type | Description | Constraints | Validation |
|-----------|------|-------------|-------------|------------|
| id | Integer | Unique identifier for the todo | Must be positive integer, sequential starting from 1 | Auto-assigned, immutable after creation |
| title | String | The task description | Non-empty string after stripping whitespace | Must contain at least one non-whitespace character |
| completed | Boolean | Completion status | True (complete) or False (incomplete) | Defaults to False on creation |

### Data Structure

**Implementation**: Python dictionary stored in a list

```python
# Single todo
{
    "id": 1,
    "title": "Buy groceries",
    "completed": False
}

# In-memory storage
todos = []  # List of todo dictionaries
next_id = 1  # Auto-increment counter
```

### Lifecycle

#### Creation
- **Operation**: Add new todo
- **ID Assignment**: Sequential auto-increment starting from 1
- **Initial State**: completed = False
- **Validation**: Title must not be empty or whitespace-only
- **Requirement Reference**: FR-001, FR-002, FR-013

#### Read
- **Operation**: View all todos
- **Order**: Displayed in insertion order (first created first shown)
- **Filtering**: None (all todos shown)
- **Empty State**: Display descriptive message when no todos exist
- **Requirement Reference**: FR-003, FR-012

#### Update Title
- **Operation**: Modify todo title by ID
- **ID Validation**: Must be numeric and exist in current list
- **Title Validation**: Non-empty after stripping whitespace
- **Immutability**: ID and completed status remain unchanged
- **Requirement Reference**: FR-004, FR-014

#### Update Status
- **Operation**: Toggle completion status by ID
- **ID Validation**: Must be numeric and exist in current list
- **State Transition**: Complete ↔ Incomplete (toggle)
- **Behavior**: Current status is inverted (True becomes False, False becomes True)
- **Requirement Reference**: FR-005, FR-014

#### Deletion
- **Operation**: Remove todo by ID
- **ID Validation**: Must be numeric and exist in current list
- **Side Effects**: Remaining todos retain original IDs (no renumbering)
- **Persistence**: Deletion is permanent within current session
- **Requirement Reference**: FR-006, FR-014

### State Transitions

```
[Created] → [Title Updated] → [Status Toggled] → [Deleted]
     ↓              ↓                ↓
  [Incomplete]  [Incomplete]    [Complete/Incomplete]
                  ↓
             [Complete]
```

**Transitions**:
1. **Creation**: Always starts as incomplete (completed = False)
2. **Title Update**: Does not affect completion status
3. **Status Toggle**: Switches between complete and incomplete
4. **Deletion**: Final state, todo removed from list

### Validation Rules

#### Title Validation
```python
def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    return title.strip()
```

**Rules**:
- Cannot be None or empty string
- Cannot contain only whitespace characters
- Whitespace at edges is trimmed (stripped)
- No maximum length enforced (Phase I scope)

#### ID Validation
```python
def validate_id(todos, id_str):
    try:
        todo_id = int(id_str)
    except ValueError:
        raise ValueError("ID must be a number")

    if todo_id < 1:
        raise ValueError("ID must be a positive integer")

    if not any(todo["id"] == todo_id for todo in todos):
        raise ValueError(f"Todo with ID {todo_id} not found")

    return todo_id
```

**Rules**:
- Must be numeric (convertible to integer)
- Must be positive (ID > 0)
- Must exist in current todo list

### Relationships

**No relationships** (Phase I scope):
- Todos are independent entities
- No dependencies between todos
- No parent-child or hierarchical structure

### Indexing

**Primary Index**: id attribute
- Used for all operations: update, toggle status, delete
- Guaranteed unique by sequential assignment
- No secondary indexes needed (Phase I scope)

### Constraints Summary

| Constraint | Type | Enforced By |
|------------|------|-------------|
| Unique ID | Primary key | Auto-increment assignment logic |
| Non-empty title | Validation | Input validation before creation/update |
| Numeric ID | Validation | Type conversion and range checking |
| ID existence | Validation | List lookup before operations |
| Immutable ID | Design | No setter/id reassignment |

### Phase II Migration Considerations

**Current design supports future migration**:
- Dictionary structure can be converted to ORM model
- List storage can be replaced with database query
- Validation logic can be extracted to schema validators
- Service layer remains unchanged (separation of concerns)

**Migration path**:
1. Add persistence layer (file or database)
2. Replace in-memory list with data source
3. Keep validation and service logic intact
4. Update CLI only if needed for new features
