#!/bin/sh

set -xe

echo "run migrations"
python3 manage.py migrate

echo "load initial data"
python3 manage.py loaddata data

echo "start the app"
exec "$@"
