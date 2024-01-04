#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
DJANGO_SUPERUSER_USERNAME=testuser 
DJANGO_SUPERUSER_PASSWORD=testpass 
DJANGO_SUPERUSER_EMAIL="admin@admin.com" 
python3 manage.py createsuperuser --no-input
