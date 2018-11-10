# assert warnings are enabled
import os
import warnings


warnings.simplefilter('ignore', Warning)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

INSTALLED_APPS = []

SECRET_KEY = 'foobar'

CAFE24_SMS_SETTINGS = {
    'USER_ID': 'userid',
    'SECURE_KEY': 'securekey',
    'SENDER': '000-0000-0000',
    'TEST_MODE': True,
}
