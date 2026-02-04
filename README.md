# Monty Standards

Coding standards, guidelines, and processes for AI assistants and human developers.

This repository contains templates, workflows, and documentation that can be consumed by AI bots or humans to understand how to set up and manage repositories following consistent standards.

## What's Inside

### 📋 Standards Documentation

| File | Purpose |
|------|---------|
| [AGENTS.md](AGENTS.md) | Guidance for AI assistants |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution workflow |
| [VERSIONING.md](VERSIONING.md) | SemVer strategy |
| [PATTERNS.md](PATTERNS.md) | Design patterns by language |
| [ANTI_PATTERNS.md](ANTI_PATTERNS.md) | Common mistakes to avoid |

### 🛠️ Templates

| Language | Framework | Test | Linter | Formatter |
|----------|-----------|------|--------|-----------|
| [Node.js](templates/node/) | ES Modules | Vitest | ESLint | Prettier |
| [Python](templates/python/) | - | pytest | ruff | black |
| [Rust](templates/rust/) | cargo | built-in | rustfmt | clippy |
| [Go](templates/go/) | modules | built-in | golangci-lint | gofmt |

### 🔧 Configuration

| File | Purpose |
|------|---------|
| [.monty.yaml](.monty.yaml) | AI-readable project config |
| [.github/workflows/ci.yml](.github/workflows/ci.yml) | CI template |

## Quick Start

### For AI Assistants

Read [AGENTS.md](AGENTS.md) first. It explains how to consume this repository.

### For Humans

```bash
# Clone this repo
git clone https://github.com/MontyForged/monty-standards.git

# Copy Node.js template
cp -r monty-standards/templates/node your-project/

# Copy configuration
cp monty-standards/.monty.yaml your-project/
cp monty-standards/CONTRIBUTING.md your-project/
```

## Project Structure

```
monty-standards/
├── .monty.yaml              # AI-readable config
├── AGENTS.md                # AI guidance
├── CONTRIBUTING.md          # Contribution workflow
├── VERSIONING.md            # SemVer strategy
├── PATTERNS.md              # Design patterns
├── ANTI_PATTERNS.md         # What to avoid
├── README.md
├── LICENSE
├── .github/
│   └── workflows/
│       └── ci.yml           # CI template
└── templates/
    ├── node/                # Node.js template
    ├── python/              # Python template
    ├── rust/                # Rust template
    └── go/                  # Go template
```

## Why Monty Standards?

### 🎯 For AI Assistants
- **AI-readable config** - `.monty.yaml` lets bots understand project rules
- **Clear patterns** - Bots can apply correct design patterns
- **Anti-pattern detection** - Avoid common mistakes automatically

### 👨‍💻 For Humans
- **Consistent onboarding** - New developers get up to speed fast
- **Best practices built-in** - Don't reinvent the wheel
- **Cross-language familiarity** - Same patterns across projects

## Versioning

All projects should use **Semantic Versioning**. See [VERSIONING.md](VERSIONING.md) for:

- When to bump MAJOR/MINOR/PATCH
- Changelog format
- Release checklist

## License

MIT - See [LICENSE](LICENSE)
