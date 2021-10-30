from app import app
#Getting api key

from app import app
import urllib.request,json
from .models import source

Source=source.Source
# Getting api key
api_key= app.config['NEWS_API_KEY']

# Getting the source base url
base_url = app.config["NEWS_API_BASE_URL "]
def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads( get_source_data)

        movie_results = None

        if get_source_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results
