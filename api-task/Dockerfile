ARG PYTHON_VERSION=3.12

# Stage 1: Build dependencies
FROM python:${PYTHON_VERSION}-slim AS builder

ARG NODE_ENV=prod
ENV NODE_ENV=$NODE_ENV

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /api-task
COPY pyproject.toml uv.lock ./

# Install depndencies
RUN uv sync --frozen --no-cache --no-dev

# Copy app
COPY ./app /api-task/app

# Stage 2 - dev environment
FROM builder AS development

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV NODE_ENV=dev

EXPOSE 2025
CMD ["sh", "-c", "uv run pytest ; uv run fastapi dev app/main.py --host 127.0.0.1 --port 2025"]

# Stage 3 - prod environment
FROM python:${PYTHON_VERSION}-slim AS production

ARG NODE_ENV=prod
ENV NODE_ENV=$NODE_ENV

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /api-task
COPY pyproject.toml uv.lock ./

# Install depndencies
RUN uv sync --frozen --no-cache --no-dev

# Remove uv
RUN rm /bin/uv

# COPY --chown=app:app . .

# Copy app
COPY ./app /api-task/app


ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --chown=app:app . .
USER app

RUN groupadd --gid 500 app \
    && useradd --uid 500 --gid app app
USER app:app

EXPOSE 2026

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "2026", "--workers", "4"]