import sys

sys.path.append("..")

from models.db import db
from models.db import User

class user_controller:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def register(self):
        user = User(self.username, self.password)
        db.session.add(user)
        db.session.commit()

    def login(self):
        user = User.query.filter_by(username=self.username, password=self.password).first()
        if user is None:
            return False
        else:
            return user
    
    def changepassword(self,currentpassword,newpassword):
        user = User.query.filter_by(username=self.username, password=currentpassword).first()
        if user is not None:
            user.password = newpassword
            db.session.flush()
            db.session.commit()
            return True
        else:
            return False

       