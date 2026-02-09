#!/usr/bin/env bash
set -o errexit

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn equipment_visualizer.wsgi:application