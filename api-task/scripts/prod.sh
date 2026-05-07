#!/usr/bin/env bash
source .env-prod
uv run uvicorn app.main:app --host $HOST --port $PORT