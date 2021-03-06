import os
import urlparse

class Config(object):
    DEBUG = False
    TESTING = False
    DB_NAME = "sensorDB"
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DATABASE = "sensorDB"
    MONGODB_USERNAME = None
    MONGODB_PASSWORD = None

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://:@localhost:27017/sensorDB")
    url = urlparse.urlparse(MONGO_URI)
    DB_NAME = url.path[1:]
    MONGODB_HOST = url.hostname
    MONGODB_PORT = url.port
    MONGODB_DATABASE = DB_NAME
    MONGODB_USERNAME = url.username
    MONGODB_PASSWORD = url.password

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    DB_NAME = "sensorDB"
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DATABASE = "sensorDB"
    MONGODB_USERNAME = None
    MONGODB_PASSWORD = None

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = "sensorDB"
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DATABASE = "sensorDB"
    MONGODB_USERNAME = None
    MONGODB_PASSWORD = None

class DebugConfig(Config):
    DEBUG = True
    TESTING = False
    MONGO_URI = os.getenv("MONGO_URL", "mongodb://:@localhost:27017/sensorDB")
    url = urlparse.urlparse(MONGO_URI)
    DB_NAME = url.path[1:]
    MONGODB_HOST = url.hostname
    MONGODB_PORT = url.port
    MONGODB_DATABASE = DB_NAME
    MONGODB_USERNAME = url.username
    MONGODB_PASSWORD = url.password

    if MONGODB_USERNAME == "":
        MONGODB_USERNAME = None
    
    if MONGODB_PASSWORD == "":
        MONGODB_PASSWORD = None
