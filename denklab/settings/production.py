from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['denklab.org']

INSTALLED_APPS += ['anymail']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_variable('DATABASES_NAME'),
        'USER': get_env_variable('DATABASES_USER'),
        'PASSWORD': get_env_variable('DATABASES_PASSWORD'),
    }
}

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'

ADMINS = ['ernesto@rico-schmidt.name']

MANAGERS = ADMINS

SERVER_EMAIL = 'noreply@rico-schmidt.name'

DEFAULT_FROM_EMAIL = 'noreply@rico-schmidt.name'

SECURE_HSTS_SECONDS = 3600

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True

ANYMAIL = {
    'MAILGUN_API_KEY': get_env_variable('ANYMAIL_MAILGUN_API_KEY'),
    'MAILGUN_SENDER_DOMAIN': get_env_variable('ANYMAIL_MAILGUN_SENDER_DOMAIN')
}
