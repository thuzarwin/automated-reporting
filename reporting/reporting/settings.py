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

ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'dbbackend',
    'leave',
    'lpp',
    'reporting',
    'supervisors',
    'hyperlinkgrades',
    'django_python3_ldap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maintenance_mode',
]

APPS_LIST = [
    'leave',
    'hyperlinkgrades',
    'lpp',
    'supervisors',
]

APPS_SHORT = {
    'leave': 'Leave',
    'hyperlinkgrades': 'Hyperlink Grades',
    'lpp': 'LPP',
    'supervisors': 'Supervisors',
}

APPS_LONG = {
    'leave': 'Annual Leave',
    'hyperlinkgrades': 'Hyperlink Grades',
    'lpp': 'Low performing pass-rates',
    'supervisors': 'Supervisor Register',
}

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
                'maintenance_mode.context_processors.maintenance_mode',
            ],
            'debug': True,
        },
    },
]


MAINTENANCE_MODE_IGNORE_URLS = [
    "/$",
    "/database/*",
    "/hyperlinkgrades/*",
]


# only use TemporaryFileUploadHandler for file uploads
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

WSGI_APPLICATION = 'reporting.wsgi.application'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'


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

# custom settings?
try:
    import reporting.settings_custom

    print("Using custom settings from 'settings_custom.py'")

    DEBUG = reporting.settings_custom.DEBUG
    SECRET_KEY = reporting.settings_custom.SECRET_KEY
    DATABASES = reporting.settings_custom.DATABASES
    REPORTING_OPTIONS = reporting.settings_custom.REPORTING_OPTIONS
    DOC_MOD_LIB = reporting.settings_custom.DOC_MOD_LIB
    JAVA = reporting.settings_custom.JAVA
    PERL = reporting.settings_custom.PERL
    LPP_SCRIPT = reporting.settings_custom.LPP_SCRIPT
    LOCAL_USERS = True
    MIDDLEWARE_CLASSES = reporting.settings_custom.MIDDLEWARE_CLASSES
    if reporting.settings_custom.USE_LDAP:
        LOCAL_USERS = False
        AUTHENTICATION_BACKENDS = reporting.settings_custom.AUTHENTICATION_BACKENDS
        LDAP_AUTH_URL = reporting.settings_custom.LDAP_AUTH_URL
        LDAP_AUTH_USE_TLS = reporting.settings_custom.LDAP_AUTH_USE_TLS
        LDAP_AUTH_CONNECTION_USERNAME = reporting.settings_custom.LDAP_AUTH_CONNECTION_USERNAME
        LDAP_AUTH_CONNECTION_PASSWORD = reporting.settings_custom.LDAP_AUTH_CONNECTION_PASSWORD
        LDAP_AUTH_SEARCH_BASE = reporting.settings_custom.LDAP_AUTH_SEARCH_BASE
    if reporting.settings_custom.USE_SHIBBOLETH:
        LOCAL_USERS = False
        AUTHENTICATION_BACKENDS = reporting.settings_custom.AUTHENTICATION_BACKENDS

except ImportError:
    print("'settings_custom.py' not found, using default values!")

    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    REPORTING_OPTIONS = {
        'supervisor.only_phd': True,
    }
    DOC_MOD_LIB = "/usr/local/bin/fcms-doc-modifier/lib"
    JAVA = "/usr/bin/java"
    PERL = "/usr/bin/perl"
    LPP_SCRIPT = "/usr/local/bin/LPP/pass-rates"

    LOCAL_USERS = True
    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'maintenance_mode.middleware.MaintenanceModeMiddleware',
    ]
