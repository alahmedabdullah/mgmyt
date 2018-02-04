import environ

project_root = environ.Path(__file__) - 3  
env = environ.Env(DEBUG=(bool, False),)  
CURRENT_ENV = 'dev' # 'dev' is the default environment

# read the .env file associated with the settings that're loaded
env.read_env('./mgmyt/{}.env'.format(CURRENT_ENV))

DATABASES = {  
    'default': env.db()
}

SECRET_KEY = env('SECRET_KEY')  
DEBUG = env('DEBUG')  

#Added following line as extra
DEBUG=True

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'rest_framework',
    'tardis.apps.mongoquery',
)

ROOT_URLCONF = 'mgmyt.urls'

STATIC_URL = '/static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = [
    env('FRONTEND_ROOT')
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [env('FRONTEND_ROOT')],
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {

        'timestamped': {
            'format': '[%(asctime)s: %(levelname)s/%(processName)s/%(name)s.%(funcName)s] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'class':'logging.StreamHandler',
            'formatter': 'timestamped'
            },
        'file': {
            'class':'logging.FileHandler',
            'formatter': 'timestamped',
            'filename':'debug.log'
            },
    },
    'loggers': {
        'tardis.apps.mongoquery': {
            'level': 'DEBUG',
            'handlers': ['default','file'],
            },
    }
}
