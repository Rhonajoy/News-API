import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_ARTICLES_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY ='2139fab7afd24744980d5c0ed96ad40a'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}