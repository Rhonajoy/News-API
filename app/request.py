from os import name
from app import app
import urllib.request,json
from app.models import article
from .models import source




Source=source.Source
Article=article.Article
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the sources

def get_source():
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = 'https://newsapi.org/v2/sources?apiKey=2139fab7afd24744980d5c0ed96ad40a'
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results
#processing the source results
def process_results(source_list):
    '''
    Function  that processes the source results and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name= source_item.get('name')
        description= source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        
        
        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return  source_results

# https://newsapi.org/v2/top-headlines?sources={}&apiKey={}
# get articles by source id
def get_articles(source_id):
    '''
        Function that gets the json response to our url request using the source id
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(
        source_id, api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_results_articles(articles_results_list)
    return articles_results
    #processing the article results

def process_results_articles(articles_list):
    '''
     Function that processes the articles list result and transform them to a list of Objects
    '''
    articles_results = []

    for article_item in articles_list:
        id = article_item.get('id')
        name = article_item.get('name')
        author = article_item.get('author')
        url = article_item.get('url')
        title = article_item.get('title')
       
        
        urlToImage = article_item.get('urlToImage')
       
        content = article_item.get('content')

        if urlToImage:
            articles_object = Article(
                id,name,author,url,title,urlToImage,content)
            articles_results.append(articles_object)

    return articles_results
