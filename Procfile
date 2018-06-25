release: python manage.py makemigrations && python manage.py migrate
web: bin/start-nginx gunicorn cardinals.wsgi --log-file -
