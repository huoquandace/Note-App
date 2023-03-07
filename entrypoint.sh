#!/bin/bash

cd /app
# until python manage.py check; do
#     sleep 1s
# done

# postgresql
while ! nc -z postgres_container 5432 ; do
    echo "Waiting for the Postgresql Server"
    sleep 1
done

# mysql
while ! nc -z mysql_container 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

$@