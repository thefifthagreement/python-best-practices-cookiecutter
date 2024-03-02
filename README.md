# Python Best Practices Cookiecutter

Best practices [cookiecutter](https://github.com/audreyr/cookiecutter) template based on the [python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter.git)

## Requirements
Locally installed:
- [poetry](https://python-poetry.org/)
- [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)

## Features
- Dependency management with [poetry](https://python-poetry.org/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Deployment ready with [Docker](https://docker.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)

## Quickstart
```sh
# Install pipx if cookiecutter is not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:sourcery-ai/python-best-practices-cookiecutter

# Enter project directory
cd <repo_name>

# Initialise git repo
git init

# create a new virtual env
mkvirtualenv <repo_name>

# Install and lock dependencies
poetry install

# Setup pre-commit and pre-push hooks
pre-commit install -t pre-commit
pre-commit install -t pre-push
```
