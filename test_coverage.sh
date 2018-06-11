#!/bin/bash

rm -rf .coverage
coverage run --source='pull_request_metrics' manage.py test -v 2 --failfast 
coverage report --show-missing --skip-covered
coverage html -i
