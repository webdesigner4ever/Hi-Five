import sys

sys.path.append("..")

from models.db import db
from models.db import Document

class document_controller():
    def __init__(self, user_id, document_title=None,document_cont=None, document_id=None):
        self.user_id = user_id
        self.document_title = document_title
        self.document_cont = document_cont
        self.document_id = document_id        

    def get_documents(self):
        documents = Document.query.filter_by(user_id=self.user_id).all()
        return documents
        
    def create_document(self):
        document = Document(self.user_id, self.document_title, self.document_cont)
        db.session.add(document)
        db.session.commit()
    
    def delete_document(self):
        Document.query.filter_by(user_id=self.user_id, document_id=self.document_id).delete()
        db.session.commit()
        return True

     