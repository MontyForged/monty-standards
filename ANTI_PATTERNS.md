# Anti-Patterns

Common mistakes to avoid in each language. These are the most impactful anti-patterns based on industry research.

## Hierarchy: Rules vs Guidance

| Category | Meaning | Impact | Enforcement |
|----------|---------|--------|-------------|
| **Rules** | Must follow | Causes bugs/security issues | CI failure |
| **Guidance** | Should follow | Maintainability issues | Warning |

See `.monty.yaml` for which category each anti-pattern falls into.

## Node.js

### 1. Callback Hell ❌

**Severity: ERROR**

Nested callbacks make code hard to read, debug, and maintain.

```javascript
// BAD: Deep nesting
getUser(1, function(err, user) {
  if (err) return handleError(err);
  getPosts(user.id, function(err, posts) {
    if (err) return handleError(err);
    getComments(posts[0].id, function(err, comments) {
      if (err) return handleError(err);
      render(comments);
    });
  });
});
```

```javascript
// GOOD: async/await
async function renderUserComments(userId) {
  const user = await getUser(userId);
  const posts = await getPosts(user.id);
  const comments = await getComments(posts[0].id);
  return comments;
}
```

### 2. Unhandled Errors ❌

**Severity: ERROR**

Silent failures that are hard to debug.

```javascript
// BAD: Unhandled promise rejection
fetch('https://api.example.com/data')
  .then(response => response.json())
  // Missing .catch() - error is swallowed!
```

```javascript
// GOOD: Always handle errors
async function getData() {
  try {
    const response = await fetch(url);
    return await response.json();
  } catch (error) {
    logger.error('Failed to fetch data:', error);
    throw error; // or return default value
  }
}

// Or handle at call site
getData().catch(err => handleError(err));
```

### 3. Synchronous I/O ❌

**Severity: ERROR**

Blocking the event loop kills performance.

```javascript
// BAD: Sync operations block the event loop
const fs = require('fs');
const content = fs.readFileSync('large-file.txt', 'utf8');  // BLOCKS!
const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));
```

```javascript
// GOOD: Async I/O
import { readFile } from 'fs/promises';
const content = await readFile('large-file.txt', 'utf8');
```

### 4. God Object/Module ❌

**Severity: WARNING**

Single class with too many responsibilities.

```javascript
// BAD: Everything in one class
class UserManager {
  createUser() { /* ... */ }
  validateEmail() { /* ... */ }
  sendEmail() { /* ... */ }
  formatData() { /* ... */ }
  connectDb() { /* ... */ }
  parseConfig() { /* ... */ }
}
```

```javascript
// GOOD: Focused classes with single responsibility
class UserService { createUser() { /* ... */ } }
class EmailService { sendEmail() { /* ... */ } }
class DataFormatter { format() { /* ... */ } }
```

### 5. Implicit Any ❌

**Severity: WARNING**

No type information leads to runtime errors.

```javascript
// BAD: No type information
function processUser(user) {
  return user.name.toUpperCase(); // What if user is null?
}
```

```javascript
// GOOD: JSDoc annotations
/**
 * @param {Object} user
 * @param {number} user.id
 * @param {string} user.name
 * @returns {Promise<string>}
 */
async function processUser(user) {
  if (!user) return '';
  return user.name.toUpperCase();
}
```

## Python

### 1. Mutable Default Arguments ❌

**Severity: ERROR**

Shared state across function calls causes subtle bugs.

```python
# BAD: Mutable default is shared
def add_item(item, items=[]):
    items.append(item)
    return items

# First call: ['a']
# Second call: ['a', 'b'] OOPS!
```

```python
# GOOD: Use None and initialize inside
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### 2. Bare Except Clause ❌

**Severity: ERROR**

Catching all exceptions hides bugs.

```python
# BAD: Silences all errors
try:
    do_something()
except:
    pass  # What went wrong?
```

```python
# GOOD: Catch specific exceptions
try:
    do_something()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise UserInputError("Check your input") from e
except DatabaseError as e:
    logger.error(f"Database issue: {e}")
    raise ServiceUnavailable("Try again") from e
```

### 3. Missing Type Hints ❌

**Severity: WARNING**

Hard to understand function contracts.

```python
# BAD: No type information
def process_data(data, config):
    return data.get(config['key'], [])
```

```python
# GOOD: Type hints
from typing import Any, List, Dict, Optional

def process_data(
    data: Dict[str, Any],
    config: Dict[str, Any]
) -> List[Any]:
    return data.get(config['key'], [])
```

### 4. Wildcard Imports ❌

**Severity: WARNING**

Namespace pollution and unclear dependencies.

```python
# BAD: from module import *
from utils import *

def helper():
    # What did we actually import?
    pass
```

```python
# GOOD: Import specific symbols
from utils import parse_date, format_number
from datetime import datetime

def process(data: str) -> str:
    parsed = parse_date(data)
    return format_number(parsed)
```

### 5. No Context Manager ❌

**Severity: WARNING**

Resource leaks and unclean shutdowns.

```python
# BAD: Manual resource management
file = open('data.txt', 'r')
content = file.read()
file.close()  # What if read() raises?
# File might not be closed!
```

```python
# GOOD: Context manager
with open('data.txt', 'r') as file:
    content = file.read()
# File automatically closed, even on error
```

## Common Patterns Across Languages

| Anti-Pattern | Node.js | Python | Solution |
|--------------|---------|--------|----------|
| Callback hell | ✅ | N/A | async/await |
| Mutable defaults | N/A | ✅ | None sentinel |
| Unhandled errors | ✅ | ✅ | Try/catch, .catch() |
| Deep nesting | ✅ | ✅ | Early returns |
| Long functions | ✅ | ✅ | Split into smaller |
| Magic numbers | ✅ | ✅ | Use constants |
| Duplicate code | ✅ | ✅ | Extract to function |
| No tests | ✅ | ✅ | Write tests |

## Severity Levels

| Level | Meaning | Enforcement |
|-------|---------|-------------|
| ERROR | Will cause bugs or security issues | CI failure (rule) |
| WARNING | Code smell | Warning (guidance) |
| INFO | Style preference | Suggestion |

## Overrides: Documented Exceptions

Individual repos can override rules/guidance. All overrides MUST be documented in `.monty.yaml`:

```yaml
overrides:
  - anti-pattern: no-mutable-defaults
    override: true
    rationale: "Using functools.lru_cache requires mutable defaults"
    approved-by: tech-lead
    date: 2026-02-04
```

When you encounter an override:
1. Accept it as valid for this project
2. The rationale explains the exception
3. Don't flag it as an issue in code review

## Related

- [docs/ANTI_PATTERNS_PROPOSAL.md](docs/ANTI_PATTERNS_PROPOSAL.md) - Research and sources
- [PATTERNS.md](PATTERNS.md) - Recommended patterns
- `.monty.yaml` - Project-specific rules/guidance configuration
