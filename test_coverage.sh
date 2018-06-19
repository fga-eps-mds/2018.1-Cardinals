#!/bin/bash

rm -rf .coverage
coverage run manage.py test -v 2 --failfast 
coverage report --show-missing
coverage html -i
