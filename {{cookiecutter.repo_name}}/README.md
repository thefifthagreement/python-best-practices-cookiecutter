# {{cookiecutter.project_name}}

## Setup
```sh
# create a new virtual env
mkvirtualenv {{cookiecutter.project_name}}

# Install and lock dependencies
poetry install

# Setup pre-commit and pre-push hooks
pre-commit install -t pre-commit
pre-commit install -t pre-push

# Test the project (compute the 10th element of the Fibonnaci suite)
{{cookiecutter.project_name}} 10 
# should return 55
```

## Credits
This package was created with Cookiecutter and the [thefifthagreement/python-best-practices-cookiecutter](https://github.com/thefifthagreement/python-best-practices-cookiecutter.git) project template.
