#!/bin/sh

set -xe

echo "run migrations"
python3 manage.py migrate

echo "start the app"
exec "$@"
