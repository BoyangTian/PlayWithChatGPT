from .base import *

DEBUG = True

STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django.template': {
            'handlers': ['console'],
            # 'level': 'DEBUG',
            'level': 'INFO',
            'propagate': True,
        },
    },
}