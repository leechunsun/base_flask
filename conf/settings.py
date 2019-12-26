import os

DEBUG = True
ENV = "test"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# 数据库配置
DB_HOST = ""
DB_PORT = ""
DB_DATABASE = ""
DB_USER = ""
DB_PASSWORD = ""
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
# 数据库链接池大小
SQLALCHEMY_POOL_SIZE = 10
# 默认链接超时时长
SQLALCHEMY_POOL_TIMEOUT = 10
# 提供多库链接 使用其他库进行链接的时候需要使用bind指定那个库使用
SQLALCHEMY_BINDS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

# REDIS配置
REDIS_CONFIGS = {
    "default": {
        "host": "",
        "port": "",
        "password": "",
    },
}


# 日志配置
LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            # 或者直接写路径
            'filename': os.path.join(BASE_DIR + '/logs/', 'all.log'),
            'when': 'D',  # this specifies the interval
            'interval': 1,  # defaults to 1, only necessary for other values
            'backupCount': 0,  # how many backup file to keep, 10 days
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'log': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
    }
}
