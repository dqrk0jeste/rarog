#!/bin/sh

set -xe

# echo "make migrations"
# python3 manage.py makemigrations

echo "run migrations"
python3 manage.py migrate

echo "start the app"
exec "$@"
