from flask import render_template
from .request import get_source
from app import app 
#views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    financial_news = get_source('financial_news')
    print(financial_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,financial_news = financial_news)
    
    