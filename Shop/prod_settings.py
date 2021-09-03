import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop_db',
        'USER': 'foxhole',
        'PASSWORD': 'WSXcde123qwe',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


SECRET_KEY = 'django-insecure-lsln4r-_4hrdje45of3vnbo784q9%qcmrwjs&nhk^0n#0u&hdx'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)