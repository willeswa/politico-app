""" Defines runtime environment configurations """

# Standard import
import os


class Config:
    """ Define common configurations for all environments """
    SECRET_KEY = os.getenv('SECRET_KEY')


class TestingConfig(Config):
    """ Defines configurations for testing """

    TESTING = True


class DevelopmentConfig(Config):
    """ Defines configurations for development """

    DEBUG = True


class ProductionConfig(Config):
    """ Defines configurations for production """

    TESTING = False
    DEBUG = False


APP_CONFIG = dict(
    testing=TestingConfig,
    development=DevelopmentConfig,
    production=ProductionConfig
)
