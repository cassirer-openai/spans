#!/usr/bin/env bash
set -euo pipefail

# Ensure pip is up to date
python -m pip install --upgrade pip

# Install Poetry for dependency management if missing
if ! command -v poetry >/dev/null; then
    pip install poetry
fi

# Install project and development dependencies
poetry install --no-interaction

# TODO: add steps for optional tools or environments if necessary

