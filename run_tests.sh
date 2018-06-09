#!/bin/bash

python manage.py makemigrations

python manage.py migrate

coverage run manage.py test

RESULT=$?
if [ ${RESULT} != "0" ]; then
	echo -e "\nOh no, some test failed!"
	exit ${RESULT}
fi

echo -e "\nGreat, all tests succeed!\n"

coverage report

codecov -t 4bbc492c-d908-4f02-8595-8a510df37ef3

exit 0
