FROM python:{python_version}-buster AS builder

# Install poetry
RUN pip install poetry==1.8.2

# Setup env
ENV LANG C.UTF-8 \
    LC_ALL C.UTF-8 \
    PYTHONDONTWRITEBYTECODE 1 \
    PYTHONFAULTHANDLER 1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN mkdir .venv && poetry install --without dev --no-root  && rm -rf $POETRY_CACHE_DIR

FROM python:{python_version}-slim-buster as runtime

# Copy virtual env from builder stage
ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY {{cookiecutter.repo_name}} ./{{cookiecutter.repo_name}}

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}.main"]
CMD ["10"]
