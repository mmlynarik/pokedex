FROM python:3.13.2-slim AS base

RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    ca-certificates && \
    apt-get clean

ENV PYTHONUNBUFFERED=True
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-dev --no-install-project

FROM base AS builder

WORKDIR /app
COPY . .

RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-dev


FROM python:3.13.2-slim
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin/:$PATH"
CMD ["sh", "-c", "cd src/djangoproject; python manage.py migrate; python manage.py importpokeapi; uvicorn pokedex.asgi:application --host 0.0.0.0 --port 8000"]
