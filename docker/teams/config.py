class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {'host': 'mongodb://teams_mongodb/teams'}

class ProductionConfig(Config):
    "Here will go the production config"

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"

