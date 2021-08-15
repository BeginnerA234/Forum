#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata custom_user_app.json
python manage.py loaddata forum_app.json
exec gunicorn backend.wsgi:application -b 0.0.0.0:8000 -w 4 --reload