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

COPY pyproject.toml poetry.lock {{cookiecutter.repo_name}}/README.md ./

# Using Buildkit cache mounts
RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

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

RUN pip install poetry && poetry install --without dev && pip uninstall poetry

# Run the executable
ENTRYPOINT ["{{cookiecutter.repo_name}}"]
CMD ["10"]
