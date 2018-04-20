"""
    HEROKU:

    Config vars change the way your app behaves. In addition to creating your own, some add-ons come with their own.
"""
import os
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print "BASE_DIR-->", BASE_DIR
print "PROJECT_ROOT-->", PROJECT_ROOT

#################################################
#            HEROKU CONFIGURATION              #
#################################################

DATABASES = {}

SECRET_KEY = None;
DEBUG=True
IS_HEROKU_ENV=False
try:
    #
    # PROD CONFIGURATION
    #

    SECRET_KEY = config('SECRET_KEY')

    DEBUG = config('DEBUG', default=False, cast=bool)

    # PostegreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    IS_HEROKU_ENV=True
except Exception as e:
    print ">>>> LOCAL TEST ENVIRONMENT"
    print str(e)
    #
    # Default values
    #
    SECRET_KEY = 'mzr2%=l*+p87^9t1x@0km^ej*xx0+32v657d)lp@sh$i)sms4g'

    DATABASE_PATH = os.path.join(BASE_DIR, 'pycon9.db')
    DATABASES['default'] =  dj_database_url.config(default='sqlite:///'+DATABASE_PATH)
