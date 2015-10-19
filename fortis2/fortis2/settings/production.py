# import os
# from django.conf import settings

# DEBUG = False

# TEMPLATE_DEGUG = True
# DATABASES = settings.DATABASES
# # Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
# #BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# # Allow all host headers
# ALLOWED_HOSTS = ['*']

# SHARE_URL = "https://fathomless-inlet-5326.herokuapp.com/?ref="

# # Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
from django.conf import settings

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	#root of project

	# Quick-start development settings - unsuitable for production
	# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

	# SECURITY WARNING: keep the secret key used in production secret!
	
SECRET_KEY = 'a(!2(3@*at&$om+braen^ahefbx4f-2lecbn56ovjj2o8^sx4!'

	# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True


ALLOWED_HOSTS = ['https://fathomless-inlet-5326.herokuapp.com']
	#purchasing domain name http://name.com



	# Application definition

INSTALLED_APPS = (
	    #django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #my apps
    'panelpage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'fortis2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fortis2.wsgi.application'


	# Database
	# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#from .db_password import DBPASS
DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

#import dj_database_url
#DATABASES['default'] = dj_database_url.config()
#DATABASES['default'] =  dj_database_url.config()

# # Enable Connection Pooling
# DATABASES['default']['ENGINE'] = 'django_postgrespool'


	# Internationalization
	# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/1.8/howto/static-files/

	# STATIC_URL = '/static/'

	# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static","our_static")

	# STATICFILES_DIRS = (
	#     os.path.join(BASE_DIR, "static","our_static"),
 #    # '/var/www/static/',
	# )



