from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap 
#initializing application
app= Flask(__name__,instance_relative_config=True)
#Setting up Configuration
app.config.from_object(DevConfig)

bootstrap = Bootstrap(app)
def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app

from app import views
from app import error