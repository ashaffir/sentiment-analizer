#! /bin/sh

set -e

echo "********* Setup Scraper *********"
ls -la /code/app
ls -la /code/app/db
uvicorn app.main:app --host 0.0.0.0 --port 8000

