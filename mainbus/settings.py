import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = os.path.join(BASE_DIR, "apps")

# Checks if is debug mode.
DEBUG: bool = os.path.exists(".DEBUG")

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media files (Images, Video, etc)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Secret key reading.
SECRET_KEY: str = 'django-insecure-xu3$gii%)#nj+#69lm*i5e2y)9ui#o0krf2%t3jwft558pm(*q'
if not DEBUG:
    try:
        with open("etc/secret_key.txt") as f:
            SECRET_KEY = f.read().strip()
    except FileNotFoundError:
        # todo - generate secret_key.txt automatically
        raise Exception("Unable to locate secret_key.txt")

ALLOWED_HOSTS: list = [
    '127.0.0.1', 
    'localhost',
    'mainb.us', 
    'www.mainb.us',
]

ROOT_URLCONF: str = 'mainbus.urls'
WSGI_APPLICATION: str = 'mainbus.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


INSTALLED_APPS: list = [
    # Default Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Installed Apps
    'channels',
    
    # Custom Apps
    #'mainbus.apps.api',
    'mainbus.apps.BaseConfig',
    'mainbus.apps.AuthenticationConfig',
    'mainbus.apps.PokerConfig',
    'mainbus.apps.WikiConfig',
    'mainbus.apps.FactoryConfig',
    'mainbus.apps.FilestoreConfig',
]

# Middle wear
MIDDLEWARE: list = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# todo: not sure this is still required.
_APP_DIR: str = os.path.join(BASE_DIR, "apps")
_APP_TEMPLATE_DIRS: list = [os.path.join(os.path.join(_APP_DIR, app), "templates") for app in os.listdir(_APP_DIR)]
_APP_TEMPLATE_CONTENT: list = []
for template_path in _APP_TEMPLATE_DIRS:
    _APP_TEMPLATE_CONTENT.append(os.path.join(template_path, "html"))
    _APP_TEMPLATE_CONTENT.append(os.path.join(template_path, "js"))
    _APP_TEMPLATE_CONTENT.append(os.path.join(template_path, "css"))

# Templates
TEMPLATES: list = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            d for d in _APP_TEMPLATE_CONTENT
        ],
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

# Database
DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS: list = [
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

# todo: change
AUTH_USER_MODEL = "authentication.User"

# Used by 'channels' for websockets
CHANNEL_LAYERS: dict = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# Logging
LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'handlers': {
    'file': {
        'level': 'DEBUG',
        'class': 'logging.FileHandler',
        'filename': os.path.join(BASE_DIR,'mainbus.log'),
    },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}