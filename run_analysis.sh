#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Static analysis
flake8 --statistics --exit-zero .
