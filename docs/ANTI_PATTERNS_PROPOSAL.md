# Anti-Patterns Proposal - v2.0

## Research Summary

### Node.js Most Impactful Anti-Patterns

| Rank | Anti-Pattern | Impact | Source |
|------|-------------|--------|--------|
| 1 | Callback Hell | High - readability, maintainability | Reddit, Stack Overflow |
| 2 | Blocking I/O in Event Loop | High - performance | Borstch |
| 3 | Not Handling Errors | High - stability | Reddit, ESLint docs |
| 4 | Global State | Medium - testability | Stack Overflow |
| 5 | Hardcoding Config | Medium - security | Liran Tal |
| 6 | Implicit Any | Medium - type safety | Reddit |
| 7 | No Timeout on APIs | Medium - reliability | Reddit |
| 8 | Sync FS Operations | Medium - performance | Reddit |

### Python Most Impactful Anti-Patterns

| Rank | Anti-Pattern | Impact | Source |
|------|-------------|--------|--------|
| 1 | Mutable Default Arguments | High - correctness | Multiple |
| 2 | Wildcard Imports | High - readability | Reddit, docs |
| 3 | Not Using Type Hints | High - maintainability | Multiple |
| 4 | Catching Broad Exceptions | High - debugging | Medium |
| 5 | File Handle Leaks | Medium - resource | Medium |
| 6 | == vs is Confusion | Medium - correctness | DeepSource |
| 7 | Ignoring Return Values | Medium - correctness | Reddit |
| 8 | Magic Numbers | Low - readability | Common |

## Recommended Anti-Patterns for Monty Standards

### Node.js (Top 5)

1. **Callback Hell** - Use async/await or Promises
2. **Unhandled Errors** - Always catch/handle promises
3. **Global State** - Use dependency injection
4. **Hardcoded Config** - Use environment variables
5. **Missing Timeouts** - Set reasonable timeouts on all I/O

### Python (Top 5)

1. **Mutable Defaults** - Use None sentinel
2. **Wildcard Imports** - Import specific symbols
3. **Missing Type Hints** - Annotate all functions
4. **Bare Except Clauses** - Catch specific exceptions
5. **Not Using Context Managers** - Use `with` for resources

## Proposal: Prioritized Anti-Patterns

### Tier 1: High Impact (Must Avoid)

| Category | Anti-Pattern | Why | Solution |
|----------|-------------|-----|----------|
| Node.js | Callback hell | Blocks event loop, unreadable | async/await |
| Node.js | Unhandled promise rejections | Silent failures | always .catch() |
| Node.js | Sync FS operations | Blocks event loop | Use fs.promises |
| Python | Mutable defaults | Shared state bug | None sentinel |
| Python | Bare except | Swallows errors | Catch specific |
| Both | No error handling | Silent failures | Always handle errors |

### Tier 2: Medium Impact (Should Avoid)

| Category | Anti-Pattern | Why | Solution |
|----------|-------------|-----|----------|
| Node.js | Implicit any | Type errors at runtime | JSDoc/TypeScript |
| Node.js | Global state | Testability issues | DI/params |
| Python | Wildcard imports | Namespace pollution | Specific imports |
| Python | No type hints | Hard to understand | Add annotations |
| Both | Magic numbers | Unclear meaning | Use constants |

### Tier 3: Low Impact (Consider Avoiding)

| Category | Anti-Pattern | Why | Solution |
|----------|-------------|-----|----------|
| Both | Deep nesting | Hard to read | Early returns |
| Both | Long functions | Single responsibility | Split up |
| Both | Duplicate code | DRY principle | Extract to function |

## Recommended Rules for Linters

### ESLint (Node.js)

```json
{
  "rules": {
    "no-callback-literal": "error",
    "no-console": "off",
    "no-implicit-any": "warn",
    "no-sync": "error",
    "handle-callback-err": "error",
    "no-unused-vars": "warn"
  }
}
```

### Ruff (Python)

```toml
[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
B006 = "error"  # mutable defaults
F401 = "error"  # unused imports
E722 = "error"  # bare except
```

## References

- https://github.com/goldbergyoni/nodebestpractices
- https://docs.quantifiedcode.com/python-anti-patterns/
- https://stackoverflow.com/questions/6081184/any-anti-patterns-of-nodejs
- https://www.reddit.com/r/node/comments/dxbe9g/whats_the_worst_antipattern_that_you_see_among/
- https://medium.com/data-science/18-common-python-anti-patterns-i-wish-i-had-known-before-44d983805f0f
