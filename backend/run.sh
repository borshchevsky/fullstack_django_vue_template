#!/usr/bin/env bash
./wait-for-it.sh postgres:5432 -t 15
python manage.py makemigrations
python manage.py migrate
python manage.py add_test_query
gunicorn --bind 0.0.0.0:8000 main.wsgi --reload
