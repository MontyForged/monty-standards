# AGENTS.md - For AI Assistants

*How to consume this repository*

## Purpose

This repository contains coding standards, processes, and templates for setting up repositories. When told to "use Monty standards," read this file and follow the appropriate templates.

## Quick Start

1. Identify the project type (Node.js, Python, Rust, Go)
2. Read `.monty.yaml` for project-specific configuration
3. Copy the template from `templates/<type>/`
4. Copy common files from root (LICENSE, README.md)
5. Apply project-specific changes

## AI-Readable Configuration

**`.monty.yaml`** contains machine-readable standards:

```yaml
language: node
versioning: semver
patterns:
  - name: repository
    description: Use repository pattern for data access
anti_patterns:
  - name: callback-hell
    description: Nested callbacks make code hard to read
```

When consuming a project:
1. Read `.monty.yaml` to understand project-specific rules
2. Check [PATTERNS.md](PATTERNS.md) for recommended patterns
3. Check [ANTI_PATTERNS.md](ANTI_PATTERNS.md) for what to avoid
4. Check [VERSIONING.md](VERSIONING.md) for version bump rules

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

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `ci`, `chore`

**Version Bump Detection:**
- `feat:` → MINOR version bump
- `fix:` → PATCH version bump
- `BREAKING CHANGE:` or `feat!:` → MAJOR version bump

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
- Patterns: [PATTERNS.md](PATTERNS.md#nodejs)
- Anti-patterns: [ANTI_PATTERNS.md](ANTI_PATTERNS.md#nodejs)

### Python

- Test framework: pytest
- Linter: ruff
- Formatter: black
- Type hints: Required
- See: `templates/python/`
- Patterns: [PATTERNS.md](PATTERNS.md#python)
- Anti-patterns: [ANTI_PATTERNS.md](ANTI_PATTERNS.md#python)

### Rust

- Test framework: built-in `cargo test`
- Linter: rustfmt + clippy
- Error handling: thiserror, anyhow
- See: `templates/rust/`
- Patterns: [PATTERNS.md](PATTERNS.md#rust)
- Anti-patterns: [ANTI_PATTERNS.md](ANTI_PATTERNS.md#rust)

### Go

- Test framework: built-in `go test`
- Linter: golangci-lint
- Error handling: explicit with context
- See: `templates/go/`
- Patterns: [PATTERNS.md](PATTERNS.md#go)
- Anti-patterns: [ANTI_PATTERNS.md](ANTI_PATTERNS.md#go)

## CI/CD

Copy `.github/workflows/ci.yml` as a starting point. Customize for your project type.

## Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [README.md](README.md) - Project overview
- [VERSIONING.md](VERSIONING.md) - Semantic versioning strategy
- [PATTERNS.md](PATTERNS.md) - Design patterns by language
- [ANTI_PATTERNS.md](ANTI_PATTERNS.md) - Common mistakes to avoid
- `docs/` - Additional documentation

## Versioning

All projects use **Semantic Versioning**. See [VERSIONING.md](VERSIONING.md) for:
- Version format (MAJOR.MINOR.PATCH)
- When to increment each component
- Changelog format
- Release checklist

## When in Doubt

1. Check `.monty.yaml` for project-specific rules
2. Read [PATTERNS.md](PATTERNS.md) for recommended patterns
3. Read [ANTI_PATTERNS.md](ANTI_PATTERNS.md) to avoid common mistakes
4. Check existing code in the project for examples
5. Ask for clarification
