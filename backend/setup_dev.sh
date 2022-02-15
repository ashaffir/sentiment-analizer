#!/bin/sh
export SECRET_KEY=foo
export DEBUG=1
export DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
export SQL_ENGINE="django.db.backends.postgresql_psycopg2"
export SQL_DATABASE="sentiment"
export SQL_USER="alfreds"
export SQL_PASSWORD="!Q2w3e4r%T"
export SQL_HOST="db"
export SQL_PORT="5432"
