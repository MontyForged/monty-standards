# AGENTS.md - For AI Assistants

*How to consume this repository*

## Purpose

This repository contains coding standards, patterns, and anti-patterns - not static templates. When told to "use Monty standards," read this file and apply the guidelines to your code.

## Philosophy

> **Templates are limiting. Guidelines are flexible.**

Instead of copying files, use these standards to:
- Apply consistent patterns across projects
- Avoid common mistakes automatically
- Make code reviews faster
- Onboard quickly to new projects

## Quick Start

1. Read `.monty.yaml` to understand project-specific configuration
2. Check [PATTERNS.md](PATTERNS.md) for recommended approaches
3. Check [ANTI_PATTERNS.md](ANTI_PATTERNS.md) for what to avoid
4. Check [VERSIONING.md](VERSIONING.md) for release strategy

## AI-Readable Configuration

**`.monty.yaml`** contains machine-readable standards:

```yaml
language: node
versioning: semver
rules:
  - name: error-handling
    description: All async operations must handle errors
    enforcement: lint-error
guidance:
  - name: async-await
    description: Prefer async/await over callbacks
overrides:
  - rule: no-mutable-defaults
    override: true
    rationale: "Using lru_cache requires mutable defaults"
```

### Hierarchy of Standards

| Category | Meaning | Can Override? |
|----------|---------|---------------|
| **Rules** | Must follow - causes bugs/security issues | No (without documented exception) |
| **Guidance** | Should follow - maintainability | Yes, with justification |

When consuming a project:
1. Parse `.monty.yaml` for rules and guidance
2. Apply rules strictly (errors in CI)
3. Apply guidance as warnings (code review)
4. Check `overrides` for documented exceptions

## Rules vs Guidance

### Rules (Must Follow)

Rules prevent **bugs, security issues, or data corruption**:

| Language | Rule | Why |
|----------|------|-----|
| Node.js | Error handling | Silent failures corrupt data |
| Node.js | No sync I/O | Blocks event loop |
| Python | No mutable defaults | Shared state causes subtle bugs |
| Python | No bare except | Hides bugs |

**Breaking a rule = CI failure**

### Guidance (Should Follow)

Guidance improves **maintainability and code quality**:

| Language | Guidance | Why |
|----------|----------|-----|
| Node.js | async/await | Readability |
| Python | Type hints | Self-documenting |
| Both | Short functions | Readability |
| Both | Repository pattern | Testability |

**Breaking guidance = Warning**

## Overrides (Documented Exceptions)

Individual repos can override rules/guidance, but MUST document:

```yaml
overrides:
  - rule: no-mutable-defaults
    override: true
    rationale: "Using functools.lru_cache requires mutable defaults"
    approved-by: tech-lead
    date: 2026-02-04
```

When you see an override:
1. Accept it as valid for this project
2. Understand the rationale
3. Don't flag it as an issue

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

## Language-Specific

### Node.js

| Topic | Resource |
|-------|----------|
| Patterns | [PATTERNS.md](PATTERNS.md#nodejs) |
| Anti-Patterns | [ANTI_PATTERNS.md](ANTI_PATTERNS.md#nodejs) |
| Linting | ESLint |

### Python

| Topic | Resource |
|-------|----------|
| Patterns | [PATTERNS.md](PATTERNS.md#python) |
| Anti-Patterns | [ANTI_PATTERNS.md](ANTI_PATTERNS.md#python) |
| Linting | ruff |

## Versioning

See [VERSIONING.md](VERSIONING.md) for:
- Semantic versioning rules
- Changelog format
- Release checklist

## When Writing Code

1. Check `.monty.yaml` for project-specific rules
2. Apply patterns from [PATTERNS.md](PATTERNS.md)
3. Avoid anti-patterns from [ANTI_PATTERNS.md](ANTI_PATTERNS.md)
4. Use conventional commits
5. Handle errors properly
6. **Always run `npm run check` (or project equivalent) before committing**
   - This runs format, lint, and tests
   - If the project has a pre-commit hook, it will catch issues
   - If not, run the check command manually

## When Reviewing Code

1. Check for anti-patterns
2. Verify patterns are applied
3. Check version bump is correct
4. Validate error handling
5. Ensure tests are added

## Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution workflow
- [README.md](README.md) - Project overview

## When in Doubt

1. Check `.monty.yaml` for project-specific rules
2. Read [PATTERNS.md](PATTERNS.md) for recommended approaches
3. Read [ANTI_PATTERNS.md](ANTI_PATTERNS.md) to avoid mistakes
4. Check existing code in the project
5. Ask for clarification
