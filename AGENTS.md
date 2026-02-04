# AGENTS.md - For AI Assistants

*How to consume this repository*

## Purpose

This repository contains coding standards, processes, and templates for setting up repositories. When told to "use Monty standards," read this file and follow the appropriate templates.

## Quick Start

1. Identify the project type (Node.js, Python, Rust, Go)
2. Copy the template from `templates/<type>/`
3. Copy common files from root (LICENSE, README.md)
4. Apply project-specific changes

## Branch Naming

```
<type>/<issue-number>-<short-description>
```

**Types:**
- `feature` - New functionality
- `bugfix` - Bug fixes
- `docs` - Documentation changes
- `refactor` - Code refactoring
- `chore` - Maintenance tasks

**Example:** `feature/01-add-user-authentication`

## Commit Messages

```
<type>: <brief description>

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `ci`

**Example:**
```
feat: add user authentication

Implemented JWT-based auth with refresh tokens.
Added login/logout endpoints.

Closes #123
```

## Pull Requests

- Create PR from feature branch to main
- Fill out PR template
- Ensure CI passes
- Request review from maintainers
- Squash and merge

## Language-Specific

### Node.js

- Test framework: Vitest
- Linter: ESLint + Prettier
- Package manager: npm (or pnpm)
- See: `templates/node/`

### Python

- Test framework: pytest
- Linter: ruff
- Formatter: black
- See: `templates/python/`

### Rust

- Test framework: built-in `cargo test`
- Linter: rustfmt + clippy
- See: `templates/rust/`

### Go

- Test framework: built-in `go test`
- Linter: golangci-lint
- See: `templates/go/`

## CI/CD

Copy `.github/workflows/ci.yml` as a starting point. Customize for your project type.

## Documentation

- `CONTRIBUTING.md` - Contribution guidelines
- `README.md` - Project overview
- `docs/` - Additional documentation

## When in Doubt

1. Check `CONTRIBUTING.md`
2. Look at existing PRs for examples
3. Ask for clarification
