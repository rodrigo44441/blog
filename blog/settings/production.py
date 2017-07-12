from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'indarra_db', 
        'USER': 'rodrigo', 
        'PASSWORD': 'rodrigo',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_ROOT='/opt/statics/blog/'

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
