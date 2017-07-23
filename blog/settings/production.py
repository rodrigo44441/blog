from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inda_db', 
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
