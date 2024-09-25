from .base import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PROD_DB_NAME'),
        'USER': config('PROD_DB_USER'),
        'PASSWORD': config('PROD_DB_PASSWORD'),
        'HOST': config('PROD_DB_HOST'),
        'PORT': config('PROD_DB_PORT', default='5432'),
    }
}


# Static files settings
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'      

# Media files settings
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Security settings
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
