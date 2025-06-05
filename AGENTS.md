# Agent Guidelines

- **Coding style**: Format code with `black` and order imports with `isort`. Use Google style docstrings without type info in the Args/Returns sections. Add type annotations to all functions.
- **Lint**: Run `poetry run black --check spans tests` and `poetry run isort --check spans tests`.
- **Tests**: Run `poetry run pytest`.
- **Tests behavior**: Prefer avoiding mocks. Never patch imports at module level; patch within individual tests only when necessary.
- **Commit/PR**: Write concise commit messages describing the change. Avoid `-n` flags with git commands.
