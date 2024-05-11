from pathlib import Path
import os
import environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = env('SECRET_KEY')
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = 'RENDER' not in os.environ

# DOMAIN = os.environ.get('DOMAIN', 'localhost')
DOMAIN = env('DOMAIN')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEV')

# # show terminal django
# LOGGNG = {
    
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#         },
#     },  
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

#para definir el nombre del servidor y dominio. para que se vea bien el correo
SITE_ID = 1

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'apps.user',
    'apps.user_profile',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_api',
    'djoser',
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'channels',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS
  
MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
     
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# esto es donde se encuentra nuestra carpeta de url .py
ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'
#VERSION MEJORADA mas potente y comunicacion con mas personas 
ASGI_APPLICATION = 'core.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mozadev_auth_db',
        'USER': 'mozadev',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": 'redis://django_auth_api_redis:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
}
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Lima'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Usuaris externos solo pueden hacer requests a la API
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

#para autenticar con redes sociales
#MODEL BACKENDO ES SOLO PARA USUARIOS NORMALES DJANGO
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend', 
)


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    # 'TOKEN_OBTAIN_PAIR': 'rest_framework_simplejwt.views.TokenObtainPairView',
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90), # tiempo que el token caduca
    'REFRESH_TOKEN_LIFETIME': timedelta(days=180),
    'ROTATE_REFRESH_TOKENS': True, # para que el token se renueve
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKE_CLASSES': 
        ('rest_framework_simplejwt.tokens.AccessToken',)
}    
    
AUTH_USER_MODEL = 'user.UserAccount'    # NO ES NECESARIO PONER AUTH
    
DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SEND_ACTIVATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_URL': 'auth/forgot_password_confirm/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}',
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:8000/google', 'http://localhost:8000/facebook'],
      'SERIALIZERS': {
        'user_create': 'apps.user.serializers.UserSerializer',
        'user': 'apps.user.serializers.UserSerializer',
        'current_user': 'apps.user.serializers.UserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'TEMPLATES': {
        "activation": "email/activation.html",
        "confirmation": "email/confirmation.html",
        "password_reset": "email/password_reset.html",
        "password_changed_confirmation": "email/password_changed_confirmation.html",
        "username_changed_confirmation": "email/username_changed_confirmation.html",
        "username_reset": "email/username_reset.html",
    }, 
}

#NOS PERMITE HACER POST Y MAS EASYT   
FILE_UPLOAD_PERMISSIONS = 0o644

#PARA HACER DEBUG A NUESTRO REGISTRO DE USUARIOS
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    # CSRF_COOKIE_DOMAIN = os.environ.get('CSRF_COOKIE_DOMAIN_DEPLOY')
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEPLOY')
    CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
    CSRF_TUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS_DEPLOY')
    
    EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
    SECURE_SSL_REDIRECT = True
    
    #smtp.com para enviar correos
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
    
    #YOUR SMTP.COM SENDER ACCOUNT CREDENTIALS
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    
    #USE TLS WHEN CONNECTING TO SMTP.COM SERVER
    
    EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')== 'True'
    
    #default "from " address for sending emails
    DEFAULT_FROM_EMAIL = 'solomoza <noreply@solomoza.com>'

#DJANGO-CREDITOR NO FUNCIONA con s3 atravez  django storages sin this line in setting.py

    AWS_QUERYTRING_AUTH = False
    
    #aws setting
    
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_DEFAULT_ACL = 'public-read'
    
    #S3 STATIC SETTINGS
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'core.storage_backends.s3bo.StaticStorage'
    
    #s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.s3bo.MediaStorage'
    
    # STATICFILES_DIRS = (os.path.join(BASE_DIR, 'build/static'),)
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    