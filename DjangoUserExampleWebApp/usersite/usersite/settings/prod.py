from .base import *

DEBUG = True

STATIC_URL = 'static/'
# STATIC_ROOT = '/shared/usersite/static/'
# STATIC_ROOT = '/usersite/static/'
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]


    # In order to let prod static file work, we need this: https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
STATIC_ROOT = BASE_DIR / 'static'

print("!!!!")
print(STATIC_ROOT)

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',  # Specify the file path here
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
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