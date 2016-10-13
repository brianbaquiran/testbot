class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    PAGE_ACCESS_TOKEN = "replace with actual page access token"
