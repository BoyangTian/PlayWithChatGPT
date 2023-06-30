from .base import *

DEBUG = False

STATIC_URL = '/prefix'

# need to run manage.py collectstatic command to move static files
STATIC_ROOT = '/usersite/www/public'

STATIC_URL = '/static/'
STATIC_ROOT = '/usersite/www/public/static/'

ALLOWED_HOSTS = [
    # TODO: debug purpose
    # '*'
    '127.0.0.1',
    # 'usersite.test',
]