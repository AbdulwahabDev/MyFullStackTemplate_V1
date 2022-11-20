#! /usr/bin/env sh
set -e

 
python ./init_db.py

# Start Uvicorn with live reload
exec uvicorn --reload --host 0.0.0.0 --port 3003 --log-level info auth_app.main:app
