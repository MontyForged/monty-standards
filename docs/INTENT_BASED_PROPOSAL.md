# Proposal: Intent-Based Monty Standards

## The Problem with Current Approach

Current Monty Standards still includes:
- Language-specific code examples
- Tool recommendations (ESLint, ruff, etc.)
- Configuration snippets

**Problem:** This gets outdated. ESLint rules change. New tools emerge. Languages evolve.

## The Intent-Based Solution

> **Document principles, not implementations.**

Instead of:
- "Use ESLint with these rules"
- "Python should use dataclass"

We say:
- "Validate input before processing"
- "Represent simple data with typed structures"

**Result:** Principles last forever. Tools come and go.

## Proposed Structure

```
monty-standards/
├── PRINCIPLES.md              # Core philosophy (1 page)
├── INTENTS.md                # The what and why (main doc)
├── PATTERNS.md               # Recommended approaches (by intent)
├── ANTI_PATTERNS.md          # Approaches to avoid
├── PROCESS.md                # Git, versioning, PR workflow
├── AGENTS.md                 # How AI should consume this
├── .monty.yaml               # Simple config (just metadata)
└── README.md
```

## Document Examples

### Before (Tool-Specific)

```markdown
## Use Repository Pattern (Node.js)

```javascript
// src/repositories/user.repository.js
export class UserRepository {
  constructor(database) { this.db = database }
  async findById(id) { return this.db.users.findOne({ id }) }
}
```

### After (Intent-Based)

```markdown
## Separate Data Access from Business Logic

**Intent:** Changes to how data is stored shouldn't affect business logic.

**Why:**
- Test business logic without database
- Swap data sources (SQL → NoSQL)
- Reuse business logic across APIs

**What to do:**
- Create abstractions for data operations
- Business logic calls abstractions, not direct DB calls
- Inject dependencies, don't import them

**Example:**
> "When I change how users are stored, I only update one place."
```

## Core Intents (Draft)

### Data Management
1. **Validate input before processing** - Reject invalid data early
2. **Separate data access from logic** - Business rules don't know about storage
3. **Represent simple data with typed structures** - Clarity and IDE support

### Error Handling
4. **Fail explicitly, not silently** - Errors should never be swallowed
5. **Propagate errors to caller** - Don't hide failures

### Code Quality
6. **Keep functions focused** - One purpose per function
7. **Keep modules focused** - One responsibility per module
8. **Avoid hidden state** - Be explicit about dependencies

### Security
9. **Validate all external input** - Never trust unverified data
10. **Don't execute dynamic code** - eval() is a security risk

## Why This Works for AI

**Current:** AI needs to know "Use ESLint rule `no-mutable-defaults`"

**Intent-based:** AI learns "Never use mutable defaults" and can:
- Apply it to any language
- Suggest appropriate linter rules
- Explain the rationale in code review

**Result:** AI becomes more capable, not less.

## What Gets Removed

| Current | Remove Because |
|---------|---------------|
| Code examples | Outdated by new syntax |
| Tool configurations | Tools change constantly |
| Language-specific rules | Same intent across languages |
| ESLint/ruff configs | Can be regenerated |

## What Gets Kept

| Document | Why |
|----------|-----|
| INTENTS.md | Principles last forever |
| PATTERNS.md | Conceptual approaches |
| ANTI_PATTERNS.md | What to avoid, with rationale |
| PROCESS.md | Git workflow, versioning |
| AGENTS.md | How AI consumes this |
| .monty.yaml | Just project metadata |

## Migration Path

1. **Rename PATTERNS.md → INTENTS.md**
   - Rewrite as intent-based principles
   - Remove all code examples

2. **Update ANTI_PATTERNS.md**
   - Keep rationale, remove code
   - Add intent-based explanations

3. **Remove templates/ directory**
   - Delete all code snippets

4. **Simplify .monty.yaml**
   - Just project name, language, versioning
   - No tool configs

## Example: New INTENTS.md Section

```markdown
## Validate Input Before Processing

**Intent:** Reject invalid data at the boundary.

**Rationale:**
- Invalid data in → garbage out
- Catching errors early reduces debugging time
- Invalid data can cause security vulnerabilities

**What this looks like:**
- Type checking on function boundaries
- Range validation for numbers
- Format validation for strings (email, phone, etc.)

**What to avoid:**
- trusting input without checks
- Delaying validation until deep in the code
- Accepting null/undefined without explicit handling
```

## Human Readability

Intent-based docs are also better for humans:

| Old | New |
|-----|-----|
| "Use ESLint rule X" | "Always validate input" |
| 50 lines of config | 3 sentences of principle |
| "Install this tool" | "Here's why this matters" |

## Questions

1. Should we keep `.monty.yaml` at all, or just use project metadata?
2. How detailed should the "what this looks like" sections be?
3. Should we include decision trees for choosing approaches?

---

**Bottom line:** Document *principles*, not *implementations*. The former lasts forever; the latter becomes outdated.
