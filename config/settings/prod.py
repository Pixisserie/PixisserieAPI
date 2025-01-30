from .base import *

SECRET_KEY = env('PROD_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['(pythonanywhere ID).pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}