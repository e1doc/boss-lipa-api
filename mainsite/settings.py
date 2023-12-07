"""
Django settings for mainsite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import datetime
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xj)*4l980^s+n%t+@6_p*(^v(2b&o122j#v*zk6&3y(524%o6d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['boss-web-api.herokuapp.com','54.251.83.87', '54.179.237.200', 'bossapi.bacoor.gov.ph', '222.127.109.48', 'boss-web-api-v2.herokuapp.com', 'localhost', 'epaymentportal.landbank.com', 'api-checkout.pisopay.com.ph']
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['lipaapi.onedoc.ph', '52.74.21.223']

# Application definition
from dotenv import load_dotenv
load_dotenv()

'''
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# EMAIL_HOST = 'mail.bacoor.gov.ph'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_USER = os.getenv('BOSS_SMTP_USER')
EMAIL_HOST_PASSWORD = os.getenv('BOSS_SMTP_PASSWORD')
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('BOSS_SMTP_USER')
'''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lipa.eservices@gmail.com'
EMAIL_HOST_PASSWORD = 'pwoi pdbp inhf ubrn'

#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
#ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
#ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'api.apps.ApiConfig',
    'staff.apps.StaffConfig',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'phonenumber_field',
    'corsheaders',
    'storages',
    'channels',
    'sequences.apps.SequencesConfig',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'mainsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mainsite.wsgi.application'
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lipa_db',
        'USER': 'postgres',
        'PASSWORD': 'admin1doc',
        'HOST': 'lipa-db.clgdglzwk6qc.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lipa_gov_db',
        'USER': 'postgres',
        'PASSWORD': 'admin1doc',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
'''

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_bacoor2',
        'USER': 'bacoor',
        'PASSWORD': 'bacoor',
        'HOST': 'db',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
'''

AUTHENTICATION_BACKENDS = ['core.custom_auth.CaseInsensitiveModelBackend'] + [
    # other authentication backends
]

DJOSER= {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE': True,

    'SEND_CONFIRMATION_EMAIL': True,
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
          'drf_jwt_2fa.authentication.Jwt2faAuthentication',
          'rest_framework.authentication.TokenAuthentication',
          'rest_framework.authentication.BasicAuthentication',
          'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 3
}

JWT2FA_AUTH = {
    # Length of the verification code (digits)
    'CODE_LENGTH': 7,

    # Characters used in the verification code
    'CODE_CHARACTERS': '0123456789',
    # Function that sends the verification code to the user
    'CODE_SENDER': 'drf_jwt_2fa.sending.send_verification_code_via_email',

    # From Address used by the e-mail sender
    'EMAIL_SENDER_SUBJECT_OVERRIDE': None,
    'CODE_TOKEN_THROTTLE_RATE': '500/3h',
}

JWT_AUTH = {
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=2),
    'JWT_VERIFY_EXPIRATION': False,
    # 'JWT_AUTH_COOKIE': '2fa-jwt',
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# CORS_ALLOW_CREDENTIALS = True
# SESSION_COOKIE_SAMESITE = None

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# aws settings
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = 'private'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_ENDPOINT_URL= f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'api.custom_storage.PrivateMediaStorage'
# s3 private media settings
PRIVATE_MEDIA_LOCATION = 'private'
PRIVATE_FILE_STORAGE = 'api.custom_storage.PrivateMediaStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'core.User'
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))
#location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'mainsite/static')
]

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ASGI_APPLICATION = 'mainsite.asgi.application'
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

#APPEND_SLASH = False