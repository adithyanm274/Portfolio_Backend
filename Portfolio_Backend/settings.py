"""
Django settings for Portfolio_Backend project.
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ===== SECURITY =====
# Use environment variable for SECRET_KEY; fallback for local dev only
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me-in-production')

# DEBUG: True only in development
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'portfolio-backend-fda8.onrender.com,localhost,127.0.0.1').split(',')# Example Render domain will be added automatically via env variable later

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'corsheaders',
    'whitenoise.runserver_nostatic',  # WhiteNoise for static
    # Your app
    'contact',
    "anymail",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',          # Highest possible
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',      # After Security
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Portfolio_Backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Portfolio_Backend.wsgi.application'

# ===== DATABASE =====
# Use PostgreSQL on Render, fallback to SQLite for local development
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=True if os.environ.get('RENDER') else False  # Render requires SSL
    )
}

# ===== STATIC FILES (WhiteNoise) =====
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===== CORS =====
CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')
    if origin.strip()
]
# Later you will set CORS_ORIGINS env var on Render to your Vercel URL
CORS_ALLOW_CREDENTIALS = True

# ===== EMAIL SETTINGS (Keep Gmail) =====
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {
 "RESEND_API_KEY": os.environ.get("RESEND_API_KEY"),
}
# Set a default from address (must be a verified domain in Resend, or the testing one)
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "Portfolio Contact <onboarding@resend.dev>")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# ===== REMAINING SETTINGS (unchanged) =====
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===== Email Settings (Gmail) =====
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'adithyan.m.2742001@gmail.com'      # 🔁 Replace with your Gmail address
# EMAIL_HOST_PASSWORD = 'lwci esyo wdqf aaqh'     # 🔁 Replace with an App Password (see note below)

# re_bkhFzRaU_FTdJDCLJJDvpqJJ8P8LaFwaN