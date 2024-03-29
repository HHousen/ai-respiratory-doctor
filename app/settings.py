from environs import Env
import logging

env = Env()
env.read_env()

TIMEZONE = env.str('TIMEZONE', default='America/New_York')

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

if ENV != 'development':
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2" + env.str('DATABASE_URL')[8:]
else:
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

SECRET_KEY = env.str('SECRET_KEY')
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)

ADMIN_CREDENTIALS = ('admin', env.str('ADMIN_PASSWORD', default='admin'))

DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False

CACHE_TYPE = 'simple'

if ENV != 'development':
    LOG_LEVEL = logging.INFO
else:
    LOG_LEVEL = logging.DEBUG
LOG_FILENAME = env.str('LOG_FILENAME', default='activity.log')
LOG_MAXBYTES = env.int('LOG_MAXBYTS', default=1024)
LOG_BACKUPS = env.int('LOG_BACKUPS', default=0)

UPLOAD_FOLDER = env.str('UPLOAD_FOLDER', default='uploads')

AUTO_CONFIRM = env.bool('AUTO_CONFIRM', default='False')

if env.bool("USE_MAIL"):
    MAIL_SERVER = env.str('MAIL_SERVER')
    MAIL_PORT = env.int('MAIL_PORT', default=465)
    MAIL_USE_TLS = env.bool('MAIL_USE_TLS', default=False)
    MAIL_USE_SSL = env.bool('MAIL_USE_SSL', default=True)
    MAIL_USERNAME = env.str('MAIL_USERNAME')
    MAIL_PASSWORD = env.str('MAIL_PASSWORD')
    ADMINS = ['flask.boilerplate@gmail.com']