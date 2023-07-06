from .base import *

DEBUG = False

# INSTALLED_APPS += [
#     # In order to let prod static file work, we need this: https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
#     'whitenoise.runserver_nostatic',
# ]

# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# ]

# STATIC_URL = 'static/'
# STATIC_ROOT = '/shared/restsite/static/'
# STATIC_ROOT = '/restsite/static/'


# In order to let prod static file work, we need this: https://stackoverflow.com/questions/5836674/why-does-debug-false-setting-make-my-django-static-files-access-fail
STATIC_ROOT = BASE_DIR / 'static'

print("!!!!")
# print(STATIC_ROOT)

# STATICFILES_DIRS = [
#     BASE_DIR / 'static',
# ]
# print("!!!!")
# print(STATICFILES_DIRS)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            # 'class': 'logging.StreamHandler',
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
    # 'restsite.test',
]