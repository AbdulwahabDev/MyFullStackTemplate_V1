#! /usr/bin/env sh
set -e

# export all .env variables
. ./.env
 
python ./init_db.py

# Start Uvicorn with live reload
exec uvicorn --reload --host 0.0.0.0 --port 3101 --log-level info app.main:app
