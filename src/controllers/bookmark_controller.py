import sys

sys.path.append("..")

from models.db import db
from models.db import Bookmark

class bookmark_controller():
    def __init__(self, user_id, bookmark_title=None, bookmark_desc=None, bookmark_url=None):
        self.user_id = user_id
        self.bookmark_title = bookmark_title
        self.bookmark_url = bookmark_url
        self.bookmark_desc = bookmark_desc

    def get_bookmarks(self):
        bookmarks = Bookmark.query.filter_by(user_id=self.user_id).all()
        return bookmarks
        
    def create_bookmark(self):
        bookmark = Bookmark(self.user_id, self.bookmark_title, self.bookmark_desc, self.bookmark_url)
        db.session.add(bookmark)
        db.session.commit()
    
        