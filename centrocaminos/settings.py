"""
Django settings for centrocaminos project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import dj_database_url

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='La clave')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = ['*']
CORS_ALLOW_ALL_ORIGINS = True



# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ccapp',
    'rest_framework',
    'rest_framework.authtoken'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'centrocaminos.urls'

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

WSGI_APPLICATION = 'centrocaminos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.config  (     
           default='sqlite:///sqllite.3', 
           conn_max_age=600    )
}
        
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {

     'DEFAULT_AUTHENTICATION_CLASSES': [

             'rest_framework.authentication.TokenAuthentication'

     ]
}



CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Especialidad/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Especialidad/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Persona/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Persona/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Tecnico/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Tecnico/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Paciente/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Paciente/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Funcionario/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Funcionario/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/TutorPaciente/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/TutorPaciente/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Prestador/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Prestador/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Pago/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Pago/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Sesion/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Sesion/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Tratamiento/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Tratamiento/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Evaluacion/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Evaluacion/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Consulta/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Consulta/")

CSP_DEFAULT_SRC = ("'self'", "http://127.0.0.1:8000/api/Registro/")
CSP_DEFAULT_SRC = ("'self'", "https://centrocaminos.onrender.com/api/Registro/")