import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'dev': DevConfig,
    'test': TestConfig,
    'stage': StagingConfig,
    'prod': ProdConfig
}
