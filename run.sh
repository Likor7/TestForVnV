#!/bin/bash

echo "Waiting for PostgreSQL to start..."
/app/wait-for-it.sh db:${POSTGRES_PORT:-5432} -- echo "PostgreSQL is up"

echo "Run migrate"
python manage.py migrate

echo "Run application"
python manage.py runserver 0.0.0.0:8000
