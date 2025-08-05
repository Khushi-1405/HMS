INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
    'records',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For development only

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],  # If you're using a global template folder
        ...
    },
]
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'hospital_management_system',
        'USER' : 'root',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}

