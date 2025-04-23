import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
APPS_DIR = os.path.join(BASE_DIR, "apps")
if not os.path.exists(APPS_DIR):
    print("Creating apps directory...")
    os.mkdir(APPS_DIR)

# Checks if is debug mode.
DEBUG: bool = os.path.exists(".DEBUG")

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media files (Images, Video, etc)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# The standard secret key is not safe for development so we read it from a file.
SECRET_KEY: str = 'django-insecure-xu3$gii%)#nj+#69lm*i5e2y)9ui#o0krf2%t3jwft558pm(*q'
if not DEBUG:
    # Create directory if it does not exsist.
    if not os.path.exists(os.path.join(BASE_DIR, "etc")):
        print("Created etc directory.")
        os.mkdir(os.path.join(BASE_DIR, "etc"))
    
    try:
        with open(os.path.join(BASE_DIR, "etc/secret_key.txt")) as f:
            SECRET_KEY = f.read().strip()
    except FileNotFoundError:
        # todo - generate secret_key.txt automatically
        raise Exception("Unable to locate secret_key.txt")

# Any endpoint that we want this to go to we have to include here.
ALLOWED_HOSTS: list = [
    '127.0.0.1', 
    'localhost',
    'mainb.us', 
    'www.mainb.us',
]

# Routing
ROOT_URLCONF: str = 'mainbus.urls'
ASGI_APPLICATION: str = 'mainbus.asgi.application'
WSGI_APPLICATION: str = 'mainbus.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


INSTALLED_APPS: list = [
    #^ Built-in Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #^ Installed Applications
    'channels',                     # Primarly used for websockets.
    
    # Mainbus Applications
    'mainbus.apps.ApiConfig',
    'mainbus.apps.AuthenticationConfig',
    'mainbus.apps.BaseConfig',
    'mainbus.apps.PokerConfig',
    'mainbus.apps.WikiConfig',
    'mainbus.apps.FactoryConfig',
    'mainbus.apps.FilestoreConfig',
    'mainbus.apps.SupportConfig',
    'mainbus.apps.VMDashConfig',
    'mainbus.apps.LocationConfig',
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

AUTHENTICATION_BACKENDS = [
    'apps.authentication.backends.auth.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Configure templates
TEMPLATES: list = [
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

# Load template directory for each application in apps directory.
for fp in [os.path.join(os.path.join(os.path.join(BASE_DIR, "apps"), app), "templates") for app in os.listdir(APPS_DIR)]:
    TEMPLATES[0]["DIRS"].append(os.path.join(fp, "html"))


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

if DEBUG:
    CHANNEL_LAYERS: dict = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        },
    }
else:
    #todo> Setup redis as the CHANNEL backend.
    print("ChannelLayers not properly configured, failed to setup websocket connections.  Must deploy redis for production safe enviornment.")
    CHANNEL_LAYERS: dict = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [('127.0.0.1', 6379)],
            }
        }
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


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # Default Redis URL and port
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}