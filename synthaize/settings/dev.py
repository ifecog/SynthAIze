from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEV_DB_NAME'),
        'USER': config('DEV_DB_USER'),
        'PASSWORD': config('DEV_DB_PASSWORD'),
        'HOST': config('DEV_DB_HOST'),
        'PORT': config('DEV_DB_PORT', default='5432'),
    }
}


# Static files settings
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files settings
MEDIA_ROOT = BASE_DIR / 'media'

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('DEV_EMAIL_HOST')
EMAIL_HOST_USER = config('DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('DEV_EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('DEV_EMAIL_PORT')
EMAIL_USE_TLS = config('DEV_EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = config('DEV_DEFAULT_FROM_EMAIL')