# Settings used in production

from __future__ import absolute_import
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',               # Or path to database file if using sqlite3
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '', # in init.py
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home/danr/webapps/maghunt_static/'
STATIC_URL = 'http://static.maghunt.com/'

MEDIA_ROOT = '/home/danr/webapps/maghunt_media/'
MEDIA_URL = 'http://media.maghunt.com/'
