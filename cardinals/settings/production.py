from .base import *

DEBUG = False
ALLOWED_HOSTS = ['cardinals.herokuapp.com']
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbuh9r1vhq2m7a',
        'USER': 'wsdfeinerozdxl',
        'PASSWORD': 'f699ebf0f159ca1a43dac9e715f00fd644474c555104e918e249dc1fe2614cb3',
        'HOST': 'ec2-54-225-96-191.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
