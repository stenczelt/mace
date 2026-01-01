# Format
python -m black .
python -m isort .

# Check
python -m pylint --rcfile=pyproject.toml mace tests scripts

# Tests (excluding slow tests for faster checks)
python -m pytest -m "not slow" tests
