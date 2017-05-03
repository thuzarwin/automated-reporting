"""
Django settings for reporting project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5)!dc%xc6622p!!wa54qaf+$_8v5a29ax04+$b)nc8x@-jtu$_'

# custom database settings?
try:
    import reporting.settings_debug
    DEBUG = reporting.settings_debug.DEBUG
    print("Using debug settings from 'settings_debug.py'")
except ImportError:
    DEBUG = False
    print("""
        Using default debug settings (ie debugging turned off)

        Create 'settings_debug.py' for custom settings, e.g. for turning debugging on:
        DEBUG = True

        SECURITY WARNING: don't run with debug turned on in production!
        """)

ALLOWED_HOSTS = []

# authentication

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Application definition

INSTALLED_APPS = [
    'database',
    'leave',
    'lpp',
    'reporting',
    'supervisors',
    'django_python3_ldap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

APPS_LIST = [
    'leave',
    'lpp',
    'supervisors',
]

APPS_SHORT = {
    'leave': 'Leave',
    'lpp': 'LPP',
    'supervisors': 'Supervisors',
}

APPS_LONG = {
    'leave': 'Annual Leave',
    'lpp': 'Low performing pass-rates',
    'supervisors': 'Supervisor Register',
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'reporting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'reporting/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

# only use TemporaryFileUploadHandler for file uploads
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

WSGI_APPLICATION = 'reporting.wsgi.application'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# custom database settings?
try:
    import reporting.settings_db
    DATABASES = reporting.settings_db.DATABASES
    print("Using database settings from 'settings_db.py'")
except ImportError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    print("""
        Using default database settings
        Create 'settings_db.py' for custom settings, e.g.:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'db_name',
                'USER': 'db_user',
                'PASSWORD': 'db_user_password',
                'HOST': '',
                'PORT': 'db_port_number',
            }
        }
        """)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    'reporting/static/',
]

# general options
# NB: this gets added to the context of templates
REPORTING_OPTIONS = {
    'supervisor.only_phd': True,
}

# LDAP settings

# custom settings?
try:
    import reporting.settings_ldap
    print("Using settings from 'settings_ldap.py'")
    AUTHENTICATION_BACKENDS = reporting.settings_ldap.AUTHENTICATION_BACKENDS
    LDAP_AUTH_URL = reporting.settings_ldap.LDAP_AUTH_URL
    LDAP_AUTH_USE_TLS = reporting.settings_ldap.LDAP_AUTH_USE_TLS
    LDAP_AUTH_CONNECTION_USERNAME = reporting.settings_ldap.LDAP_AUTH_CONNECTION_USERNAME
    LDAP_AUTH_CONNECTION_PASSWORD = reporting.settings_ldap.LDAP_AUTH_CONNECTION_PASSWORD
    LDAP_AUTH_SEARCH_BASE = reporting.settings_ldap.LDAP_AUTH_SEARCH_BASE
    LOGGING = reporting.settings_ldap.LOGGING
except ImportError:
    print("""
        No LDAP settings defined!
        Create 'settings_ldap.py' for custom settings, see details:"
        https://github.com/etianen/django-python3-ldap

        For example:

        AUTHENTICATION_BACKENDS = [
            'django_python3_ldap.auth.LDAPBackend',
        ]

        LDAP_AUTH_URL = "ldaps://server.example.com:636"
        LDAP_AUTH_USE_TLS = False
        LDAP_AUTH_CONNECTION_USERNAME = None
        LDAP_AUTH_CONNECTION_PASSWORD = None
        LDAP_AUTH_SEARCH_BASE = "ou=Active,ou=People,dc=example,dc=com"
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                },
            },
            "loggers": {
                "django_python3_ldap": {
                    "handlers": ["console"],
                    "level": "INFO",
                },
            },
        }
        """)

# LPP settings

# custom settings?
try:
    import reporting.settings_lpp
    print("Using settings from 'settings_lpp.py'")
    PERL = reporting.settings_lpp.PERL
    LPP_SCRIPT = reporting.settings_lpp.LPP_SCRIPT
except ImportError:
    print("""
        Using default LPP settings
        Create 'settings_lpp.py' for custom settings, e.g.:"
        PERL = "/usr/bin/perl"
        LPP_SCRIPT = "/usr/local/bin/LPP/pass-rates"
        """)
    PERL = "/usr/bin/perl"
    LPP_SCRIPT = "/usr/local/bin/LPP/pass-rates"

