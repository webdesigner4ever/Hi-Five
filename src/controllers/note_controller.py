import sys

sys.path.append("..")

from models.db import db
from models.db import Note

class note_controller():
    def __init__(self,user_id,note_title=None, note_content=None):
        
        self.user_id = user_id
        self.note_title = note_title
        self.note_content= note_content
        

    def get_notes(self):
        notes = Note.query.filter_by(user_id=self.user_id).all()
        return notes
        
    def create_note(self):
        notes = Note(self.note_id,self.user_id, self.note_title, self.note_content)
        db.session.add(notes)
        db.session.commit()
    
    def delete_note(self):
        Note.query.filter_by(user_id=self.user_id, note_id=self.note_id).delete()
        db.session.commit()
        return True