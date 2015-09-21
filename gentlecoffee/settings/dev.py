from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!


SECRET_KEY = env('SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


def custom_show_toolbar(request):
    return not request.get_full_path().startswith('/userbar/')


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'gentlecoffee.settings.dev.custom_show_toolbar'
}

try:
    from .local import *
except ImportError:
    pass
