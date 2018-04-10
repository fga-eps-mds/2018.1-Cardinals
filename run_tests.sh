#!/bin/bash

python manage.py makemigrations

python manage.py migrate

coverage run --source='.' manage.py test

codecov -t 4bbc492c-d908-4f02-8595-8a510df37ef3
