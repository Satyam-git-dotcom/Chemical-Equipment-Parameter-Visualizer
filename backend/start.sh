#!/usr/bin/env bash
set -o errexit

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn equipment_visualizer.wsgi:application \
  --bind 0.0.0.0:$PORT \
  --workers 2s