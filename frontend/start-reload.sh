#! /usr/bin/env sh
set -e


# Start Uvicorn with live reload
exec uvicorn --reload --host 0.0.0.0 --port 3006 --log-level info frontend_app.main:app