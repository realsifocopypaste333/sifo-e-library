from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fpu%lu==abtc!p)mztrw+p=+-sm!pbcqu)pefg%!-+p!a2e67#'








ALLOWED_HOSTS = ['*', 'herokuapp.com', 'sifosuperweb.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
