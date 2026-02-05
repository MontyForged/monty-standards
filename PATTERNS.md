# Design Patterns

Recommended design patterns for each supported language.

## Node.js

### Repository Pattern

Separate data access logic from business logic.

```javascript
// src/repositories/user.repository.js
export class UserRepository {
  constructor(database) {
    this.db = database
  }

  async findById(id) {
    return this.db.users.findOne({ id })
  }

  async create(data) {
    return this.db.users.create(data)
  }

  async update(id, data) {
    return this.db.users.update({ id }, data)
  }

  async delete(id) {
    return this.db.users.delete({ id })
  }
}

// Usage in service
export class UserService {
  constructor(userRepository) {
    this.userRepository = userRepository
  }

  async getUser(id) {
    return this.userRepository.findById(id)
  }
}
```

### Factory Pattern

Create objects without specifying exact class.

```javascript
// src/factories/user.factory.js
export function createUser(data) {
  return {
    id: data.id || generateId(),
    name: data.name,
    email: data.email,
    createdAt: new Date(),
    ...data
  }
}

// Test fixture
export function createTestUser(overrides = {}) {
  return createUser({
    name: 'Test User',
    email: 'test@example.com',
    ...overrides
  })
}
```

### Service Layer

Business logic in services, not controllers.

```javascript
// src/services/user.service.js
export class UserService {
  constructor(userRepository, emailService) {
    this.userRepository = userRepository
    this.emailService = emailService
  }

  async registerUser(data) {
    // Business logic here
    const user = await this.userRepository.create(data)
    await this.emailService.sendWelcome(user.email)
    return user
  }

  async updateProfile(userId, data) {
    // Validation, business rules, etc.
    if (data.email && await this.emailExists(data.email)) {
      throw new Error('Email already exists')
    }
    return this.userRepository.update(userId, data)
  }
}
```

## Python

### Dataclass

Simple data objects with type hints.

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime
    role: str = "user"

@dataclass
class UserCreateRequest:
    name: str
    email: str
    role: Optional[str] = None

@dataclass
class UserResponse:
    id: int
    name: str
    email: str
    role: str
```

### Context Manager

Resource handling with automatic cleanup.

```python
from contextlib import contextmanager

@contextmanager
def database_connection():
    conn = open_connection()
    try:
        yield conn
    finally:
        conn.close()

# Usage
with database_connection() as conn:
    conn.execute("SELECT * FROM users")

# Or use @contextmanager for more complex setup
@contextmanager
def timer(name):
    start = time.time()
    yield
    print(f"{name}: {time.time() - start:.2f}s")

with timer("expensive_operation"):
    do_something()
```

### Abstract Base Class

Define interfaces and contracts.

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def find_by_id(self, id: int):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

class UserRepository(Repository):
    def __init__(self, db):
        self.db = db

    def find_by_id(self, id: int):
        return self.db.users.find(id)
```

## Rust

### Builder Pattern

Complex struct construction.

```rust
pub struct User {
    name: String,
    email: String,
    age: u32,
    active: bool,
}

impl User {
    pub fn builder() -> UserBuilder {
        UserBuilder::default()
    }
}

#[derive(Default)]
pub struct UserBuilder {
    name: Option<String>,
    email: Option<String>,
    age: u32,
    active: bool,
}

impl UserBuilder {
    pub fn name(mut self, name: &str) -> Self {
        self.name = Some(name.to_string());
        self
    }

    pub fn email(mut self, email: &str) -> Self {
        self.email = Some(email.to_string());
        self
    }

    pub fn age(mut self, age: u32) -> Self {
        self.age = age;
        self
    }

    pub fn active(mut self, active: bool) -> Self {
        self.active = active;
        self
    }

    pub fn build(self) -> Result<User, &'static str> {
        Ok(User {
            name: self.name.ok_or("name is required")?,
            email: self.email.ok_or("email is required")?,
            age: self.age,
            active: self.active,
        })
    }
}
```

### Error Chaining

Proper error handling with `?` and `thiserror`.

```rust
use thiserror::Error;

#[derive(Error, Debug)]
pub enum UserError {
    #[error("user not found: {id}")]
    NotFound { id: u64 },
    
    #[error("invalid email: {email}")]
    InvalidEmail { email: String },
    
    #[error("database error: {source}")]
    Database { source: sqlx::Error },
}

pub async fn get_user(id: u64) -> Result<User, UserError> {
    sqlx::query_as!(User, "SELECT * FROM users WHERE id = ?", id)
        .fetch_one(&pool)
        .await
        .map_err(|e| UserError::Database { source: e })
}
```

## Go

### Functional Options

Flexible configuration without breaking changes.

```go
package options

type Option func(*config)

func WithTimeout(timeout time.Duration) Option {
    return func(c *config) {
        c.timeout = timeout
    }
}

func WithRetry(retry int) Option {
    return func(c *config) {
        c.retry = retry
    }
}

type config struct {
    timeout time.Duration
    retry   int
}

func NewConfig(opts ...Option) *config {
    c := &config{
        timeout: 30 * time.Second,
        retry:   3,
    }
    for _, opt := range opts {
        opt(c)
    }
    return c
}

// Usage
cfg := NewConfig(
    WithTimeout(60 * time.Second),
    WithRetry(5),
)
```

### Package Structure

Clear organization for maintainability.

```
cmd/
├── myapp/
│   └── main.go          # Entry point
pkg/
├── api/
│   ├── handler.go
│   └── router.go
├── models/
│   └── user.go
├── services/
│   └── user_service.go
└── repository/
    └── user_repo.go
internal/
├── auth/
│   └── auth.go
└── middleware/
    └── logging.go
```

## Pattern Selection Guide

| Pattern | Use When | Language |
|---------|----------|----------|
| Repository | Data access abstraction | All |
| Factory | Object creation, test fixtures | All |
| Service Layer | Business logic organization | All |
| Dataclass | Simple data objects | Python |
| Context Manager | Resource handling | Python |
| ABC/Interface | Contracts, polymorphism | Python, Go |
| Builder | Complex construction | Rust, Go |
| Functional Options | Configurable APIs | Go |
| Result/Option | Error handling | Rust |

## Related

- [ANTI_PATTERNS.md](ANTI_PATTERNS.md) - What to avoid
- [VERSIONING.md](VERSIONING.md) - Release and versioning strategy
- `.monty.yaml` - Project pattern configuration
