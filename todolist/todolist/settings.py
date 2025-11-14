"""
Django settings for ToDoList project.
"""

from pathlib import Path
import os # Keep os import for potential environment variables

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production

SECRET_KEY = 'django-insecure-an%mqu)d%nlx2q4ot!%9)=*g+m76qg1n$d(*s)9_epi%f%^q49'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost']


# ==========================================================
# EMAIL CONFIGURATION (Required for send_mail to work)
# ==========================================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 

# !!! ACTION REQUIRED: REPLACE THESE PLACEHOLDERS !!!
# 1. Your actual Gmail address
EMAIL_HOST_USER = 'todolist.notifiications75@gmail.com' 
# 2. The App Password generated from your Google Account (NOT your regular password)
EMAIL_HOST_PASSWORD = 'YOUR_GMAIL_APP_PASSWORD'

# The default email address for sending
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ==========================================================


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your Apps
    'dashboard',
    'notifications.apps.NotificationsConfig', # <--- ADDED THE NOTIFICATIONS APP
    
    # Third-party Apps
    'rest_framework',
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

# Correcting the case to match your project folder 'ToDoList'
ROOT_URLCONF = 'ToDoList.urls' 


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS needs to be adjusted based on where you store shared templates
        'DIRS': [BASE_DIR / 'dashboard' / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Correcting the case to match your project folder 'ToDoList'
WSGI_APPLICATION = 'ToDoList.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = '/accounts/login/' 

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

LOGIN_REDIRECT_URL = '/dashboard/'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'