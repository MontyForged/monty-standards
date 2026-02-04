# Contributing to Monty Standards

## Branch Naming Convention

Include the GitHub issue number at the start of branch names for easy tracking.

```
<type>/<issue-number>-<short-description>
```

**Types:**

- `feature` - New functionality
- `bugfix` - Bug fixes
- `docs` - Documentation changes
- `refactor` - Code refactoring
- `chore` - Maintenance tasks

**Examples:**

- `feature/01-user-authentication`
- `bugfix/23-fix-encoding-detection`
- `docs/29-update-contributing-guide`

## Quick Workflow

```bash
# Start a new feature
git checkout -b feature/01-my-feature

# Make changes and commit
git add .
git commit -m "feat: add user authentication"

# Push and create PR
git push -u origin feature/01-my-feature
```

## Making Changes

1. Create a new branch from `main`
2. Make your changes
3. Test changes if applicable
4. Commit with clear message
5. Push and create PR

## Commit Message Convention

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `refactor` - Code change without feature/fix
- `test` - Adding tests
- `ci` - CI changes
- `chore` - Maintenance tasks

**Version Bumps:**

| Commit Type | Version Bump |
|-------------|--------------|
| `feat:` | MINOR |
| `feat!:` | MAJOR |
| `fix:` | PATCH |
| `BREAKING CHANGE:` | MAJOR |

## Versioning

All projects should use **Semantic Versioning** by default. See [VERSIONING.md](VERSIONING.md) for:

- Version format (MAJOR.MINOR.PATCH)
- When to increment each component
- Changelog format
- Release checklist

Set `versioning: none` in `.monty.yaml` to disable versioning.

## Design Patterns

See [PATTERNS.md](PATTERNS.md) for recommended patterns:

- Repository pattern for data access
- Factory pattern for test fixtures
- Service layer for business logic
- And more...

## Anti-Patterns

See [ANTI_PATTERNS.md](ANTI_PATTERNS.md) for common mistakes:

- Node.js: Callback hell, unhandled errors, sync I/O
- Python: Mutable defaults, bare except, missing type hints

## Supported Languages

| Language | Linter |
|----------|--------|
| Node.js | ESLint |
| Python | ruff |

## Merging

After PR approval:

1. Merge via GitHub UI
2. Delete the feature branch
3. Close the issue (use "Fixes #123" in PR description)

## Anti-Pattern Research

When adding new anti-patterns, follow the research process:

1. Search for common anti-patterns in the language
2. Document sources in [docs/ANTI_PATTERNS_PROPOSAL.md](docs/ANTI_PATTERNS_PROPOSAL.md)
3. Add to [ANTI_PATTERNS.md](ANTI_PATTERNS.md) with examples
4. Update [.monty.yaml](.monty.yaml) configuration

## Code Review Guidelines

For reviewers:

- Check for anti-patterns in [ANTI_PATTERNS.md](ANTI_PATTERNS.md)
- Ensure patterns match [PATTERNS.md](PATTERNS.md)
- Verify version bump is correct
- Validate error handling
- Check documentation updates
