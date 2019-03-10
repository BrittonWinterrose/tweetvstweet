"""Use SqlAlchemy models (schemas) for Tweet VS Tweet"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we pull and analyze Tweets for."""
    # What is the format of the primary key?
    id = DB.Column(DB.Integer, primary_key=True) 
    # What is the format of the twitter ID?
    name = DB.Column(DB.String(15))

    # Here we define a helpful string representation for formatting usernames
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets"""
    # A primary key ID for the tweet.
    id = DB.Column(DB.Integer, primary_key=True)
    # The text data from the tweet.
    text = DB.Column(DB.Unicode(280))
    # Define many Tweets to one User so we add UserID foreign key and mandate it with nullable.
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    # Add user relationship to autofill username for conveninence. So we don't have to query both tables. 
    user = DB.relationship('User', backref=DB.backref('tweets',lazy=True))

    # Here we define a helpful string representation for formatting tweets
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)