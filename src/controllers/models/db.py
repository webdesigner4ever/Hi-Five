from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer , primary_key=True , autoincrement=True)
    username = db.Column(db.String(65), nullable=False)
    password = db.Column(db.String(65), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Bookmark(db.Model):
    bookmark_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id), primary_key=True)
    bookmark_title = db.Column(db.String(165), nullable=False)
    bookmark_desc = db.Column(db.String(1024), nullable=True)
    bookmark_url = db.Column(db.String(1024), nullable=False)

    def __init__(self, user_id, bookmark_title, bookmark_desc, bookmark_url):
        self.user_id = user_id
        self.bookmark_title = bookmark_title
        self.bookmark_url = bookmark_url
        self.bookmark_desc = bookmark_desc