#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Test related tasks
coverage run --source='.' manage.py test
coverage report
codecov -t 4bbc492c-d908-4f02-8595-8a510df37ef3

# Static analysis
flake8 --statistics --exit-zero .
