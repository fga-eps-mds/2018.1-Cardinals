#!/bin/bash

python manage.py makemigrations

python manage.py migrate

coverage run --source='.' manage.py test