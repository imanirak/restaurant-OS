import os
from .base import *
import environ

env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR) + '/.env')    
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    }
}
