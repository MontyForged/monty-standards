# Monty Standards

Coding standards, guidelines, and processes for AI assistants and human developers.

This repository contains **patterns, anti-patterns, and processes** - not templates. AI assistants and humans can use these guidelines to create consistent, maintainable projects without being tied to specific file structures.

## Philosophy

> **Templates are limiting. Guidelines are flexible.**

Instead of copying static templates, use these standards to:
- Apply consistent patterns across projects
- Avoid common mistakes
- Make AI-assisted code reviews faster
- Onboard new developers quickly

## What's Inside

### 📋 Documentation

| File | Purpose |
|------|---------|
| [AGENTS.md](AGENTS.md) | How AI assistants should consume this repo |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Branch naming, commit conventions |
| [VERSIONING.md](VERSIONING.md) | SemVer strategy |

### 🛠️ Patterns

| Directory | Purpose |
|----------|---------|
| [PATTERNS.md](PATTERNS.md) | Design patterns by language |
| [PATTERNS/](PATTERNS/) | Proven patterns (weighted memory, etc.) |

### ⚠️ Anti-Patterns

| File | Purpose |
|------|---------|
| [ANTI_PATTERNS.md](ANTI_PATTERNS.md) | Common mistakes to avoid |

### ⚙️ Configuration

| File | Purpose |
|------|---------|
| [.monty.yaml](.monty.yaml) | AI-readable project configuration |

### 📄 Research

| File | Purpose |
|------|---------|
| [docs/ANTI_PATTERNS_PROPOSAL.md](docs/ANTI_PATTERNS_PROPOSAL.md) | Research sources for anti-patterns |

## Quick Start

### For AI Assistants

Read [AGENTS.md](AGENTS.md) first. It explains how to consume this repository.

### For Humans

1. **Read patterns**: See [PATTERNS.md](PATTERNS.md) for what to do
2. **Avoid anti-patterns**: See [ANTI_PATTERNS.md](ANTI_PATTERNS.md) for what to avoid
3. **Configure project**: Copy [.monty.yaml](.monty.yaml) and customize

## Supported Languages

| Language | Patterns | Anti-Patterns | Linting |
|----------|-----------|---------------|---------|
| Node.js | ✅ | ✅ | ESLint |
| Python | ✅ | ✅ | ruff |

## Featured Patterns

| Pattern | Status | Tested In |
|---------|--------|-----------|
| [Weighted Memory System](PATTERNS/weighted-memory-system.md) | Pattern | clawdit |

A memory system that accumulates knowledge over time, with weighted importance and decay only on neglect.

## Project Structure

```
monty-standards/
├── .monty.yaml              # AI-readable config
├── AGENTS.md                # AI guidance
├── CONTRIBUTING.md          # Workflow
├── VERSIONING.md            # SemVer
├── PATTERNS.md              # Pattern index
├── PATTERNS/               # Pattern implementations
│   └── weighted-memory-system.md
├── ANTI_PATTERNS.md         # Mistakes to avoid
├── README.md
├── LICENSE
└── docs/
    └── ANTI_PATTERNS_PROPOSAL.md
```

## Example: Starting a New Project

**Human says:** "Create a Node.js project called 'my-api'"

**AI does:**
1. Creates project with Node.js structure
2. Configures ESLint with Monty rules
3. Applies repository pattern for data access
4. Avoids callback hell by using async/await
5. Adds error handling to all async functions

Result: Consistent project that follows Monty Standards without copying templates.

## Why This Works

| Approach | Problem | Monty Solution |
|----------|---------|----------------|
| Static templates | One-size-fits-all | Flexible guidelines |
| Copy-paste | Stale code | Living documentation |
| Implicit rules | Inconsistent | Explicit patterns |

## Versioning

All projects should use **Semantic Versioning** by default. See [VERSIONING.md](VERSIONING.md) for:
- When to bump MAJOR/MINOR/PATCH
- Changelog format
- Release checklist

Set `versioning: none` in `.monty.yaml` to disable.

## License

MIT - See [LICENSE](LICENSE)
