from flask import render_template
from . import main
from app import app 
from .request import get_articles,get_source


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_source = get_source()
   
    # print(popular_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular=popular_source)
    
@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    print(articles)
    title = f'{source_id}'

    return render_template('articles.html', title=title, article=articles)
    