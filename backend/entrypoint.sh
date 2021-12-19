#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn backend.wsgi:application --bind 0.0.0.0:8000
gunicorn --certfile=/etc/certs/localhost.crt --keyfile=/etc/certs/localhost.key backend.wsgi:application --bind 0.0.0.0:443