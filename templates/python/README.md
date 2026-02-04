# Python Template

Copy these files to your Python project:

```
.
├── pyproject.toml
├── src/
│   └── __init__.py
└── tests/
    └── test_example.py
```

## Usage

```bash
# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter (ruff)
ruff check .

# Format code
black .

# Full check
ruff check . && black --check . && pytest
```
