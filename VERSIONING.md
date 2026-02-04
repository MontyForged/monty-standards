# Versioning Strategy

Monty Standards uses **Semantic Versioning (SemVer)** for all projects.

## Version Format

```
MAJOR.MINOR.PATCH
```

| Component | Description | When to Increment |
|-----------|-------------|-------------------|
| MAJOR | Breaking changes | Incompatible API changes |
| MINOR | New features | Backward-compatible additions |
| PATCH | Bug fixes | Backward-compatible fixes |

## Rules

### MAJOR (X.0.0)

Increment when you make **breaking changes**:

- Remove or rename a public API
- Change function signatures
- Alter expected behavior in a way that breaks consumers
- Remove configuration options

**Trigger keywords:**
- `BREAKING CHANGE:` in commit footer
- `feat!:` (exclamation mark) in commit type

### MINOR (0.X.0)

Increment when you **add new features**:

- Add new functions or methods
- Add new configuration options
- Add new optional parameters
- Deprecate old features (without removal)

**Trigger keyword:** `feat:`

### PATCH (0.0.X)

Increment for **bug fixes and refinements**:

- Fix incorrect behavior
- Improve performance
- Refactor internals without behavior change
- Update documentation

**Trigger keywords:** `fix:`, `docs:`, `refactor:`

## Version Bump Detection

Monty Standards uses **Conventional Commits** to automatically determine version bumps:

```bash
# These trigger MINOR
feat: add user authentication
feat(auth): add OAuth support

# These trigger PATCH  
fix: resolve memory leak in connection pool
docs: update API documentation

# These trigger MAJOR
feat!: change database schema
BREAKING CHANGE: API endpoint path changed
```

## Changelog Format

Every release should include a changelog entry:

```markdown
## [2.1.0] - 2026-02-04

### Added
- User authentication module (#123)
- OAuth2 support for Google and GitHub (#124)

### Changed
- Updated dependencies to latest versions (#125)

### Deprecated
- `oldFunction()` - Use `newFunction()` instead (#126)

### Removed
- Removed deprecated `v1-api` endpoint (#127)

### Fixed
- Memory leak in connection pool (#128)
- Race condition in user creation (#129)

### Security
- Updated vulnerable dependency (#130)

### Internal
- Refactored database layer for better testability (#131)
```

## Release Checklist

Before releasing:

- [ ] All tests pass
- [ ] Coverage meets minimum (80%)
- [ ] Documentation updated
- [ ] Changelog entry added
- [ ] Version bumped in config
- [ ] PR merged to main

## Version Lifecycle

```
Development (0.0.x)
├── Alpha (unstable, for testing)
├── Beta (feature-complete, testing)
└── RC (release candidate, final testing)

1.0.0+
├── Stable release
├── Subsequent patch/minor releases
└── Major releases for breaking changes
```

## Example Version Bump Workflow

```bash
# Make changes
feat: add user login feature
fix: resolve timeout issue

# Determine bump (patch in this case)
git log --oneline --since="v1.2.0" | grep -E "^(feat|fix)" | wc -l
# If only fixes -> PATCH
# If features added -> MINOR
# If breaking -> MAJOR

# Update version
npm version patch  # Updates package.json and creates tag
# or手动:
sed -i 's/"version": "1.2.3"/"version": "1.2.4"/' pyproject.toml

# Create changelog entry
git log --oneline --since="v1.2.3" > CHANGELOG.md

# Tag and release
git tag v1.2.4
git push origin main --tags
```

## Related

- [CONTRIBUTING.md](CONTRIBUTING.md) - Commit message conventions
- [PATTERNS.md](PATTERNS.md) - Design patterns by language
- `.monty.yaml` - Project-specific versioning config
