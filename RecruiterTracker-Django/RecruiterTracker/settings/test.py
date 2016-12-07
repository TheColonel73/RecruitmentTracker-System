import os
from .base import *

DEBUG = True

TEST_RUNNER = 'RecruiterTrackerApp.testrunner.ManagedModelTestRunner'

DATABASE_ROUTERS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    },
}