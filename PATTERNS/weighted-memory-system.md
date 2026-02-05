# Weighted Memory System

**Status:** Pattern  
**Tested in:** clawdit

A memory system that accumulates knowledge over time, with weighted importance and decay only on neglect.

---

## Concept

Projects accumulate knowledge as they evolve. This system captures that knowledge with:

- **Weighted importance** - Critical knowledge persists, minor knowledge fades
- **Neglect-based decay** - Memories fade only when ignored, not based on time
- **Human boosting** - Humans can emphasize important lessons
- **AI referencing** - Referenced memories strengthen

## Why

Without a memory system:

- Lessons learned are forgotten
- Same mistakes are repeated
- Important decisions are lost

With this system:

- Knowledge accumulates
- Important lessons persist
- Decisions are documented and referenced

## Implementation

### Directory Structure

```
.monty/
├── .monty.yaml           # Project configuration
├── README.md             # Memory system guide
├── rules/               # High-impact guidelines
├── decisions/           # Specific choices made
└── memories/            # Weighted knowledge
```

### Memory Format

```markdown
# Memory: <title>

**Date:** YYYY-MM-DD
**Author:** <name/AI>
**Severity:** <critical|high|medium|low|note>
**Weight:** <initial weight>
**Last Referenced:** YYYY-MM-DD
**Decay Scheduled:** <true|false>

---

## Situation

<What happened?>

## What We Learned

<Key insight>

## Application

<Where/how applied>

---

## Boost this memory

Human: "Boost this memory" → +30
AI: Reference in commit → +10

## Archive Status

Current Weight: <number>
Threshold: 20
Status: <Active|Archived>
Decay: Only if not referenced for 90 days
```

### Weight by Severity

| Severity | Initial Weight | Decay |
|----------|---------------|-------|
| Critical | 100 | Never |
| High | 70 | -5 per 90 days of no reference |
| Medium | 40 | -5 per 90 days of no reference |
| Low | 20 | -5 per 90 days of no reference |
| Note | 10 | -5 per 90 days of no reference |

### Boosting

| Source | Weight Gain |
|--------|-------------|
| Human: "Boost this memory" | +30 |
| AI: Reference in commit | +10 |

### Decay (Neglect-Based)

**Key principle:** Memory decays only if IGNORED, not based on time.

```
Memory referenced → weight +10, decay reset
Memory ignored for 90 days → -5
Still ignored → continue decaying
Weight < 20 → archive (preserve in git, remove from active)
```

### Archive Status

```
Active: weight >= 20
Archive: weight < 20 (move to archive/)
Restore: "Restore memory X" → weight 50, active
```

Archived memories are preserved in git history and can be restored.

## Query Examples

| Query | Result |
|-------|--------|
| "Check memories" | Active memories (weight >= 20) |
| "Check all memories" | Read all including archived |
| "Boost this memory" | Human boosts weight +30 |
| "Archive status" | Show all memories by weight |
| "Critical memories" | Only weight 100 |
| "Restore memory X" | Restore archived memory |

## Example Memories

### High Severity (Weight: 70)

```markdown
# Memory: Dead Code Removal

**Date:** 2026-02-04
**Author:** Brian
**Severity:** high
**Weight:** 70
**Last Referenced:** 2026-02-04

---

During the scanner library refactor, old code was left behind.

## What We Decided

Rule: Remove dead code during refactoring.

What counts as dead code:
- Unused files
- Unused functions
- Commented code
- Unused imports

## Application

Applied in PR #21: Removed root test.js
```

### Low Severity (Weight: 20)

```markdown
# Memory: Email Validation

**Date:** 2026-02-04
**Author:** AI Review
**Severity:** low
**Weight:** 20

---

Question: Should we add email format validation?

Decision: NOT NOW

Rationale: Focus on cleanup before features.

When to revisit: After scanner refactoring is complete.
```

## Usage in Projects

1. Create `.monty/` directory
2. Add `README.md` with this guide
3. Create memories as lessons are learned
4. Reference memories in commits to boost weight
5. Archive weak memories

## Related

- Tested in: clawdit (PR #28)
- Pattern: Weighted Memory System
