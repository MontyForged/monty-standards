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
# Then create PR at: https://github.com/MontyForged/<repo>/pull/new/feature/01-my-feature
```

## Making Changes

1. Create a new branch from `main`
2. Make your changes
3. Test: See language-specific template
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

**Examples:**
```
feat: add user authentication

Implements JWT-based auth with refresh tokens.

Closes #123
```

```
fix: resolve memory leak in connection pool

The leak occurred when connections were not properly closed.

Fixes #456
```

```
feat!: change database schema

BREAKING CHANGE: The user table schema has changed.
Please run the migration script before deploying.

See: #789
```

## Pull Request Template

```markdown
## Description

Brief description of changes

## Type

- [ ] Feature
- [ ] Bug Fix
- [ ] Documentation
- [ ] Refactoring
- [ ] CI/CD

## Testing

- [ ] Tests pass
- [ ] Coverage maintained (min 80%)
- [ ] Manual testing completed

## Checklist

- [ ] Code follows project style
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] Version bumped (if applicable)
- [ ] Anti-patterns checked
```

## Versioning

All projects use **Semantic Versioning (SemVer)**. See [VERSIONING.md](VERSIONING.md) for:

- Version format (MAJOR.MINOR.PATCH)
- When to increment each component
- Changelog format
- Release checklist

**Quick Reference:**

```
MAJOR (1.0.0) - Breaking changes
MINOR (0.1.0) - New features (backward-compatible)
PATCH (0.0.1) - Bug fixes (backward-compatible)
```

## Design Patterns

See [PATTERNS.md](PATTERNS.md) for recommended patterns by language:

- Repository pattern for data access
- Factory pattern for test fixtures
- Service layer for business logic
- And more...

## Anti-Patterns to Avoid

See [ANTI_PATTERNS.md](ANTI_PATTERNS.md) for common mistakes:

- Node.js: Callback hell, implicit any
- Python: Mutable defaults, wildcard imports
- Rust: Excessive unwrap, unnecessary clones
- Go: Error swallowing, package bloat

## Language-Specific Standards

See `templates/` directory for language-specific configurations:

- `templates/node/` - Node.js with Vitest, ESLint
- `templates/python/` - Python with pytest, ruff
- `templates/rust/` - Rust with cargo
- `templates/go/` - Go with modules

## Merging

After PR approval:

1. Merge via GitHub UI or: `git checkout main && git merge --no-ff feature/01-my-feature`
2. Delete the feature branch locally and remotely
3. Close the associated issue (use "Fixes #123" in PR description)
4. Update changelog if this is a release

## Code Review Guidelines

For reviewers:

- Check for anti-patterns in [ANTI_PATTERNS.md](ANTI_PATTERNS.md)
- Ensure patterns match [PATTERNS.md](PATTERNS.md)
- Verify version bump is correct
- Check test coverage
- Validate documentation updates
