from flask import render_template
from .request import get_source
from app import app 
from .request import get_articles


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_source = get_source()
    print(popular_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_source)
    
@app.route('/news-source/articles/<source_id>')
def articles(source_id):
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles(source_id)
    title = f'{source_id}'

    return render_template('articles.html', title=title, article=articles)
    