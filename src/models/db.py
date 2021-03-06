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
    bookmark_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    bookmark_title = db.Column(db.String(165), nullable=False)
    bookmark_desc = db.Column(db.String(1024), nullable=True)
    bookmark_url = db.Column(db.String(1024), nullable=False)
    pinned = db.Column(db.Integer,default=0)

    def __init__(self, user_id, bookmark_title, bookmark_desc, bookmark_url):
        self.user_id = user_id
        self.bookmark_title = bookmark_title
        self.bookmark_url = bookmark_url
        self.bookmark_desc = bookmark_desc

class Document(db.Model):
    document_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    document_title = db.Column(db.String(165), nullable=False)
    document_cont= db.Column(db.String(1024), nullable=False)
    pinned = db.Column(db.Integer,default=0)

    def __init__(self, user_id, document_title, document_cont):
        self.user_id = user_id
        self.document_title = document_title
        self.document_cont = document_cont

class pswrd(db.Model):
    pswrd_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    pswrd_user = db.Column(db.String(165), nullable=False)
    pswrd_title = db.Column(db.String(165), nullable=False)
    pswrd_content = db.Column(db.String(1024), nullable=True)
    pinned = db.Column(db.Integer,default=0)
   

    def __init__(self, user_id, pswrd_user, pswrd_title, pswrd_content):
        self.user_id = user_id
        self.pswrd_user = pswrd_user
        self.pswrd_title = pswrd_title
        self.pswrd_content= pswrd_content

class Note(db.Model):
    note_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    note_title = db.Column(db.String(165), nullable=False)
    note_content = db.Column(db.String(1024), nullable=True)
    pinned = db.Column(db.Integer,default=0)
   
    def __init__(self, user_id, note_title, note_content):
        self.user_id = user_id
        self.note_title = note_title
        self.note_content= note_content