# Monty Standards

Coding standards, guidelines, and processes for AI assistants and human developers.

This repository contains templates, workflows, and documentation that can be consumed by AI bots or humans to understand how to set up and manage repositories following consistent standards.

## What's Inside

- **Process Standards** - Branch naming, PR templates, commit conventions
- **Language Templates** - Node.js, Python, Rust, Go templates
- **GitHub Workflows** - CI/CD patterns and automation
- **Documentation Templates** - CONTRIBUTING, README, etc.
- **Bootstrap Scripts** - Tools to create/apply standards

## Usage

### For AI Assistants

Read `AGENTS.md` first to understand how to consume this repository.

### For Humans

Clone or fork this repository, then copy the templates you need:

```bash
git clone https://github.com/MontyForged/monty-standards.git
cp -r monty-standards/templates/node your-project/
cp monty-standards/.github/workflows/ your-project/.github/
cp monty-standards/CONTRIBUTING.md your-project/
```

## License

MIT - See [LICENSE](LICENSE)
