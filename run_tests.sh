#!/bin/bash

python manage.py makemigrations
python manage.py migrate
coverage run --source='.' manage.py test

RESULT=$?
if [ ${RESULT} != "0" ]; then
	echo -e "\nOh no, some test failed!"
	exit ${RESULT}
fi

echo -e "\nGreat, all tests succeed!\n"

coverage report

exit 0
