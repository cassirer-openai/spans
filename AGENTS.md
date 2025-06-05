# Agent Guidelines

- **Coding style**: Format code with `black` and order imports with `isort`.
- **Lint**: Run `poetry run black --check spans tests` and `poetry run isort --check spans tests`.
- **Tests**: Run `poetry run pytest`.
- **TDD**: When fixing or adding features, first add a failing test and run it.
  After confirming the failure, implement the change and run tests again to
  show they pass. You **MUST** Cite both executions in your output.
