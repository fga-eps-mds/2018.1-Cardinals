#!/bin/bash

rm -rf .coverage
coverage run --source=ranking_commiters/ manage.py test ranking_commiters/ -v 2 --failfast 
coverage report --show-missing
coverage html -i
