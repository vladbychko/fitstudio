from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-заміни-на-свій-або-лиш-старий'

DEBUG = True

ALLOWED_HOSTS = ["*"]


# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'studio',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # важливо: LocaleMiddleware має бути після SessionMiddleware і до CommonMiddleware
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitstudio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # за потреби можна додати окрему папку templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # потрібен для i18n + перемикачів
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fitstudio.wsgi.application'


# Database — залиш як було
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
LANGUAGE_CODE = 'uk'

# дві мови — UA / EN
LANGUAGES = [
    ('uk', _('Українська')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',   # тут будуть .po файли
]

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',    # опціонально, якщо є глобальна статика
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media (для фото тренерів)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL — для тестів в консолі (в проді заміниш на SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@fitstudio.local'
CONTACT_FORM_RECIPIENT = 'you@example.com'   # сюди будуть приходити листи, заміни
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-replace-this"

DEBUG = False   # важливо для Render

ALLOWED_HOSTS = ["*"]    # дозволяємо всі хости


# -------------------------
# Installed apps
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'studio',   # твій застосунок
]


# -------------------------
# Middleware (WhiteNoise)
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise повинен стояти тут (другим!)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fitstudio.urls'


# -------------------------
# Templates
# -------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Django шукатиме шаблони всередині apps/templates/
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

WSGI_APPLICATION = 'fitstudio.wsgi.application'


# -------------------------
# DATABASE (default SQLite)
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -------------------------
# Password validators
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = "uk"
TIME_ZONE = "Europe/Kyiv"

USE_I18N = True
USE_TZ = True


# -------------------------
# STATIC FILES + WHITENOISE
# -------------------------

STATIC_URL = "/static/"

# Папка, з якої collectstatic збере файли
STATIC_ROOT = BASE_DIR / "staticfiles"

# Папки, де лежать твої CSS/JS (ручні файли)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# WhiteNoise storage — обовʼязково на Render
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

