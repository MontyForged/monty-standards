# Rule: Record Information in GitHub

**Impact:** High

---

## Summary

Record decisions, context, and discussions in GitHub (issues, PRs, comments) rather than or in addition to prompts. This ensures continuity and preserves institutional knowledge.

## Why This Matters

1. **Continuity** - Future contributors see the full context
2. **Audit Trail** - Decisions are documented where code lives
3. **Searchable** - GitHub search finds decisions, chat doesn't
4. **Accountability** - Who made the decision and why is preserved

## What to Record in GitHub

### Pull Request Comments

- Answers to review questions
- Clarifications on changes
- Trade-offs considered
- Alternative approaches rejected

### Issue Discussions

- Problem definition
- Solution approaches evaluated
- Final decision rationale
- Constraints or dependencies

### Commit Messages

- Why the change was made
- What was considered but rejected
- Related issues or PRs

## Examples

### Good: Answer in GitHub Comment

**Question:** "Can you address the review comments?"

**Don't do:** Just make changes without explanation.

**Do:** Make changes and reply to each comment:

```
@reviewer Yes, the script is now idempotent. It checks
`git config core.hooksPath` before setting up, so you can
rerun it safely.
```

### Good: Document Decision in Issue

**Issue:** Should we use TypeScript or JavaScript?

**Don't:** Decide in chat and forget.

**Do:** Comment in issue with rationale:

```
Decided to use JavaScript with JSDoc for now because:
1. Faster iteration for prototype
2. Team has more JS experience
3. Can add TypeScript later with minimal refactor

If runtime errors exceed threshold, we'll migrate to TypeScript.
```

### Good: Commit Message with Context

```bash
git commit -m "fix: make setup.sh idempotent

Before: git config would overwrite existing hooks
After: Check if hooks already configured before setting

Context: Reviewers asked if script could be safely rerun.
See PR #30 discussion
```

## Anti-Patterns

| Anti-Pattern | Why It's Bad |
|--------------|--------------|
| Answering questions only in chat | Context lost to future contributors |
| Making changes without explaining | Reviewers don't learn reasoning |
| Deciding without documenting | Same decisions get revisited |
| "Mental notes" | Not written down = not remembered |

## Enforcement

- When asked a question about code/design, reply in GitHub if there's a PR/issue
- When making decisions, document rationale in GitHub
- When rejecting alternatives, explain why in GitHub
