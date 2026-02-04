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

## Pull Request Template

```markdown
## Description

Brief description of changes

## Testing

- [ ] Tests pass
- [ ] Manual testing completed

## Checklist

- [ ] Code follows project style
- [ ] Documentation updated
- [ ] Tests added/updated
```

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

## Merging

After PR approval:

- Merge via GitHub UI or: `git checkout main && git merge --no-ff feature/01-my-feature`
- Delete the feature branch locally and remotely
- Close the associated issue (use "Fixes #123" in PR description)

## Language-Specific Standards

See `templates/` directory for language-specific configurations.
