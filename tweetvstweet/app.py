"""Main application and routing logic for TweetVsTweet"""
from flask import Flask
from .models import DB

def create_app():
    """Create and Configure an instance of the flask application"""
    app = Flask(__name__)

    # This tells the app about the database
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'

    # This tells the Database to register to the app. 
    DB.init_app(app)

    @app.route("/")
    def root():
         return "Welcome to TweetVsTweet"
    return app