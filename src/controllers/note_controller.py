import sys
sys.path.append("..")

from utility import AESCipher
from models.db import db
from models.db import Note

class note_controller():
    def __init__(self, user_id, note_title=None, note_content=None, note_id=None):
        self.note_id = note_id
        self.user_id = user_id
        self.note_title = note_title
        self.note_content= note_content

    def get_notes(self):
        """
            Returns all notes of given user id
        """
        notes = Note.query.filter_by(user_id=self.user_id).all()
        return notes
    
    def get_note(self):
        """
            Returns a note of given note id and user id
        """
        aes = AESCipher()
        note = Note.query.filter_by(user_id=self.user_id, note_id=self.note_id).first()
        note.note_content = aes.decrypt(note.note_content)
        return note
        
    def create_note(self):
        aes = AESCipher()
        notes = Note(self.user_id, self.note_title, aes.encrypt(self.note_content))
        db.session.add(notes)
        db.session.commit()
    
    def update_note(self):
        """
            Update note of given note id with new contents
        """
        aes = AESCipher()
        note = Note.query.filter_by(user_id=self.user_id, note_id=self.note_id).first()
        note.note_title = self.note_title
        note.note_content = aes.encrypt(self.note_content)
        db.session.flush()
        db.session.commit()
    
    def delete_note(self):
        """
            Delete given note id and user id
        """
        Note.query.filter_by(user_id=self.user_id, note_id=self.note_id).delete()
        db.session.commit()
        return True
    def pin_note(self, pin):
        note = note.query.filter_by(note_id=self.note_id,user_id=self.user_id).first()
        note.pinned = pin
        db.session.flush()
        db.session.commit()