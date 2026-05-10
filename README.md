# docker-maestro-dlu

A collection of Docker projects and experiments — companion material for the [Docker Maestro](https://dockermaestro.pl) course.

---

## Repository contents

| Directory | Description |
|-----------|-------------|
| [`api-task/`](./api-task/) | FastAPI app with a production-grade Dockerfile (multi-stage build) |

---

## api-task

A minimal **FastAPI** application demonstrating a production-ready approach to containerising a Python app.

> **Docker Hub:** `docker pull rayzki/api-task:latest` or `docker pull rayzki/api-task:0.3`

### Tech stack

- **Python 3.12**
- **FastAPI** (with standard extras)
- **uv** — fast Python package manager
- **Uvicorn** — ASGI server (4 workers in production)

### Dockerfile architecture (multi-stage build)

```
Stage 1: builder
  └── install dependencies via uv (no dev deps)
       ├── Stage 2: development  ← hot-reload, tests, port 2025
       └── Stage 3: production   ← non-root user, health check, port 2026
```

### Running — development

```bash
cd api-task

# Build and run the development container
docker build --target development -t api-task:dev .
docker run --rm -p 2025:2025 --name api-task-dev api-task:dev
```

App available at: `http://localhost:2025/health`

> The development container runs `pytest` first, then starts the server in hot-reload mode.

### Running — production

```bash
cd api-task

# Build the production image with a version tag
docker build --target production --build-arg VERSION=0.3.0 -t api-task:0.3 .

# Run the container
docker run -d -p 2026:2026 --name api-task api-task:0.3
```

App available at: `http://localhost:2026/health`

Example response:

```json
{
  "status": "ok",
  "name": "api-task",
  "version": "0.3.0",
  "env": "prod"
}
```

### Publishing the image

```bash
docker tag api-task:0.3 <your-username>/api-task:0.3
docker tag api-task:0.3 <your-username>/api-task:latest
docker push <your-username>/api-task:0.3
docker push <your-username>/api-task:latest
```

---

## Key Docker concepts demonstrated

| Concept | Where |
|---------|-------|
| **Multi-stage build** | `api-task/Dockerfile` — 3 stages: builder, development, production |
| **Non-root user** | `app:app` (UID 500 / GID 500) in the production stage |
| **Health check** | HTTP GET on `/health`, every 30s, timeout 10s, 3 retries |
| **Build ARG** | `PYTHON_VERSION`, `VERSION`, `ENVIRONMENT` |
| **Dev/prod separation** | Different CMD, port, env vars, and dev dependencies per stage |
| **Image size reduction** | `uv`/`uvx` removed after dependency installation in production |

---

## Requirements

- Docker Engine >= 24.x
- Docker Compose >= 2.x (optional)

---

## Resources

- [Docker Maestro — course](https://dockermaestro.pl)
- [FastAPI — docs](https://fastapi.tiangolo.com)
- [uv — docs](https://docs.astral.sh/uv/)
