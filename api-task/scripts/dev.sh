#!/usr/bin/env bash
source .env-dev
uv run uvicorn app.main:app --reload --host $HOST --port $PORT
