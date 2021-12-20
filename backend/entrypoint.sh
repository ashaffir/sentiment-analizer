#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

echo ">>>>>>>>>>>> Current User... >>>>>>>>>>>>>"
whoami

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# gunicorn backend.wsgi:application --bind 0.0.0.0:8000
gunicorn --certfile=/etc/certs/localhost.crt --keyfile=/etc/certs/localhost.key backend.wsgi:application \
  --bind 0.0.0.0:443 \
  --log-level=debug \
  --log-file=/home/ubuntu/logs/gunicorn.log