#! /usr/bin/env sh
set -e


# export all .env variables
. ./.env

# Start Uvicorn with live reload
exec uvicorn --reload --host 0.0.0.0 --port 3006 --log-level info app.main:app