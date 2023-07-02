from .base import *

DEBUG = False

STATIC_URL = 'static/'
STATIC_ROOT = '/usersite/www/public/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',  # Specify the file path here
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file'],
            # 'level': 'DEBUG',
            'level': 'INFO',
            'propagate': True,
        },
    },
}

ALLOWED_HOSTS = [
    # TODO: debug purpose
    # '*'
    '127.0.0.1',
    # 'usersite.test',
]