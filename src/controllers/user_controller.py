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