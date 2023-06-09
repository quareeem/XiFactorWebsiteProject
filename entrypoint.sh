#!/bin/sh

echo "Waiting for postgres..."

sleep 5

echo "PostgreSQL started"

python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

exec "$@"
