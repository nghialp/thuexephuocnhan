"""
Django settings for CMS project.

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
SECRET_KEY = 'u2(f^mjb)yy%fky$fpk7mk^^40s)*=&!wl$9lsg%x9%=)^di47'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False

#ALLOWED_HOSTS = ['localhost']

DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'carservice',
    #'fontawesome',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'phonenumber_field',
    'djmoney',
    # 'ckeditor',
    # 'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'CMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'car_development',
        'USER': 'car',
        'PASSWORD': '1197614',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    ('css' , os.path.join(STATIC_ROOT, 'css')),
    ('js' , os.path.join(STATIC_ROOT, 'js')),
    ('images' , os.path.join(STATIC_ROOT, 'images')),
    ('font-awesome' , os.path.join(STATIC_ROOT, 'font-awesome')),
    ('vendor' , os.path.join(STATIC_ROOT, 'vendor')),
    ('admin' , os.path.join(STATIC_ROOT, 'admin')),
)

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

LOGIN_REDIRECT_URL = '/admin'
LOGOUT_REDIRECT_URL = '/admin/login'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# MEDIA_ROOT = STATIC_URL + 'images/uploads/' #os.path.join(STATIC_ROOT  , 'images')

# MEDIA_URL = STATIC_URL + 'images/uploads/'

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

# CKEDITOR_JQUERY_URL = STATIC_ROOT + 'js/jquery.min.js'

# CKEDITOR_UPLOAD_PATH = STATIC_ROOT + '/images/uploads/'
# CKEDITOR_IMAGE_BACKEND = STATIC_ROOT + "/images/uploads/"

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': block,
#     },
# }

###################################

# UPLOAD HANDLE
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]