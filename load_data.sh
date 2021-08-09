#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata custom_user_app.json
python manage.py loaddata forum_app.json