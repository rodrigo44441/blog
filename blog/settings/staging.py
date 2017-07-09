from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dn9d2ldurabga', 
        'USER': 'dzxmkkxqoyundu', 
        'PASSWORD': 'crSDkCjopGHEC48J2Y0ORiBdIR',
        'HOST': 'ec2-23-21-234-218.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# nada