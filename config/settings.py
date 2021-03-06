"""
Django settings for mep_server project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from datetime import datetime, timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1(qysju(!_t&llyte@n5=wz6uk4b0sj6*f(fh0u_3mbuj4g3qz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    # 'corsheaders'
]

LOCAL_APPS = [
    "apps.users"
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 跨域或者用nginx处理
    'utils.mep_middleware.RequestIDMiddleware',  # 自定义request_id
    'utils.mep_middleware.CostTimeMiddleware',  # 自定义接口耗时
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'routers.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mep_server',
        'USER': 'root',
        'PASSWORD': '1q2w3e4r99',
        # 'HOST': '177.7.0.13',
        # 'PORT': '3306',
        'HOST': '127.0.0.1',
        'PORT': '13306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR / 'media'  # 在Windows开发环境下加上.replace("\\", "/")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 日志配置
# 创建日志的路径
LOG_PATH = BASE_DIR / 'log'
# 如果地址不存在，则自动创建log文件夹
if not LOG_PATH.exists():
    LOG_PATH.mkdir()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # 日志格式
        'standard': {
            # 'format': '[%(asctime)s] [%(request_id)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
            #           '[%(levelname)s]- %(message)s',
            'format': '{"asctime":"%(asctime)s","path":"%(path)s", "request_id":"%(request_id)s","lineno":%(lineno)d,"module":"%(funcName)s","level":"%(levelname)s","msg":"%(message)s"}'
            # 日志格式

        },
        'simple': {  # 简单格式
            'format': '%(levelname)s %(message)s'
        },
    },
    # 过滤
    'filters': {
        'request_id': {
                '()': 'utils.mep_middleware.RequestIDFilter'
            },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }

    },
    # 定义具体处理日志的方式
    'handlers': {
        # 默认记录所有日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH / 'all-{}.log'.format(datetime.now().strftime('%Y-%m-%d')),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'filters': ['request_id'],
            'encoding': 'utf-8',  # 设置默认编码，否则打印出来汉字乱码
        },
        # 输出错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH / 'error-{}.log'.format(datetime.now().strftime('%Y-%m-%d')),
            'maxBytes': 1024 * 1024 * 5,  # 文件大小
            'backupCount': 5,  # 备份数
            'formatter': 'standard',  # 输出格式
            'filters': ['request_id'],
            'encoding': 'utf-8',  # 设置默认编码
        },
        # 控制台输出
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'filters': ['request_id', 'require_debug_true'],
            'filters': ['request_id'],
            'formatter': 'standard'
        },
        # 输出info日志
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH / 'info-{}.log'.format(datetime.now().strftime('%Y-%m-%d')),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
            'filters': ['request_id'],
            'encoding': 'utf-8',  # 设置默认编码
        },
    },
    # 配置用哪几种 handlers 来处理日志
    'loggers': {
        # 类型 为 django 处理所有类型的日志， 默认调用
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        # log 调用时需要当作参数传入
        'log': {
            'handlers': ['error', 'info', 'console', 'default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}
