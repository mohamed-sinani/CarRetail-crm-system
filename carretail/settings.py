
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='django-insecure-*u95s8*0d%9l+n8+y=n#^wn(%ahw(d4yvnn)k)@^*#mu27*jb1'
DEBUG=True
ALLOWED_HOSTS=[]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'accounts',
    'dashboard',
    'vehicles',
    'customers',
    'deals',
    'sales',
    'reports',
    'announcements',
    'inbox',
    'public',
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
ROOT_URLCONF='carretail.urls'
TEMPLATES = [
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[BASE_DIR/'templates'],
        'APP_DIRS':True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'inbox.context_processors.inquiry_count',
            ],
        },
    },
]
WSGI_APPLICATION='carretail.wsgi.application'
AUTH_USER_MODEL='accounts.User'
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'carretail_db',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS': {
            'charset':'utf8mb4',
        },
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
STATIC_URL='static/'
STATICFILES_DIRS=[BASE_DIR/'static']
MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR/'media'
DEALER_PHONE='+254700000000'
