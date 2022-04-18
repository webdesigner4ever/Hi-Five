import sys

sys.path.append("..")

from models.db import db
from models.db import Document

class document_controller():
    def __init__(self, user_id, document_title=None,  document_desc=None, document_cont=None):
        self.user_id = user_id
        self.document_title = document_title
        self.document_desc = document_desc
        self.document_cont = document_cont
        

    def get_documents(self):
        documents = Document.query.filter_by(user_id=self.user_id).all()
        return documents
        
    def create_document(self):
        document = Document(self.document_id,self.user_id, self.document_title, self. document_desc, self.document_cont)
        db.session.add(bookmark)
        db.session.commit()
    
    def delete_document(self):
        Document.query.filter_by(user_id=self.user_id, document_id=self.document_id).delete()
        db.session.commit()
        return True

     