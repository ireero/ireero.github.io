# config.py
import os

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback')

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
