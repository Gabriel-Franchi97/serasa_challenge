#!/usr/bin/env sh
set -e

# Run migrations
alembic upgrade head

# Run server with Uvicorn
exec uvicorn serasa_challenge.main:app --host=${SERVER_HOST} --port=${SERVER_PORT} --log-level $SERVER_LOG_LEVEL --reload --http h11
