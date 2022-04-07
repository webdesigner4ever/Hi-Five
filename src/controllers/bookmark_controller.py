import sys

sys.path.append("..")

from models.db import db
from models.db import Bookmark

class bookmark_controller():
    def __init__(self, user_id, bookmark_title, bookmark_desc, bookmark_url):
        self.user_id = user_id
        self.bookmark_title = bookmark_title
        self.bookmark_url = bookmark_url
        self.bookmark_desc = bookmark_desc

    def create_bookmark():
        bookmark = Bookmark(self.user_id, self.bookmark_title, self.bookmark_desc, self.bookmark_url)
        db.session.add(bookmark)
        db.session.commit()
    
        