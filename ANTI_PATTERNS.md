# Anti-Patterns

Common mistakes to avoid in each language.

## Node.js

### Callback Hell ❌

```javascript
// BAD: Nested callbacks are hard to read and maintain
getUser(1, function(err, user) {
  if (err) { return handleError(err); }
  getPosts(user.id, function(err, posts) {
    if (err) { return handleError(err); }
    getComments(posts[0].id, function(err, comments) {
      if (err) { return handleError(err); }
      render(comments);
    });
  });
});
```

```javascript
// GOOD: Use async/await for readability
async function renderUserComments(userId) {
  const user = await getUser(userId);
  const posts = await getPosts(user.id);
  const comments = await getComments(posts[0].id);
  return comments;
}
```

### Implicit Any ❌

```javascript
// BAD: No type information
function processUser(user) {
  return user.name.toUpperCase(); // What if user is null?
}
```

```javascript
// GOOD: Use JSDoc annotations
/**
 * @param {Object} user
 * @param {number} user.id
 * @param {string} user.name
 * @returns {Promise<string>}
 */
async function processUser(user) {
  return user.name.toUpperCase();
}
```

### Mixing Concerns in Controllers ❌

```javascript
// BAD: Business logic in HTTP handler
app.post('/users', async (req, res) => {
  const hashed = await bcrypt.hash(req.body.password, 10);
  const user = await db.users.create({
    name: req.body.name,
    email: req.body.email,
    password: hashed,
  });
  await emailService.sendWelcome(user.email);
  await analytics.track('user_created', user.id);
  res.json(user);
});
```

```javascript
// GOOD: Delegate to service layer
app.post('/users', async (req, res) => {
  const user = await userService.createUser(req.body);
  res.json(user);
});

// src/services/user.service.js
export async function createUser(data) {
  const hashed = await bcrypt.hash(data.password, 10);
  const user = await userRepository.create({
    ...data,
    password: hashed,
  });
  await emailService.sendWelcome(user.email);
  analytics.track('user_created', user.id);
  return user;
}
```

## Python

### Mutable Default Arguments ❌

```python
# BAD: Mutable default is shared across calls
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

### Wildcard Imports ❌

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

def process(data):
    parsed = parse_date(data)
    return format_number(parsed)
```

### Catching Broad Exceptions ❌

```python
# BAD: Silences all errors
try:
    do_something()
except:
    pass  # We don't know what went wrong
```

```python
# GOOD: Catch specific exceptions
try:
    do_something()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise UserInputError("Please check your input") from e
except DatabaseError as e:
    logger.error(f"Database issue: {e}")
    raise ServiceUnavailable("Please try again later") from e
```

## Rust

### Excessive Unwrapping ❌

```rust
// BAD: Panic on any error
fn process_user(id: u64) -> User {
    let user = db.find_by_id(id).unwrap(); // Panics if not found
    user
}
```

```rust
// GOOD: Handle errors explicitly
fn process_user(id: u64) -> Result<User, UserError> {
    db.find_by_id(id)
        .ok_or(UserError::NotFound { id })?
        .try_map(|row| row.try_into())
        .await
        .map_err(|e| UserError::Database { source: e })
}
```

### Unnecessary Clones ❌

```rust
// BAD: Cloning when not needed
fn print_name(user: &User) {
    println!("{}", user.name.clone()); // No need to clone
}
```

```rust
// GOOD: Borrow when possible
fn print_name(user: &User) {
    println!("{}", user.name); // Borrowed reference
}
```

### Using `?` in Main Without Context ❌

```rust
// BAD: Poor error messages
fn main() {
    let config = load_config()?; // What if this fails?
    // ...
}
```

```rust
// GOOD: Add context with anyhow
use anyhow::{Context, Result};

fn main() -> Result<()> {
    let config = load_config()
        .context("Failed to load configuration")?;
    
    let app = build_app(config)
        .context("Failed to build application")?;
    
    app.run().context("Application failed")?;
    Ok(())
}
```

## Go

### Error Swallowing ❌

```go
// BAD: Ignoring errors
func createUser(w http.ResponseWriter, r *http.Request) {
    var user User
    json.NewDecoder(r.Body).Decode(&user)
    // Error? What error?
    saveUser(&user)
    json.NewEncoder(w).Encode(user)
}
```

```go
// GOOD: Handle or log errors
func createUser(w http.ResponseWriter, r *http.Request) {
    var user User
    if err := json.NewDecoder(r.Body).Decode(&user); err != nil {
        http.Error(w, "Invalid request body", http.StatusBadRequest)
        return
    }
    
    if err := saveUser(&user); err != nil {
        http.Error(w, "Failed to save user", http.StatusInternalServerError)
        return
    }
    
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}
```

### Package Bloat ❌

```
// BAD: Everything in main package
main.go
├── User struct
├── User validation
├── User database ops
└── HTTP handlers
```

```
// GOOD: Organized structure
cmd/myapp/main.go
pkg/
├── user/
│   ├── model.go
│   ├── service.go
│   └── repository.go
└── config/
    └── config.go
```

### Mutating Shared State ❌

```go
// BAD: Shared state causes race conditions
var userCache map[string]*User

func GetUser(id string) *User {
    return userCache[id]
}

func SetUser(user *User) {
    userCache[user.ID] = user  // Race condition!
}
```

```go
// GOOD: Use sync.Mutex or channels
type UserCache struct {
    mu   sync.RWMutex
    data map[string]*User
}

func (c *UserCache) Get(id string) (*User, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    user, ok := c.data[id]
    return user, ok
}

func (c *UserCache) Set(user *User) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.data[user.ID] = user
}
```

## Universal Anti-Patterns

| Anti-Pattern | Description | Solution |
|--------------|-------------|----------|
| God Object | Single class/module does too much | Split into focused units |
| Shotgun Surgery | Small changes require many edits | Improve cohesion |
| Magic Numbers | Hardcoded values without explanation | Use constants/enums |
| Premature Optimization | Optimizing before measuring | Profile first |
| Hardcoding Config | Environment-specific values in code | Use config files |
| Missing Tests | No test coverage | Write tests first |
| Long Functions | Functions do too much | Extract to smaller functions |
| Deep Nesting | Excessive indentation levels | Early returns, guard clauses |

## Detection Tools

### Node.js
- ESLint: `no-console`, `no-implicit-any`, `no-callback-literal`

### Python
- Ruff: `B006` (mutable defaults), `F401` (unused imports)

### Rust
- Clippy: Warns about `clone`, `unwrap`, etc.

### Go
- golangci-lint: `errcheck`, `gofmt`, `govet`

## Related

- [PATTERNS.md](PATTERNS.md) - Recommended patterns
- `.monty.yaml` - Anti-pattern configuration for your project
- [VERSIONING.md](VERSIONING.md) - Version strategy
