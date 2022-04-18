import sys

sys.path.append("..")

from models.db import db
from models.db import pswrd

class pswrd_controller():
    def __init__(self,user_id,pswrd_title=None, pswrd_content=None):
        
        self.user_id = user_id
        self.pswrd_title = pswrd_title
        self.pswrd_content= pswrd_content
        

    def get_pswrds(self):
        pswrds = pswrd.query.filter_by(user_id=self.user_id).all()
        return pswrds
        
    def create_pswrd(self):
        pswrds = pswrd(self.pswrd_id,self.user_id, self.pswrd_title, self.pswrd_content)
        db.session.add(pswrds)
        db.session.commit()
    
    def delete_pswrd(self):
        pswrd.query.filter_by(user_id=self.user_id, pswrd_id=self.pswrd_id).delete()
        db.session.commit()
        return True