# Agent Guidelines

- **Coding style**: Format code with `black` and order imports with `isort`. Use Google style docstrings without type info in the Args/Returns sections. Add type annotations to all functions.
- **Lint**: Run `poetry run black --check spans tests` and `poetry run isort --check spans tests`.
- **Tests**: Run `poetry run pytest`.
