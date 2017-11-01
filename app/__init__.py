from flask import Flask
from flask_bootstrap import Bootstrap # from flask_bootstrap

app = Flask(__name__)
app.config.from_object('config') # get configuration
# app: the variable assigned an instance of Flask
from app import views
# app: the package we import the views module

bootstrap = Bootstrap(app)
